# 6.1.7 定义一个函数，参数为 1 个字符串和 1 个只包含字符串的列表，用字符串作为连接符，将列表的每个元素连接起来，返回连接后的字符串
# 例如，参数为 '123' 和 ['a', 'b', 'c']，返回 'a123b123c'
def link(s, l):
    i = ""
    for items in l:
        i += items
    return s.join(i)


# 更快的方法
def link1(sep, strs):
    return sep.join(strs)


print(link("123", ['a', 'b', 'c']))
print(link1("123", ['a', 'b', 'c']))
