import json
from constant.constant import Constant


class DuplicateData:
    global data

    with open(Constant.FILE_PATH, "r") as students:
        data = json.load(students)

    def get_duplicate_data(self):
        """This method is used to get duplicate data"""
        for student_detail in range(0, len(data[Constant.FILE_NAME])):
            for another_student_detail in range(1, student_detail):
                if data[Constant.FILE_NAME][student_detail]["id"] == data[Constant.FILE_NAME][another_student_detail]["id"]:
                    print("Duplicate data -->", data[Constant.FILE_NAME][another_student_detail])


students = DuplicateData()
students.get_duplicate_data()
