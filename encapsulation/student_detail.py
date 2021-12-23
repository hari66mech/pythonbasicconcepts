class ClassRoom:
    """This class use to manipulate the student detail"""
    def __init__(self):
        """This is a constructor. use to initialising the objects"""
        self.student_name = "raj"
        self.__studentID = "mech001"
        self._age = 25

    def print_student_details(self):
        """This method is use to print the student details(public, private, protected)"""
        print("Student Name:", self.student_name)
        print("StudentID:", self.__studentID)
        print("Student age:", self._age)


classRoom = ClassRoom()
print(classRoom.student_name)
print(classRoom._age)
classRoom.print_student_details()
"""Name Mangling(access the private variable from outside the class)"""
print(classRoom._ClassRoom__studentID)
