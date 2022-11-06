def permutation(array):
    s = []
    if len(array) == 1:
        return [array]
    else:
        for i in range(len(array)):
            array[i], array[0] = array[0], array[i]   # 每次交换⼀个元素
            temp = permutation(array[1:])   # 递归
            for l in temp:      # 如果只是打印不⽤保存，那么for循环可以去掉
                s.append([array[0]]+l)
            array[i], array[0] = array[0], array[i]   # 恢复原始序列
    return s


test = [i for i in range(5)]
print(len(permutation(test)))
print(permutation(test))
"""
想够1个小时了，不继续纠结了，网上找了一个，看过之后还是不太懂，就这样了，下一题。
"""
