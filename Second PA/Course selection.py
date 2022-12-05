class Manager:
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def enter_system(self):
        pass

    def exit_system(self):
        pass

    def create_stu_account(self):
        pass

    def check_stu_info(self):
        pass

    def set_credit_rule(self):
        pass

    def create_classes(self):
        pass

    def edit_class_info(self):
        pass

    def check_course_info(self):
        pass


class Class:
    def __init__(self, name, stu, stu_max, teacher, credit, period, time, location, category, *students):
        self.className = name
        self.stu = stu
        self.stu_max = stu_max
        self.teacher = teacher
        self.classCredit = credit
        self.classPeriod = period
        self.classDuration = time
        self.classRoom = location
        self.classType = category
        self.students = students


class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.courseTeaching = course

    def enter_system(self):
        pass

    def exit_system(self):
        pass

    def check_stu(self):
        pass


class Student:
    def __init__(self, name, gender, age, grade, account_number, password, *selected_course):
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.account_number = account_number
        self.password = password
        self.selected_course = selected_course

    def enter_system(self):
        pass

    def exit_system(self):
        pass

    def select_course(self):
        pass

    def check_course_info(self):
        pass

    def drop_course(self):
        pass

    def iterate_password(self):
        pass
