class Course:
    def __init__(self, teacher="a teacher", student=15, class_code=None):
        self.time = 45
        self.course_teacher = teacher
        self.student = student
        self.class_code = class_code
        print("This class is teaching by {}, with {} students, "
              "and the class code is {}, welcome to our class!".format(teacher, student, class_code))

    def __del__(self):
        print("This course was canceled")

    def enroll(self):
        self.student += 1

    def course_introduction(self):
        print(self)
