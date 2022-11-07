# 5.2.5 处理矩阵
# 使用 for 循环，将下方的矩阵保存在一个二维列表中
# 定义 2 个元祖，一个保存行，一个保存列，元祖的每个元素是一个列表（一行或一列的所有数），打印这 2 个元祖
# 定义 2 个新的元祖，分别保存行、列的和，打印这 2 个元祖
'''
  1  2  3  4  5  6
  7  8  9 10 11 12
 13 14 15 16 17 18
 19 20 21 22 23 24
 25 26 27 28 29 30
 31 32 33 34 35 36
'''


Two_D_list_row = []
for row in range(0, 6):
    row_list = []
    Two_D_list_row.append(row_list)
    for num in range(1, 7):
        row_list.append(num + row * 6)

Two_D_list_colum = []
for i in range(6):
    temp = []
    Two_D_list_colum.append(temp)
    for j in range(6):
        temp.append(Two_D_list_row[j][i])

Two_D_tuple_row = tuple(Two_D_list_row)
Two_D_tuple_colum = tuple(Two_D_list_colum)
print(Two_D_tuple_row)
print(Two_D_tuple_colum)

Two_D_list_row_sum = []
for i in range(6):
    a = sum(Two_D_list_row[i])
    Two_D_list_row_sum.append(a)
Two_D_tuple_row_sum = tuple(Two_D_list_row_sum)
print(Two_D_tuple_row_sum)

Two_D_list_colum_sum = []
for i in range(6):
    a = sum(Two_D_list_colum[i])
    Two_D_list_colum_sum.append(a)
Two_D_tuple_colum_sum = tuple(Two_D_list_colum_sum)
print(Two_D_tuple_colum_sum)
