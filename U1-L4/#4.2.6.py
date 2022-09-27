# 4.2.6 参考上节课练习 #3.3.3 的打印乘法表，定义一个函数，能够根据不同的参数，打印不同范围的九九乘法表，
# 例如参数为 1 时，只打印 '1 * 1 = 1'；参数为 9 时，打印完整的内容
def chart(numbers_of_rows):
    row = 1
    while row <= numbers_of_rows:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (row, col, row * col), end="\t")
            col += 1
        print("")
        row += 1


chart(int(input("How many rows you want to generate: ")))
