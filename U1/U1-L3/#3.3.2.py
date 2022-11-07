# 3.3.2 用户输入高度（行数），按照下方格式打印 1 个菱形
a = int(input("How many rows you want to print: "))
d = ((a // 2) + 1) - a  # 找到了规律（3，2，1，0，1，2，3），所以现在要把这个从小到大排，所以就有了绝对值
for i in range(d, abs(d)+1):     # 所以现在要把这个从小到大排，所以就有了绝对值
    b, c = "*", " "
    if a % 2 == 0:  # 禁止输入偶数
        print("Nonono")
        break
    c *= abs(i)     # 先打印空格
    b *= (a - 2 * abs(i))   # 空格的数量刚好是高度减去空格数量的2倍，并且对于每一行都成立
    print(c, b, sep="")
# 改过了，终于成功了！！！
