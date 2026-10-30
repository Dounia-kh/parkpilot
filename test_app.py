import unittest

from app import repondre


class TestApp(unittest.TestCase):
    def test_health(self):
        self.assertEqual(repondre("/health"), (200, {"status": "ok"}))

    def test_tarif(self):
        self.assertEqual(repondre("/tarif/90")[1]["tarif"], 4.0)

    def test_duree_invalide(self):
        self.assertEqual(repondre("/tarif/abc")[0], 400)

    def test_inconnu(self):
        self.assertEqual(repondre("/nimporte")[0], 404)


if __name__ == "__main__":
    unittest.main()