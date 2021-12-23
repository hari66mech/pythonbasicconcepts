class Engineering:
    """Parent Class"""
    def engineering_subject(self):
        """This method is used to print engineering subject"""
        print("Mechatronics Engineering")


class Bachelor_of_Technology:
    """Parent Class"""
    def bachelor_of_technology_subject(self):
        """This method is used to print bachelor of technology subject"""
        print("B.tech Mechatronics")


class Collage_Student(Engineering, Bachelor_of_Technology):
    """Child Class. This class inherit the Engineering, Bachelor_of_Technology classes."""
    def subject(self):
        print("Basic Subject")


student = Collage_Student()
student.subject()
student.engineering_subject()
student.bachelor_of_technology_subject()
