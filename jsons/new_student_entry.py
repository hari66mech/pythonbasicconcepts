import json
from constant.constant import Constant


class NewStudent:
    def enter_new_student(self, new_data, filename=Constant.FILE_PATH):
        """This method is used to enter new student details"""
        with open(filename, 'r+') as file:
            student_data = json.load(file)
            student_data[Constant.FILE_NAME].append(new_data)
            file.seek(0)
            json.dump(student_data, file, indent=4)
