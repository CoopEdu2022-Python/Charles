# 2.1.5 学生输入一个成绩，对不同的成绩进行评价（标准自定）
# 这个标准是学校2021-2022handbook里面的，所以其实可以直接用到生活中hhhhhh
GPA = float(input("Please enter your course score: "))
if GPA >= 97:
    print("you've got an A+, and your GPA is 4.0, well done!!!")
elif 93 <= GPA < 97:
    print("you've got an A, and your GPA is 4.0, well done!!!")
elif 90 <= GPA < 93:
    print("you've got an A-, and your GPA is 3.7, not bad~")
elif 85 <= GPA < 90:
    print("you've got an B+, and your GPA is 3.3, not bad~")
elif 80 <= GPA < 85:
    print("you've got an B, and your GPA is 3.0, you need to work harder!")
elif 77 <= GPA < 80:
    print("you've got an B-, and your GPA is 2.7, you need to work harder!")
elif 73 <= GPA < 77:
    print("you've got an C+, and your GPA is 2.3, you really should keep up\n if you don't want to fail the course!")
elif 70 <= GPA < 73:
    print("you've got an C, and your GPA is 2.0, you really should keep up\n if you don't want to fail the course!")
elif 67 <= GPA < 70:
    print("you've got an C-, and your GPA is 1.7, you really should keep up\n if you don't want to fail the course!")
elif GPA < 67:
    print("I'm sorry, you have failed this course.(F)")
