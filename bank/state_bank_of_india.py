from bank.abstraction_classes.atm import ATM
from bank.abstraction_classes.feature import Features
from bank.abstraction_classes.interest import Interest
from bank.values.bank import Bank
from bank.values.customer import Customer


class SBI(Interest, ATM, Features):
    """This is a concrete class. This class is extended from Interest, ATM, Features classes"""
    def simple_interest(self):
        """"This method is used to calculate SBI simple interest"""
        interest = (Customer.deposit_amount * Customer.saving_year * Bank.SBI_interest) / 100
        total_amount = Customer.deposit_amount + interest
        print("\nThis is a SBI simple interest")
        return total_amount

    def compound_interest(self):
        """This method is used to calculate SBI compound interest"""
        final_amount = Customer.deposit_amount * (1 + (Bank.SBI_interest / 100)) ** Customer.saving_year
        print("\nThis is a SBI compound interest")
        return final_amount

    def verify_pin_number(self):
        """This method used to verify pin number"""
        if Bank.pin_number == Customer.pin_number:
            current_payment = Customer.initial_amount - Customer.withdrawal_amount
            print("\nwithdrawal payment is RS.", Customer.withdrawal_amount)
            print("Current payment is RS.", current_payment)
        else:
            print("Transaction declined")

    def show_services(self):
        """This method is used to show SBI bank services"""
        print("\nATMs Services, Debit cards, Online banking, Mobile Banking, Discounting of Bills of Exchange")

    def show_loan(self):
        """This method is used to show SBI bank loans"""
        print("\nPersonal loan, Education loan, Farming loan, Business loan, Gold loan")

    def show_payment_ways(self):
        """This method is used to show SBI bank payment ways"""
        print("\nBankWise payment, Online Banking, ATM")


sbi_interest = SBI()
print(sbi_interest.simple_interest())
print(sbi_interest.compound_interest())
sbi_interest.verify_pin_number()
sbi_interest.show_services()
sbi_interest.show_loan()
sbi_interest.show_payment_ways()
