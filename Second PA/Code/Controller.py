class Admin:
    def __init__(self, id_number, password):
        self.id = id_number
        self.password = password

    @staticmethod
    # 创建新学生账号，文件末尾写入新信息
    def create_stu_account(new_id_number):
        with open("../account & password", "a") as f:
            f.write("student | s_%s | 12345678" % new_id_number)

    @staticmethod
    # 创建新教师账号，文件末尾写入新信息
    def create_teacher_account(new_id_number):
        with open("../account & password", "a") as f:
            f.write("teacher | t_%s | 88888888" % new_id_number)

    @staticmethod
    # 查看学生信息，直接调文件
    def check_stu_info(stu_id):
        with open("../Students/format", "r") as f:
            for line in f.readlines():
                a = line.split(" | ")
                if a[0] == stu_id:
                    return a[2::]

    @staticmethod
    # 这个ok了
    def set_credit_rule(rule):
        with open("../Course/Credit rule", "w") as f:
            f.write(rule)
        return "rules has been set"

    @staticmethod
    # 创建新课程
    def create_classes(name, class_number, stu_max, teacher, credit, category, students: list):
        with open("../Course", "w") as f:
            f.write("{} | {} | {} | {} | {} | {} | {} | {}"
                    .format(name, class_number, len(students), stu_max, teacher, credit, category, students))
        with open("./all course", "w") as f:
            f.write(name)

    @staticmethod
    # 修改课程信息，直接调文件修改，里面含有删改输入指令
    def edit_course_info(course_name):
        while 1:
            try:
                # 第一遍读取，把文件读进来在内存中修改
                with open("./Course/%s" % course_name, "r") as f_read1:
                    info = f_read1.read().split(" | ")
                    print("0_course: {} | 1_class_code: {} | 2_current_stu_num: {} | 3_max_capacity: {} | "
                          "4_teacher: {} | 5_credit: {} | 6_category: {} | 7_students: {} \n"
                          .format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]))
                    new_info_input = input("Enter the number for category you want to edit "  # 修改内容输入
                                           "and new information after the number.\n"
                                           "(divide number and information with one space ': ' "
                                           "and different categories with '; ' )\n"
                                           "You can enter now: ")
                    new_info_input = new_info_input.split("; ")
                    for items in new_info_input:
                        index = int(items.split(": ")[0])
                        new_info = items.split(": ")[1]
                        info[index] = new_info
                    info = " | ".join(info)
                # 写文件，将第一步内存中修改好的文件内容重新写入到这个文件中
                with open(course_name, "w") as f_write:
                    f_write.write(info)
                    print("File has been changed")
                # 第二遍读文件，验证是否已经修改
                with open(course_name, "r") as f_read2:
                    info = f_read2.read().split(" | ")
                    return "0_course: {} | 1_class_code: {} | 2_current_stu_num: {} | 3_max_capacity: {} | " \
                           "4_teacher: {} | 5_credit: {} | 6_category: {} | 7_students: {}"\
                        .format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
            except FileNotFoundError:
                print("Course name not found, maybe you want to add a new course or "
                      "you just miss input the course name, please try again.")
            except:
                print("You must have been wrong when you are entering the information or something"
                      "otherwise it won't be wrong, try again please")
        pass

    @staticmethod
    def check_course_info(course_name):  # 直接调文件
        while 1:
            try:
                with open(course_name, "r") as f:
                    info = f.readline().split(" | ")
                    return "course: {} | class_code: {} | current_stu_num: {} | max_capacity: {}" \
                           "teacher: {} | credit: {} | category: {} | students: {}" \
                        .format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
            except FileNotFoundError:
                print("wrong class name")


# class Operator:
#     @staticmethod
#     def select_course(student, course):
#         student.selected_course.append(course)
#         course.student.append(student)
#
#     @staticmethod
#     def drop_course(student, course):
#         student.selected_course.remove(course)
#         course.student.remove(student)
#
# # 其实觉得并不需要中介类
