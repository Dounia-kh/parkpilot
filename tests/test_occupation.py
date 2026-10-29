import unittest

from src.occupation import classer_occupation


class TestOccupation(unittest.TestCase):
    def test_sature(self):
        self.assertEqual(classer_occupation(0.9), "saturé")
        self.assertEqual(classer_occupation(1.0), "saturé")

    def test_charge(self):
        self.assertEqual(classer_occupation(0.6), "chargé")

    def test_fluide(self):
        self.assertEqual(classer_occupation(0.2), "fluide")

    def test_invalide(self):
        with self.assertRaises(ValueError):
            classer_occupation(1.5)


if __name__ == "__main__":
    unittest.main()