"""Data hiding"""


class Collage:
    def __init__(self):
        """This is a constructor. use to initialising the objects"""
        self.student_count = 1140
        self.staffs_count = 57
        self.available_class_rooms = 27
        self.__account_details = 5000000
        self.__average_salary_detail = 35000

    def accountant(self):
        """This method is used to print the salary(private) and return the account details(private)"""
        print(self.__salary())
        return "This is the hidden detail. not access others. account detail", self.__account_details

    def __salary(self):
        """This is a private method.It is used to return the salary"""
        return "This is the hidden detail. only access the accountant. salary detail", self.__average_salary_detail

    def print_collage_student_detail(self):
        """This method is used to print the student details(public)"""
        print("Student count", self.student_count)
        print("Staffs count", self.staffs_count)
        print("Class rooms count", self.available_class_rooms)


collage = Collage()
collage.print_collage_student_detail()
print(collage.accountant())
