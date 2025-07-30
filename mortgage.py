from mortgage.payment_frequency import PaymentFrequency

class Mortgage:
    # Allowed amortization years
    __amortization_years = [5, 10, 15, 20, 25, 30]

    def __init__(self, loan_amount, annual_interest_rate, amortization, frequency):
        # Check loan_amount is a positive number
        if not isinstance(loan_amount, (int, float)):
            raise TypeError("Loan amount must be a number.")
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")

        # Check interest rate is a number between 0 and 1 (exclusive 0)
        if not isinstance(annual_interest_rate, (int, float)):
            raise TypeError("Annual interest rate must be a number.")
        if annual_interest_rate <= 0 or annual_interest_rate > 1:
            raise ValueError("Interest rate must be > 0 and <= 1.")

        # Check amortization is in allowed list
        if amortization not in Mortgage.__amortization_years:
            raise ValueError(f"Amortization must be one of {Mortgage.__amortization_years}.")

        # Check frequency is a PaymentFrequency enum
        if not isinstance(frequency, PaymentFrequency):
            raise ValueError("Frequency must be a PaymentFrequency enum value.")

        # Store values privately
        self.__loan_amount = loan_amount
        self.__annual_interest_rate = annual_interest_rate
        self.__amortization = amortization
        self.__frequency = frequency

    # loan_amount getter/setter with checks
    @property
    def loan_amount(self):
        return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Loan amount must be a number.")
        if value <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        self.__loan_amount = value

    # annual_interest_rate getter/setter with checks
    @property
    def annual_interest_rate(self):
        return self.__annual_interest_rate

    @annual_interest_rate.setter
    def annual_interest_rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Interest rate must be a number.")
        if value <= 0 or value > 1:
            raise ValueError("Interest rate must be > 0 and <= 1.")
        self.__annual_interest_rate = value

    # amortization getter/setter with checks
    @property
    def amortization(self):
        return self.__amortization

    @amortization.setter
    def amortization(self, value):
        if value not in Mortgage.__amortization_years:
            raise ValueError(f"Amortization must be one of {Mortgage.__amortization_years}.")
        self.__amortization = value

    # frequency getter/setter with checks
    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        if not isinstance(value, PaymentFrequency):
            raise ValueError("Frequency must be a PaymentFrequency enum value.")
        self.__frequency = value

    # Calculate the payment amount per period
    def get_payment(self):
        P = self.__loan_amount
        i = self.__annual_interest_rate / self.__frequency.value  # Interest rate per payment period
        n = self.__amortization * self.__frequency.value          # Total number of payments

        # If interest rate is zero, just divide loan by number of payments
        if i == 0:
            payment = P / n
        else:
            # Mortgage payment formula
            payment = P * (i * (1 + i)**n) / ((1 + i)**n - 1)

        return round(payment, 2)

    # Friendly string output
    def __str__(self):
        return (
            f"Loan Amount: ${self.__loan_amount:,.2f}\n"
            f"Interest Rate: {self.__annual_interest_rate * 100:.2f}%\n"
            f"Amortization (years): {self.__amortization}\n"
            f"Payment Frequency: {self.__frequency.name}\n"
            f"Payment Amount: ${self.get_payment():,.2f}"
        )

    # Developer-friendly representation
    def __repr__(self):
        return (f"Mortgage({self.__loan_amount}, {self.__annual_interest_rate}, "
                f"{self.__amortization}, {self.__frequency.name})")
