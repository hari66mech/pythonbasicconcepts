class Student:
    """Parent Class"""
    def __init__(self, name):
        """This is a Student class constructor."""
        self.name = name

    def student(self):
        """This method is used to print the student name"""
        print("Student name is", self.name)


class Engineering(Student):
    """Child Class.This class inherit the Student class"""
    def __init__(self, name, id):
        """This is a Engineering class constructor."""
        Student.__init__(self, name)
        self.id = id

    def engineer(self):
        """This method is used to print the engineering student detail"""
        print("Student name is", self.name, "and ID is", self.id)


class B_Sc(Student):
    """Child Class.This class inherit the Student class"""
    def __init__(self, name, id, age):
        """This is a B_Sc class constructor."""
        Student.__init__(self, name)
        self.id = id
        self.age = age

    def b_sc(self):
        """This method is used to print the b_sc student detail"""
        print("Student name is", self.name, ", age is", self.age, "and ID is", self.id)


engineering = Engineering("raj", "001")
engineering.student()
engineering.engineer()
bsc = B_Sc("ram", "bsc001", 20)
bsc.student()
bsc.b_sc()
