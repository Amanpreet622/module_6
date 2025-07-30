import unittest
from mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

class TestMortgageLoanAmount(unittest.TestCase):
    def test_set_loan_amount_type_error(self):
        mortgage = Mortgage(100000, 0.05, 10, PaymentFrequency.MONTHLY)
        with self.assertRaises(TypeError):
            mortgage.loan_amount = "invalid"

    def test_set_loan_amount_zero(self):
        mortgage = Mortgage(100000, 0.05, 10, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0

    def test_set_loan_amount_negative(self):
        mortgage = Mortgage(100000, 0.05, 10, PaymentFrequency.MONTHLY)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = -500

    def test_set_loan_amount_valid_update(self):
        mortgage = Mortgage(100000, 0.05, 10, PaymentFrequency.MONTHLY)
        mortgage.loan_amount = 200000
        self.assertEqual(mortgage.loan_amount, 200000)

    def test_get_loan_amount(self):
        mortgage = Mortgage(150000, 0.05, 10, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.loan_amount, 150000)

if __name__ == "__main__":
    unittest.main()
