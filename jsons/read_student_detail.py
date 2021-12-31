import json
from constant.constant import Constant


class Student_detail:
    global data

    with open(Constant.FILE_PATH, "r") as students:
        data = json.load(students)

    def get_name(self):
        """This method is used to get student name"""
        student_name = []
        for name in data[Constant.FILE_NAME]:
            student_name.append(name["name"])
        print("First Year Students name -->", student_name)

    def get_student_count(self):
        """This method is used to get students count"""
        print("\nTotal first year students -->", len(data[Constant.FILE_NAME]))

    def get_student_name_with_age(self):
        """This method is used to get student name and age"""
        for student_name_with_age in data[Constant.FILE_NAME]:
            print(student_name_with_age["name"] + "'s age is " + str(student_name_with_age["age"]))

    def get_student_details(self):
        """This method is used to get student details"""
        student_details = []
        for student_detail in data[Constant.FILE_NAME]:
            name = student_detail["name"]
            id = student_detail["id"]
            age = student_detail["age"]
            year = student_detail["year"]
            student_details.append(id + " id " + str(year) + "'st year student name is " + name + " and age is " + str(age))
        for detail_of_student in student_details:
            print(detail_of_student)


student = Student_detail()
student.get_name()
student.get_student_count()
student.get_student_name_with_age()
student.get_student_details()
