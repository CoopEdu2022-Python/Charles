class Admin:
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def enter_system(self):
        pass

    def exit_system(self):
        pass

    @staticmethod
    def create_stu_account(new_account):
        return "student | %s | 12345678" % new_account

    @staticmethod
    def check_stu_info(stu_id):   # 直接调文件
        pass

    @staticmethod
    def set_credit_rule(rule):
        return rule

    @staticmethod
    def create_classes(name, class_number, stu_max, teacher, credit, category, students: list):
        return "{} | {} | {} | {} | {} | {} | {} | {}".format(name, class_number, len(students), stu_max,
                                                              teacher, credit, category, students)

    @staticmethod
    def edit_course_info():   # 直接调文件修改

        pass

    @staticmethod
    def check_course_info(course_name):   # 直接调文件

        pass


class Operator:
    @staticmethod
    def select_course(student, course):
        student.selected_course.append(course)
        course.student.append(student)

    @staticmethod
    def drop_course(student, course):
        student.selected_course.remove(course)
        course.student.remove(student)

# 其实觉得并不需要中介类