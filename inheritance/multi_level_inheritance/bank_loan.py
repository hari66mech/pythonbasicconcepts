class InitialPayment:
    """Parent Class"""
    def __init__(self, initial_amount):
        """This is a InitialPayment class constructor."""
        self.initial_amount = initial_amount

    def initial_payment(self):
        """This method is used to print the customer initial payment"""
        print("Initial Payment is", self.initial_amount)


class FirstPayment(InitialPayment):
    """Child Class.This class inherit the InitialPayment class"""
    def __init__(self, initial_amount, first_amount):
        """This is a FirstPayment class constructor."""
        InitialPayment.__init__(self, initial_amount)
        self.first_amount = first_amount

    def first_payment(self):
        """This method is used to print the customer initial payment and first payment"""
        print("Initial Payment is", self.initial_amount, "First Payment is", self.first_amount)


class FinalPayment(FirstPayment):
    """Child Class.This class inherit the FirstPayment class"""
    def __init__(self, initial_amount, first_amount, final_amount):
        """This is a FinalPayment class constructor."""
        FirstPayment.__init__(self, initial_amount, first_amount)
        self.final_amount = final_amount

    def final_payment(self):
        """This method is used to print the customer initial payment, first payment and final payment."""
        print("Initial Payment is", self.initial_amount, "First Payment is", self.first_amount, "Final Payment is", self.final_amount)


payment = FinalPayment(20000, 45000, 300000)
payment.initial_payment()
payment.first_payment()
payment.final_payment()
