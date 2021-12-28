from abc import ABC, abstractmethod
from bank.values.bank import Bank
from bank.values.customer import Customer


class ATM(ABC):
    """This is an abstract class. It extended from a predefined abstract class(ABC).
     This class maintain ATM transaction method"""

    def verify_user_name(self):
        """This method used to verify customer name"""
        if Bank.customer_name == Customer.name:
            print("Hello", Customer.name)
        else:
            print("Name declined")

    def verify_passbook_number(self):
        """This method used to verify customer account number"""
        if Bank.passbook_number == Customer.account_number:
            print("Your account number is", Customer.account_number)
        else:
            print("Account number declined")

    @abstractmethod
    def verify_pin_number(self):
        """This method used to verify pin number"""
        pass
