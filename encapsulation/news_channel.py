"""Code Re-usability"""


class XYZ_Channel:
    """Parent Class"""
    def __news(self):
        """This is a private method"""
        self.news = "This is sensational news."
        return self.news

    def base_channel(self):
        """This method is use to call the __news(method)"""
        print(self.__news() + " Produced by base news channel")


class ABC_Channel(XYZ_Channel):
    """Child Class"""
    def __news(self):
        """This is a overrides method in XYZ_Channel class"""
        print("This is so-sensational news.")

    def news(self):
        """This method is use to call the base_channel(method) and __news(overrides method)"""
        self.base_channel()
        self.__news()
        print("Delivering by ABC channel")


class CBA_Channel(XYZ_Channel):
    """Child Class"""
    def news(self):
        """This method is use to call the base_channel(method)"""
        self.base_channel()
        print("Delivering by CBA channel")


abc_channel = ABC_Channel()
abc_channel.news()
cba_channel = CBA_Channel()
cba_channel.news()
