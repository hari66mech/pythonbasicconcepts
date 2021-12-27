from bank.values.customer import Customer
from bank.values.interest_rate import Interest


"""Method overriding"""


class ReserveBankOfIndia:
    """Parent Class"""

    def __init__(self, deposit_amount, year):
        """This is a ReserveBankOfIndia class constructor"""
        self.deposit_amount = deposit_amount
        self.year = year
        self.interest_rate = Interest.reserve_bank_interest_rate
        self.bank_name = "Reserve Bank Of India"

    def get_bank_name(self):
        """This method is used to get RBI bank name"""
        print("This is a", self.bank_name)

    def simple_interest(self):
        """This method is used to calculate the simple interest for the Reserve bank of India"""
        interest = (self.deposit_amount * self.year * self.interest_rate) / 100
        total_amount = self.deposit_amount + interest
        return total_amount

    def show_interest(self):
        """This method is used to show final amount"""
        print("Finally will get RS.", ReserveBankOfIndia.simple_interest(self), "\n")


class StateBankOfIndia(ReserveBankOfIndia):
    """Child Class. It's extended from ReserveBankOfIndia class"""

    def __init__(self, deposit_amount, year):
        """This is a StateBankOfIndia class constructor"""
        ReserveBankOfIndia.__init__(self, deposit_amount, year)
        self.interest_rate = Interest.state_bank_interest_rate
        self.bank_name = "State Bank Of India"

    def get_bank_name(self):
        """This method is used to get SBI bank name"""
        print("This is a", self.bank_name)

    def simple_interest(self):
        """This method is used to calculate the simple interest for the State bank of India"""
        interest = (self.deposit_amount * self.year * self.interest_rate) / 100
        total_amount = self.deposit_amount + interest
        return total_amount


class HDFC(ReserveBankOfIndia):
    """Child Class. It's extended from ReserveBankOfIndia class"""

    def __init__(self, deposit_amount, year):
        """This is a HDFC class constructor"""
        ReserveBankOfIndia.__init__(self, deposit_amount, year)
        self.interest_rate = Interest.hdfc_bank_interest_rate
        self.bank_name = "HDFC Bank"

    def get_bank_name(self):
        """This method is used to get HDFC bank name"""
        print("This is a", self.bank_name)

    def simple_interest(self):
        """This method is used to calculate the simple interest for the HDFC bank"""
        interest = (self.deposit_amount * self.year * self.interest_rate) / 100
        total_amount = self.deposit_amount + interest
        return total_amount


print("Hi", Customer.customer_name)

reserveBank = ReserveBankOfIndia(Customer.deposit_amount, Customer.year)
reserveBank.get_bank_name()
reserveBank.simple_interest()
reserveBank.show_interest()

sbi = StateBankOfIndia(Customer.deposit_amount, Customer.year)
sbi.get_bank_name()
sbi.simple_interest()
sbi.show_interest()

hdfc = HDFC(Customer.deposit_amount, Customer.year)
hdfc.get_bank_name()
hdfc.simple_interest()
hdfc.show_interest()
