while 1:
    a = float(input("请输入一个数字："))
    b = float(input("请输入另一个数字："))
    c = input("你希望对这两个数怎么操作（+，-，*，/）：")
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        if b == 0:
            print("0 不可以作为除数哦~")
        else:
            print(a/b)


