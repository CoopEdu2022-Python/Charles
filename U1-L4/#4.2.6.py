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
