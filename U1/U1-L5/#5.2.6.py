# 5.2.6 小明在黑板上写了一个整数数列，先将数列由小到大排好，每次擦去其中的第 1 个和第 2 个数。
# 假设擦去数的值分别为 a 和 b，再在数列中添加一个数 a * b + 1 并保持数列有序，如此下去，直至黑板上只剩下一个数，打印出这个数

int_list = [13, 27, 49, 58, 67]
while len(int_list) > 1:
    a = int_list[0] * int_list[1] + 1
    int_list.pop(0)
    int_list.pop(0)
    int_list.append(a)
    int_list.sort()
print(int_list)
