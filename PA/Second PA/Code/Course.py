class Course:
    def __init__(self, name, class_number, stu_max, teacher, credit, category, students):
        self.class_name = name
        self.class_number = class_number
        self.current_stu = len(students)
        self.stu_max = stu_max
        self.teacher = teacher
        self.class_credit = credit
        self.class_type = category
        self.students = students
