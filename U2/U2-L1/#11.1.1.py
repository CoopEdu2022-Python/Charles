class Student():
    def __init__(self, name=str(), id=str()):
        self.name = name
        self.id = id
        self.courses = list()

    def __del__(self):
        print("已删除: {} (id:{})".format(self.name, self.id))

    def __str__(self):
        return "name: {}\nid: {}".format(self.name, self.id)

    def __len__(self):
        return len(self.courses)

    def get_courses(self):
        return self.courses


student_1 = Student("Charles", "20011041")
print(student_1)
student_1.courses = ["Math", "English", "Python", "Chinese", "Football"]
print(len(student_1))
del student_1

