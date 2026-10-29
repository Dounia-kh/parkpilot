import unittest

from src.tarif import calculer_tarif


class TestTarif(unittest.TestCase):
    def test_gratuit(self):
        self.assertEqual(calculer_tarif(0), 0.0)
        self.assertEqual(calculer_tarif(15), 0.0)

    def test_premiere_heure(self):
        self.assertEqual(calculer_tarif(16), 2.0)
        self.assertEqual(calculer_tarif(60), 2.0)

    def test_heure_commencee(self):
        self.assertEqual(calculer_tarif(61), 4.0)
        self.assertEqual(calculer_tarif(90), 4.0)

    def test_plafond(self):
        self.assertEqual(calculer_tarif(1440), 15.0)

    def test_negatif(self):
        with self.assertRaises(ValueError):
            calculer_tarif(-1)


if __name__ == "__main__":
    unittest.main()