class User:
    def enter_system(self):
        pass

    def exit_system(self):
        pass


class Teacher(User):
    num = 0

    def __init__(self, name, course):
        self.name = name
        self.courseTeaching = course
        Teacher.num += 1

    @staticmethod
    def check_stu(students):   # 直接调文件
        pass


class Student(User):
    num = 0

    def __init__(self, name: str, gender: str, age: int, grade: int, account_number: int, password: str, selected_course: list):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.account_number = account_number
        self.password = password
        self.selected_course = selected_course
        Student.num += 1

    def select_course(self, course):
        self.selected_course.append(course)
        course.student.append(self)

    @staticmethod
    def check_course_info(course):  # 直接调文件
        pass

    def drop_course(self, course):
        self.selected_course.remove(course)
        course.student.remove(self)

    def iterate_password(self):
        pass
