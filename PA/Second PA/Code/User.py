class Teacher:
    num = 0

    def __init__(self, name, course):
        self.name = name
        self.course_teaching = course
        Teacher.num += 1

    @staticmethod
    def check_stu(stu_id):   # 直接调文件
        with open("../Students/format", "r") as f:
            for line in f.readlines():
                a = line.split(" | ")
                if a[0] == stu_id:
                    return a[2::]


class Student:
    num = 0

    def __init__(self, name: str, stu_id: str, gender: str, age: str, grade: str, password: str, selected_course: list, credit_req: str):
        self.name = name
        self.stu_id = stu_id
        self.gender = gender
        self.age = age
        self.grade = grade
        self.password = password
        self.selected_course = selected_course
        self.credit_req = credit_req
        Student.num += 1

    def select_course(self, course):
        if course.current_stu == course.stu_max:
            return "This course is full, try another course."
        self.selected_course.append(course)
        course.student.append("%s, %s | " % (self.name, self.stu_id))
        with open("../Course/Credit rule", "r") as f:
            a = f.read()
            c_ = int(self.credit_req[:2])
            c_ += int(course.credit)
            new_c_r = str(c_) + "/" + a
            print("Done")
            return new_c_r


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
        with open("../Course/Credit rule", "r") as f:
            a = f.read()
            c_ = int(self.credit_req[:2])
            c_ -= int(course.credit)
            new_c_r = str(c_) + "/" + a
            print("Done")
            return new_c_r
