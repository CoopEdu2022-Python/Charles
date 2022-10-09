# 5.3.6 编写一个函数 compare_dict(dict1, dict2)，判断两个字典中存在多少个完全相同的键值对，
# 将重复键值对的数量和重复的键值对保存在一个元祖中，将这个元祖作为返回值
def compare_dict(dict1, dict2):
    same_item_list = []
    i = 0
    for item1 in dict1.item():
        for item2 in dict2.item():
            if item1 == item2:
                i += 1
                if item2 not in same_item_list:
                    same_item_list.append(item2)
                    same_item_list.append(i)
                same_item_list[i] = i
    same_item_tuple = tuple(same_item_list)
    return same_item_tuple
# 我这段代码有一个问题可能没办法解决的就是两个字典如果不一样长该怎么办，这个我没太想清楚
