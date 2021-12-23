from inheritance.multiple_inheritance.collage import Collage_Student
from inheritance.multi_level_inheritance.bank_loan import FinalPayment


class Person(Collage_Student, FinalPayment):
    """Child Class.This class inherit the Collage_Student, FinalPayment classes."""
    def __init__(self, initial_amount, first_amount, final_amount):
        """This is a person class constructor."""
        FinalPayment.__init__(self, initial_amount, first_amount, final_amount)


person = Person(25000, 50000, 500000)
person.subject()
person.final_payment()
