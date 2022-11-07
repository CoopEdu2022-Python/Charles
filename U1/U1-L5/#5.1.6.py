# 5.1.6 定义一个函数，将列表每隔一个元素就增加一个 0，将新列表作为返回值

def expand(list):
    i = 0
    for items in list:
        if i % 2 != 0:
            list.insert(i, "0")
        i += 1
    return list


b = [1, "a", 2, "b", 3, "c", 4, True, 5]
expand(b)
print(b)
