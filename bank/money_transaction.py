from values.payment_option import TransactionWay


"""Duck typing(Dynamic typing)."""


class BankWay:
    """This class is used to monitor the bank wise transaction"""
    def excuted_way(self):
        print("Bank wise transaction")


class ATM:
    """This class is used to monitor the ATM wise transaction"""
    def excuted_way(self):
        print("ATM wise transaction")


class OnlinePayment:
    """This class is used to monitor the online transaction"""
    def excuted_way(self):
        print("Online payment transaction")


class MoneyTransaction:
    """This class is used to monitor the money transaction"""
    def transaction(self, transaction_type):
        """This method is used to show transaction type"""
        transaction_type.excuted_way()

    def show_money_status(self):
        """This method is used to show money status"""
        initial_payment = TransactionWay.initial_amount
        transaction_amount = TransactionWay.transaction_amount
        current_status = initial_payment + transaction_amount
        print("Initial Payment is RS.", initial_payment)
        print("Transaction Payment is RS.", transaction_amount)
        print("Current Payment is RS.", current_status)


payment_way = ""
if TransactionWay.transactionWay == "bank_wise":
    payment_way = BankWay()
elif TransactionWay.transactionWay == "atm":
    payment_way = ATM()
elif TransactionWay.transactionWay == "online_payment":
    payment_way = OnlinePayment()
else:
    payment_way = BankWay()

money_transaction = MoneyTransaction()
money_transaction.transaction(payment_way)
money_transaction.show_money_status()
