from constant.constant import Constant
from jsons.duplicate_data import DuplicateData
from jsons.new_student_entry import NewStudent
from jsons.read_student_detail import Student_detail


class Student(NewStudent, Student_detail, DuplicateData):
    """This class is extended from NewStudent, Student_detail, DuplicateData classes"""
    pass


students = Student()
students.enter_new_student(Constant.NEW_STUDENT)
students.get_student_details()
students.get_duplicate_data()
