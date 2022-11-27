# 19.2.3  计算班级平均成绩
# 定义函数 input_score
# - 允许用户输入 1 次成绩（0-100）、最多两位小数（可以是整数）
# - 如果输入的数字不符合要求，抛出自定义异常 ScoreError
# 在主程序中，完成 30 名学生成绩的录入，并捕获 2 类异常
# 1. 输入的不是数字
# 2. 输入的数字不符合要求
class ScoreError(ValueError):
    pass


def input_score(a):
    if a.isnumeric():
        if 100 > int(a) > 0:
            return a
        raise ScoreError("invalid score")
    raise ScoreError("not number")


score = list()
i = 0
while i < 30:
    try:
        a = input("请输入学生成绩：")
        input_score(a)
    except Exception as result:
        print("error type: %s" % result)
    else:
        score.append(a)
        i += 1
