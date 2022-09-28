# 5.2.8 编写一个函数，功能是去除元祖中的重复项（默认都是数字类型的元素），升序排列后，返回新的元祖
# 比如 tuple_sample = (1, 1, 2, 3, 6, 5, 4, 1)，返回 (1, 2, 3, 4 ,5 ,6)
def del_repeat(a):
    a = list(a)
    a.sort()
    for item in a:
        i = a[0]
        if i == item:
            a.pop(0)
    a = tuple(a)
    return a


tuple_sample = (1, 1, 2, 3, 6, 5, 4, 1)
print(del_repeat(tuple_sample))
