class Teacher:
    num = 0

    def __init__(self, name, course):
        self.name = name
        self.course_teaching = course
        Teacher.num += 1

    @staticmethod
    def check_stu(stu_id):   # 直接调文件
        with open("../Student", "r") as f:
            for line in f.readlines():
                a = line.split(" | ")
                if a[0] == stu_id:
                    return a[2::]


class Student:
    num = 0

    def __init__(self, name: str, gender: str, age: str, grade: str, password: str, selected_course: list):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.password = password
        self.selected_course = selected_course
        Student.num += 1

    def select_course(self, course):
        self.selected_course.append(course)
        course.student.append(self)

    @staticmethod
    # 直接调文件
    def check_course_info(course_name):
        with open("../Course/Python", "r") as f:
            for line in f.readlines():
                a = line.split(" | ")
                if a[0] == course_name:
                    return a

    def drop_course(self, course):
        self.selected_course.remove(course)
        course.student.remove(self)
