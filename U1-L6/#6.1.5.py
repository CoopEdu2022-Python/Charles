# 6.1.5 定义一个函数，参数为 1 个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数，将所有数量保存在 1 个元祖返回
def count(a):
    a = ",".join(a)
    a = a.split(",")
    alphabet = 0
    space = 0
    number = 0
    else_ = 0
    for i in range(0, len(a)):
        if a[i].isalpha():
            alphabet += 1
        elif a[i].isspace():
            space += 1
        elif a[i].isdigit():
            number += 1
        else:
            else_ += 1
    return (alphabet, space, number, else_)


print(count(input("Enter something: ")))

# 我真的不懂为什么我这个不行