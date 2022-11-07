# 6.1.2 定义一个函数，参数为 1 个字符串，判断它是否为 '回文数'
# 如果一个数字左右对称，就是 '回文数'，如 123454321, 1221
def is_symmetry_number(a):
    a = str(a)
    if a == a[::-1]:
        return True
    return False


print(is_symmetry_number("12321"))
