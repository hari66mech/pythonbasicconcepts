"""Flexibility"""


class Employee:
    """Inside this class restricted the read and write access separately"""
    def __init__(self):
        """This is a constructor. use to initialising the objects"""
        self.name = "raj"
        self.__id = "emp001"
        self._salary = 50000

    def get__id(self):
        """This method is use to get(read) the employee id(private)"""
        print(self.__id)

    def set__id(self, new_id):
        """This method is use to set(write) the employee id(private)"""
        self.__id = new_id


employee = Employee()
employee.get__id()
employee.set__id("emp000")
employee.get__id()
