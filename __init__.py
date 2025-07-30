import unittest
from mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

class TestMortgageInit(unittest.TestCase):
    def test_loan_amount_type_error(self):
        with self.assertRaises(TypeError):
            Mortgage("not a number", 0.05, 10, PaymentFrequency.MONTHLY)

    def test_loan_amount_value_error_zero(self):
        with self.assertRaises(ValueError):
            Mortgage(0, 0.05, 10, PaymentFrequency.MONTHLY)

    def test_loan_amount_value_error_negative(self):
        with self.assertRaises(ValueError):
            Mortgage(-100, 0.05, 10, PaymentFrequency.MONTHLY)

    def test_interest_rate_type_error(self):
        with self.assertRaises(TypeError):
            Mortgage(100000, "not a number", 10, PaymentFrequency.MONTHLY)

    def test_interest_rate_value_error_zero_or_less(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0, 10, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            Mortgage(100000, -0.01, 10, PaymentFrequency.MONTHLY)

    def test_interest_rate_value_error_greater_than_one(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 1.5, 10, PaymentFrequency.MONTHLY)

    def test_amortization_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0.05, 7, PaymentFrequency.MONTHLY)

    def test_frequency_value_error(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 0.05, 10, "WEEKLY")  # Not PaymentFrequency enum

    def test_valid_initialization(self):
        mortgage = Mortgage(100000, 0.05, 10, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.loan_amount, 100000)
        self.assertEqual(mortgage.annual_interest_rate, 0.05)
        self.assertEqual(mortgage.amortization, 10)
        self.assertEqual(mortgage.frequency, PaymentFrequency.MONTHLY)

if __name__ == "__main__":
    unittest.main()
