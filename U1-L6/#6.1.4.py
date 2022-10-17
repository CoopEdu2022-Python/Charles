# 6.1.4 定义一个函数，参数为 2 个字符串，从第 1 个字符串中删除第 2 个字符串中所有的字符，返回新的字符串
# 例如，参数为 'They are students.' 和 'aeiou'，返回 'Thy r stdnts.'
def strip(a, b):
    a, b = str(a), str(b)
    for i in b:
        a = a.replace(i, "")
    return a


print(strip('They are students.', 'aeiou'))


# translate 和 maketrans 的用法
def del_str(str_original, str_to_remove):
    return str_original.translate(str.maketrans("", "", str_to_remove))


print(del_str("They are students.", "aeiou"))