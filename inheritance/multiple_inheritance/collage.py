class Engineering:
    def engineering_subject(self):
        print("Mechatronics Engineering")


class Bachelor_of_Technology:
    def bachelor_of_technology_subject(self):
        print("B.tech Mechatronics")


class Student(Engineering, Bachelor_of_Technology):
    def subject(self):
        print("Basic Subject")


student = Student()
student.subject()
student.engineering_subject()
student.bachelor_of_technology_subject()
