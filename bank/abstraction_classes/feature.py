from abc import ABC, abstractmethod


class Features(ABC):
    """This is an abstract class. It extended from a predefined abstract class(ABC).
     This class maintain bank features"""

    @abstractmethod
    def show_services(self):
        """This method is used to show bank services"""
        pass

    @abstractmethod
    def show_payment_ways(self):
        """This method is used to show bank payment ways"""
        pass

    @abstractmethod
    def show_loan(self):
        """This method is used to show bank loans"""
        pass
