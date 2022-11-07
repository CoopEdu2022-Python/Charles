name1 = "Rob"
name2 = "Tim"
name3 = "Roy"
# 上面这个东西可以一起放到下面这个 列表中
name_list = ["Rob", "Tim", "Roy"]
# 列表的编号是从0开始的
# 输出的时候直接像下面这样就可以了
print(name_list[0])  # 输出列表中的第一个东西

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

name_list = ["zhangsan", "Lisi","wangwu"]
# 1.取值和取索引
# list index out of range-列表索引超出范围
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置(知道内容找位置)
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("wangwu"))
""""""""""""""
# 2.修改
name_list[1] = "李四"  # 输入想要修改list中第几项，并且输入修改后的结果就改完了

name_list[3] = "你好"  # 列表指定的索引超出范围，程序会报错！
# 如果输入的项数超出了原列表的最高项，系统会报错（只能改原列表中的值，并不能通过这个方法添加新元素）
""""""""""""""
# 3.增加
name_list.append("你好")  # 这样会将“你好”添加到列表的末尾
name_list.insert(1, "再见")  # 这样会将“再见”插入到列表中编号为 1 的位置（第二个位置）
temp_list = ["Hi", "Hello", "How are you"]
name_list.extend(temp_list)  # 这样会将上面的temp_list中所有元素放入name_list的最后（顺序不会发生改变）
""""""""""""""
# 4.删除
name_list.remove("wangwu")  # remove可以将列表中指定的元素移除
name_list.pop()  # 未设定的情况下会默认将列表中最后一个元素移除
name_list.pop(3)  # 将列表中编号为 3 的元素删除（实际从左往右数第四个元素）
name_list.clear()  # 将列表中所有元素全部清空
"""
del 关键字本质上是用来将一个变量从内存中删除的
    del name_list[1]  # 实际效果和上面的一样，删除列表中指定编号位置的元素
但是删除之后都不能再使用这个变量了
所以推荐使用列表提供的方法进行删除操作
"""

print(name_list)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

name_list = ["张三", "李四", "王五", "王小二", "张三"]
# len（length 长度）函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)
# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了 %d 次" % count)
# 从列表中删除第一次出现的数据，如果数据不存在，系统就会报错
name_list.remove("张三")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

name_list  = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 升序
name_list.sort()  # 将列表中的元素按照字母的顺序由A到Z排列
num_list.sort()  # 将列表中的元素按照数字从小到大的顺序排列
# 降序
name_list.sort(reverse=True)  # 将列表中的元素按照字母的顺序由Z到A排列
num_list.sort(reverse=True)  # 将列表中的元素按照数字从大到小顺序排列
# 逆序（反转）
name_list.reverse()  # 将列表中的所有元素以相反方向重新排列
num_list.reverse()  # 效果同上


