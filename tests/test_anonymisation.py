import unittest

from src.anonymisation import anonymiser


class TestAnonymisation(unittest.TestCase):
    def test_secret_masque(self):
        self.assertEqual(
            anonymiser("login token=abc user=bob"),
            "login token=[SECRET] user=bob",
        )


if __name__ == "__main__":
    unittest.main()