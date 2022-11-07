# 4.3.6 改写 #4.2.6：函数内打印乘法表，同时，将打印的算式条数作为函数的返回值。
# 例如完整的乘法表，应有 9+8+7+……+1 共 45 条算式。用任意的方式调用函数，打印乘法表的同时，在下方打印算式条数
def chart(numbers_of_rows):
    row = 1
    while row <= numbers_of_rows:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (row, col, row * col), end="\t")
            col += 1
        print("")
        row += 1
    branch = str(int((1 + numbers_of_rows) * numbers_of_rows / 2)) + " branches in total"
    return branch


print(chart(5))


