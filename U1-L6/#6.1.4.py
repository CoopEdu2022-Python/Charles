# 6.1.4 定义一个函数，参数为 2 个字符串，从第 1 个字符串中删除第 2 个字符串中所有的字符，返回新的字符串
# 例如，参数为 'They are students.' 和 'aeiou'，返回 'Thy r stdnts.'
def strip(a, b):
    a, b = str(a), str(b)
    b = " ".join(b)
    for i in b.split():
        a = a.replace(i, "")
    return a


print(strip('They are students.', 'aeiou'))
