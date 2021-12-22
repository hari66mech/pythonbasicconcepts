class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def employee_name(self):
        print(self.id, "number employee name is", self.name)

    def employee_salary(self):
        print(self.id, "initial salary is 20000")


class Salary(Employee):
    def __init__(self, id, name, salary):
        Employee.__init__(self, id, name)
        self.salary = salary

    def employee_salary(self):
        super().employee_salary()
        print(self.id, "number employee salary is", self.salary)


employee = Salary("001", "Raj", 45000)
employee.employee_name()
employee.employee_salary()
