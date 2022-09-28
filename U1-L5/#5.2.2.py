# 5.2.2 编写一个函数，功能是计算学生的平均分
# 用户先输入正整数 n，告知学生数量
# 用户输入每个学生的成绩，如果成绩在 0-100 以外，提示用户输入错误
# 学生成绩录入完毕后，计算平均分，将平均分作为返回值
# 在函数外部调用函数，打印出学生的平均分
def mean_score(b):
    i = 0
    sum = 0
    while i < b:
        a = int(input("请输入学生的成绩："))
        if a < 0 or a > 100:
            print("分数有误，请重新输入")
            continue
        sum += a
        i += 1

    mean = sum / i
    return "录入完毕！平均分为 %d 分" % mean



print(mean_score(int(input("请输入学生数量："))))
