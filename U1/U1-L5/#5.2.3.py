# 5.2.3 将 5.2.2 的函数复制过来，将返回值修改为一个元祖，这个元祖保存了所有学生的成绩
# 在函数外部调用函数，获取所有学生的成绩，打印出所有学生的成绩
# 在函数外部计算所有学生的平均分，打印一条消息显示平均分
# 你发现一个学生的成绩有错误，修改这个成绩，并重新计算平均分，打印
def score(number_of_students):
    i = 0
    sum = 0
    score_list = []
    while i < number_of_students:
        a = int(input("请输入学生的成绩："))
        score_list.append(a)
        if a < 0 or a > 100:
            print("分数有误，请重新输入")
            score_list.pop()
            continue
        sum += a
        i += 1

    score_tuple = tuple(score_list)
    return score_tuple


a = score(int(input("请输入学生数量：")))
print(a)


def mean(a):
    total = 0
    for i in range(0, len(a)):
        total += a[i]
    mean = total / len(a)
    return mean


print(mean(a))
NewScoreList = list(a)
NewScoreList[1] = 55
print(mean(NewScoreList))
