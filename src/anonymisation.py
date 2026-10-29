import re


def masquer_secrets(texte: str) -> str:
    return re.sub(r"(?i)\b(password|token|api_key)=\S+", r"\1=[SECRET]", texte)


def anonymiser(texte: str) -> str:
    return masquer_secrets(texte)