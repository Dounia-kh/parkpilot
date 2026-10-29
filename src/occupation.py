def classer_occupation(taux: float) -> str:
    if taux < 0 or taux > 1:
        raise ValueError("taux hors limites")
    if taux >= 0.9:
        return "saturé"
    if taux >= 0.6:
        return "chargé"
    return "fluide"