import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from src.tarif import calculer_tarif


def repondre(chemin):
    if chemin == "/health":
        return 200, {"status": "ok"}
    if chemin == "/version":
        return 200, {"version": os.getenv("APP_VERSION", "dev")}
    if chemin.startswith("/tarif/"):
        try:
            minutes = int(chemin.split("/")[2])
            return 200, {"minutes": minutes, "tarif": calculer_tarif(minutes)}
        except ValueError:
            return 400, {"erreur": "durée invalide"}
    return 404, {"erreur": "introuvable"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        statut, corps = repondre(self.path)
        donnees = json.dumps(corps).encode()
        self.send_response(statut)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(donnees)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()