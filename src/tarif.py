import math

MINUTES_GRATUITES = 15
TARIF_HORAIRE = 2.0
PLAFOND_JOURNALIER = 15.0


def calculer_tarif(minutes: int) -> float:
    if minutes < 0:
        raise ValueError("durée négative")
    if minutes <= MINUTES_GRATUITES:
        return 0.0
    heures = math.ceil(minutes / 60)
    return min(heures * TARIF_HORAIRE, PLAFOND_JOURNALIER)