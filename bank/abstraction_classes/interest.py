from abc import ABC, abstractmethod


class Interest(ABC):
    """This is an abstract class. It is extended from a predefined abstract class(ABC).
     This class contains two types of interest"""

    @abstractmethod
    def simple_interest(self):
        """This method is used to calculate simple interest"""
        pass

    @abstractmethod
    def compound_interest(self):
        """This method is used to calculate compound interest"""
        pass
