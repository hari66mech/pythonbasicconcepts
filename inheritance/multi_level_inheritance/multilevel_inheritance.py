class InitialPayment:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount

    def initial_payment(self):
        print("Initial Payment is", self.initial_amount)


class FirstPayment(InitialPayment):
    def __init__(self, initial_amount, first_amount):
        InitialPayment.__init__(self, initial_amount)
        self.first_amount = first_amount

    def first_payment(self):
        print("Initial Payment is", self.initial_amount, "First Payment is", self.first_amount)


class FinalPayment(FirstPayment):
    def __init__(self, initial_amount, first_amount, final_amount):
        FirstPayment.__init__(self, initial_amount, first_amount)
        self.final_amount = final_amount

    def final_payment(self):
        print("Initial Payment is", self.initial_amount, "First Payment is", self.first_amount, "Final Payment is", self.final_amount)


payment = FinalPayment(20000, 45000, 300000)
payment.initial_payment()
payment.first_payment()
payment.final_payment()
