def enter_system(id_number: str, password: str):
    with open("../account & password", "r") as f:
        a = f.readlines()
        a.pop(0)
        for i, items in enumerate(a):
            a[i] = items.rstrip("\n")[-14:]
        v_password = ""
        for items in a:
            if items[:5] == id_number:
                v_password = items[8:]
                break
        if password == v_password:
            for items in a:
                if items[0] == id_number[0] == "a":
                    print("access granted")
                    return "a"
        else:
            return "access denied(you can try again if you want hhhh)"


def update_stu_info(student, id_number):
    with open("../Students/%s" % id_number, "w") as f:
        new_stu_info = "{} | {} | {} | {} | {} | {} | {} | {}" \
            .format(student.stu_id, student.password, student.name, student.gender,
                    student.age, student.grade, student.selected_course, student.credit_req)
        f.write(new_stu_info)


def update_course_info(course_name):
    with open("../Course/%s" % course_name, "w") as f:
        new_course_info = "{} | {} | {} | {} | {} | {} | {} | {}" \
            .format(course_name.class_name, course_name.class_number, course_name.current_stu,
                    course_name.stu_max, course_name.teacher, course_name.class_credit,
                    course_name.class_type, course_name.class_credit)
        f.write(new_course_info)

# def iterate_password():
#     global __account_number
#     old_password = input("Enter your original password: ")
#     with open("../account & password", "r") as f:
#         a = f.readlines()
#         a.pop(0)
#         for i, items in enumerate(a):
#             a[i] = items.rstrip("\n")[-14:]
#         v_password = ""
#         for items in a:
#             if items[:4] == __account_number:
#                 v_password = items[6:]
#                 break


# login
print("Hi welcome to the course selection system, you may enter your id and your password to log in")
while 1:
    id_number = input("Please enter your personal id to log in: ")
    password = input("Please enter your password: ")
    temp = enter_system(id_number, password)
    if temp == "a" or "t" or "s":
        break
    else:
        print(temp)


if temp == "a":
    from Controller import Admin
    admin = Admin(id_number, password)
    while 1:
        print("here's what you can do: \n"
              "1: create_stu_account\n"
              "2: create_teacher_account\n"
              "3: check_stu_info\n"
              "4: set_credit_rule\n"
              "5: create_classes\n"
              "6: edit_course_info\n"
              "7: check_course_info\n"
              "-1: if you want to exit the system just press -1")
        action = int(input("Enter a number for what you want to do: "))

        if action == 1:
            stu_id = input("input stu id with format(s_xxx): ")
            admin.create_stu_account(stu_id)
        if action == 2:
            teacher_id = input("input teacher id with format(t_xxx): ")
            admin.create_stu_account(teacher_id)
        if action == 3:
            stu_id = input("input stu id with format(s_xxx): ")
            admin.check_stu_info(stu_id)
        if action == 4:
            rule = input("Set the total credit that stu needs to achieve in their course selection: ")
            admin.set_credit_rule(rule)
        if action == 5:
            name = input("enter the course name: ")
            class_number = input("enter class code/number: ")
            stu_max = input("enter the maximum students in this course: ")
            teacher = input("enter who teach this course: ")
            credit = input("enter how much credit does this course have: ")
            category = input("enter 'selective' or 'required' for the category of this course")
            students = input("enter all the students that needs to be add before the course selection(separate with ', '):").split(", ")
            admin.create_classes(name, class_number, stu_max, teacher, credit, category, students)
        if action == 6:
            course_name = input("enter the course name that you want edit: ")
            admin.edit_course_info(course_name)
        if action == 7:
            course_name = input("enter the course name: ")
            admin.check_course_info(course_name)
        if action == -1:
            break
if temp == "t":
    from User import Teacher
    with open("../Teacher", "r") as f:
        a = f.readlines()
        for i, items in enumerate(a):
            a[i] = items.rstrip("\n")
    # teacher = Teacher()
    # not important, I don't want you to do anything
if temp == "s":
    from User import Student
    from Course import Course

    with open("../Students/%s" % id_number, "r") as f:
        a = f.readline()
        c = a.split(" | ")
        for items in c:
            if items[0] == id_number:
                user = items
    with open("../Students/format", "r") as f:
        b = f.read()
        print(b, a, sep="\n")
    student = Student(user[2], user[0], user[3], user[4], user[5], user[1], user[6][1:-1].split(", "), user[7])

    while 1:
        print("1: select course\n"
              "2: check specific course information\n"
              "3: drop course"
              "-1: if you want to exit the system just press -1\n")
        action = int(input("Enter a number for what you want to do: "))
        # 选课
        if action == 1:
            # 显示所有课程
            with open("../Course/all course") as f:
                a = f.readlines()
                for i, items in enumerate(a):
                    a[i] = items.rstrip("\n").split(" | ")
                for items in a:
                    for i in items:
                        print(i.ljust(15), end="\t")
                    print("\n")
            # 输入要选择的课程
            course_name = input("enter the course name that you want to add: ")
            # 选课操作
            with open("../Course/%s" % course_name, "r") as f:
                a = f.readline()
                c_info = a.split(" | ")
                course_name = Course(c_info[0], c_info[1], c_info[2], c_info[3], c_info[4], c_info[5], c_info[6])

            new_c_r = student.select_course(course_name)
            # 更新学生信息
            update_stu_info(student, id_number)
            # 更新课程信息
            update_course_info(course_name)
        # 查看课程信息
        if action == 2:
            course_name = input("Which course you want to check in detailed")
            student.check_course_info(course_name)
        # 退课
        if action == 3:
            course_name = input("enter the course name that you want to drop: ")

            with open("../Course/%s" % course_name, "r") as f:
                a = f.readline()
                c_info = a.split(" | ")
                course_name = Course(c_info[0], c_info[1], c_info[2], c_info[3], c_info[4], c_info[5], c_info[6])

            new_c_r = student.drop_course(course_name)

            # 更新学生信息
            update_stu_info(student, id_number)
            # 更新课程信息
            update_course_info(course_name)



