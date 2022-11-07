# 6.1.5 定义一个函数，参数为 1 个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数，将所有数量保存在 1 个元祖返回
def count(a):
    a_alphabet = 0
    a_space = 0
    a_number = 0
    for i in range(0, len(a)):
        if a[i].isalpha():
            a_alphabet += 1
        elif a[i].isspace():
            a_space += 1
        elif a[i].isdigit():
            a_number += 1
    else_ = len(a) - a_alphabet - a_number - a_space

    return (a_alphabet, a_space, a_number, else_)


print(count(input("Enter something: ")))

# 我真的不懂为什么我这个不行