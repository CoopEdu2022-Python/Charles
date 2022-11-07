# 定义一个函数，参数为一个由单位正整数组成的列表，用于表示一个数字
# 最高位数字存放在数组的首位，除了整数 0 之外，这个整数不会以零开头
def plus_one(digit):
    digit = str(digit)
    digit = int(digit.replace("[", "").replace(",", "").replace(" ", "").replace("]", ""))
    digit += 1

    return list(str(digit))


print(plus_one([1, 2, 3]))
