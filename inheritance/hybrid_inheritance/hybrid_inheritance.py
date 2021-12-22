from inheritance.multiple_inheritance.collage import Student
from inheritance.multi_level_inheritance.multilevel_inheritance import FinalPayment


class Person(Student, FinalPayment):
    def __init__(self, initial_amount, first_amount, final_amount):
        FinalPayment.__init__(self, initial_amount, first_amount, final_amount)


person = Person(25000, 50000, 500000)
person.subject()
person.final_payment()
