# 5.1.3 依次删除下方列表中所有的 3，并在删除后打印每个 3 的索引，最后打印最终的列表
list_num = [1, 3, 4, 3, 7, 3, 9, 8, 6, 3]
for i in range(0, len(list_num)):
    if list_num[i] == 3 and i < 9:
        print(i, end=" ")
    if list_num[i] == 3 and i == 9:
        print(i)
print(list_num)



