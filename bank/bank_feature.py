"""Python Polymorphism is not allowing method overloading as directly."""


class BankFeatures:
    """This class is used to show available services and available loans"""
    def show_available_feature(self, atm=None, net_banking=None, text_alert=None, locker=None):
        """This class is used to show available bank services"""
        print("Available services -->", end=" ")
        if atm is not None:
            print("ATM", end=', ')
        if net_banking is not None:
            print("Net-Banking", end=', ')
        if text_alert is not None:
            print("Text message", end=', ')
        if locker is not None:
            print("Locker")

    def show_available_loan(self, gold=None, education=None, business=None, farmer=None):
        """This class is used to show available bank loans"""
        print("Available loans -->", end=" ")
        if gold is not None:
            print("Gold Loan", end=', ')
        if education is not None:
            print("Education Loan", end=', ')
        if business is not None:
            print("Business Loan", end=', ')
        if farmer is not None:
            print("Farming Loan")


bank_feature = BankFeatures()
bank_feature.show_available_feature(atm="Yes", net_banking="Yes", locker="Yes")
bank_feature.show_available_loan(gold="Yes", business="Yes", farmer="Yes")
