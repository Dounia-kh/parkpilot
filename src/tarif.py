import math

MINUTES_GRATUITES = 15
TARIF_HORAIRE = 2.0
PLAFOND_JOURNALIER = 15.0


def calculer_tarif(minutes: int) -> float:
    """Tarif en euros : 15 min gratuites, 2 euros par heure commencée, plafond 15 euros."""
    if minutes < 0:
        raise ValueError("durée négative")
    if minutes <= MINUTES_GRATUITES:
        return 0.0
    heures = math.ceil(minutes / 60)
    return min(heures * TARIF_HORAIRE, PLAFOND_JOURNALIER)


def formater_tarif(montant: float) -> str:
    return f"{montant:.2f} EUR"  

#calcul du tarif de stationnement 