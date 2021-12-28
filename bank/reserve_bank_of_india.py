from bank.abstraction_classes.atm import ATM
from bank.abstraction_classes.feature import Features
from bank.abstraction_classes.interest import Interest
from values.customer import Customer
from values.bank import Bank


class RBISimpleInterest(Interest):
    """This is an abstract class. It used to calculate simple interest"""
    def simple_interest(self):
        """"This method is used to calculate RBI simple interest"""
        interest = (Customer.deposit_amount * Customer.saving_year * Bank.RBI_interest) / 100
        total_amount = Customer.deposit_amount + interest
        print("\nThis is a RBI simple interest")
        return total_amount


class RBICompoundInterest(Interest):
    """This is an abstract class. It used to calculate compound interest"""
    def compound_interest(self):
        """This method is used to calculate RBI compound interest"""
        final_amount = Customer.deposit_amount*(1 + (Bank.RBI_interest / 100)) ** Customer.saving_year
        print("\nThis is a RBI compound interest")
        return final_amount


class RBI(RBISimpleInterest, RBICompoundInterest, ATM, Features):
    """This is a concrete class. This class is extended from RBISimpleInterest, RBICompoundInterest, ATM, Features classes"""
    def verify_pin_number(self):
        """This method used to verify pin number"""
        if Bank.pin_number == Customer.pin_number:
            current_payment = Customer.initial_amount - Customer.withdrawal_amount
            print("\nInitial Payment is Rs.", Customer.initial_amount)
            print("withdrawal payment is RS.", Customer.withdrawal_amount)
            print("Current payment is RS.", current_payment)
        else:
            print("Transaction declined")

    def show_services(self):
        """This method is used to show RBI bank services"""
        print("\nATMs Services, Debit cards, Online banking, Mobile Banking, Home banking")

    def show_loan(self):
        """This method is used to show RBI bank loans"""
        print("\nPersonal loan, Education loan, farming loan, business loan")

    def show_payment_ways(self):
        """This method is used to show RBI bank payment ways"""
        print("\nBankWise payment, Online Banking, Mobile Banking, ATM")


rbi_interest = RBI()
print(rbi_interest.simple_interest())
print(rbi_interest.compound_interest())
rbi_interest.verify_pin_number()
rbi_interest.show_services()
rbi_interest.show_loan()
rbi_interest.show_payment_ways()
