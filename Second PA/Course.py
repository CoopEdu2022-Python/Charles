class Course:
    num = 0

    def __init__(self, name, class_number, stu_max, teacher, credit, category, students):
        self.className = name
        self.classNumber = class_number
        self.stu = len(students)
        self.stu_max = stu_max
        self.teacher = teacher
        self.classCredit = credit
        self.classType = category
        self.students = students
        Course.num += 1
