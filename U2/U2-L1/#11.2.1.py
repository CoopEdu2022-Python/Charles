class Student:
    def __init__(self, name=None, student_id='0'):
        self.name = name
        self.student_id = student_id
        self.score = 70
        print('{} enrolled! (id: {})'.format(name, student_id))

    def __del__(self):
        print('{} dropped out! (id: {})'.format(self.name, self.student_id))

    def __str__(self):
        info = 'name: {}\nid: {} '.format(self.name, self.student_id)
        return info

    def study(self):
        self.score += 1
        self.mood = 'good'

    def play(self, days=1):
        if self.score < 70 or self.score > 90:
            self.mood = 'perfect'
        else:
            self.mood = 'bad'
        self.score -= (days - 1)

    def self_introduction(self):
        print(self)


"""11.2.1"""
student_1 = Student()  # 打印一遍init
print(student_1.name, student_1.student_id)  # 打印 student_1 这个对象的 name 和 id
"""11.2.2"""
student_1 = Student('7')  # 打印一遍传入 "7" 这个参数的 init
print(student_1)  # 打印一遍 str 里面的东西
"""11.2.3"""
student_1 = Student()  # 打印一遍init
student_1.self_introduction()  # 里面的 self 就是 student_1, 所以有打印了一遍 init
"""11.2.4"""
student_1 = Student('xxs', '9')  # 打印一遍传过这两个参数的 init

for day in range(30):  # 0 ~ 30 循环 30 次所以是 + 30，最后打印出来这个学生的成绩是 100 分，mood 是 good
    student_1.study()

print(student_1.score, student_1.mood)

for day in range(31, 0, -1):  # 31 到 0 还是循环30次，但是因为里面的 day 没有传进去，所以 day 和 - 1 抵消了。
    student_1.play()

print(student_1.score, student_1.mood)  # 所以 score 不会减少，反而 mood 变成 perfect 了

if student_1.score < 70:  # 所以这一行就不会执行到了
    del student_1
"""11.2.5"""
student_1 = Student()  # 打印一遍init
info = str(student_1)  # 这个 info 只是定义了一个变量。
print(student_1.info)  # 这个 .info 应该是内置方法，但是类里面没有定义这个方法，只是有一个变量，所以三者均不互通，所以这里会报错
"""11.2.6"""

student_1 = Student()  # 打印一遍init
student_2 = Student()  # 打印一遍init

student_1.study()  # 因为 student_1 study 了，所以多了一个 mood 的方法，这个方法是在 study 方法里面创建的。
len_1 = len(dir(student_1))  # dir 返回对象的所有属性 + 方法的列表
len_2 = len(dir(student_2))
print("---------")
print(len_1 - len_2)  # 所以最后 student_1 的方法要比 student_2 多一个，所以最后会 print 1
