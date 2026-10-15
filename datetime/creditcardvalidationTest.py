import unittest
from datetime import date
from creditcardvalidation import validateCard

class CreditCardValidationTest(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def test_validateCard_valid(self):
        result = validateCard(date(2026, 10, 15))
        self.assertEqual("Valid", result)

    def test_validateCard_expired(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2026, 10, 13))

    def tearDown(self):
        print("TearDown")

if __name__ == '__main__':
    unittest.main()
