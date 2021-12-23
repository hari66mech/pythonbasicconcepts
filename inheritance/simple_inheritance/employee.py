class Employee:
    """Parent Class"""
    def __init__(self, id, name):
        """This is a Employee class constructor."""
        self.id = id
        self.name = name

    def employee_name(self):
        """This method used to print the employee name according to the employee ID"""
        print(self.id, "number employee name is", self.name)

    def employee_salary(self):
        """This method used to print the employee basic salary"""
        print(self.id, "initial salary is 20000")


class Salary(Employee):
    """Child Class"""
    def __init__(self, id, name, salary):
        """This is a Salary class constructor."""
        Employee.__init__(self, id, name)
        self.salary = salary

    def employee_salary(self):
        """This method used to print the employee initial salary and current salary according to the employee ID."""
        super().employee_salary()
        print(self.id, "number employee salary is", self.salary)


employee = Salary("001", "Raj", 45000)
employee.employee_name()
employee.employee_salary()
