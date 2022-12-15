class Student:
    def __init__(self, course, id, name):
        self.id = id
        self.name = name
        self.course = course

    def __del__(self):
        print("format has been deleted")

    def add_course(self):
        self.course.append("class code")

    def del_course(self):
        self.course.pop()


class Course:
    def __init__(self, id, name, students):
        self.id = id
        self.name = name
        self.students = students

    def __del__(self):
        print("This course has been deleted")

    def add_students(self):
        self.students.append("Students")

    def del_students(self):
        self.students.pop()


