class Student:
    def __init__(self, name):
        self.name = name

    def student(self):
        print("Student name is", self.name)


class Engineering(Student):
    def __init__(self, name, id):
        Student.__init__(self, name)
        self.id = id

    def engineer(self):
        print("Student name is", self.name, "and ID is", self.id)


class B_Sc(Student):
    def __init__(self, name, id, age):
        Student.__init__(self, name)
        self.id = id
        self.age = age

    def b_sc(self):
        print("Student name is", self.name, ", age is", self.age, "and ID is", self.id)


engineering = Engineering("raj", "001")
engineering.student()
engineering.engineer()

bsc = B_Sc("ram", "bsc001", 20)
bsc.student()
bsc.b_sc()
