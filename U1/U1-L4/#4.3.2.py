# 4.3.2 改写 #4.2.2：函数内不打印消息，将消息作为函数的返回值。调用函数时，在 print 语句中直接调用函数，打印提示信息
def make_shirt(size, words):

    return "Please confirm that your shirt size is (%s) and the words you want to put on are (%s)" % (size, words)



print(make_shirt(str(input("please enter your shirt size: ")),
           str(input("please enter the words you want to put on your shirt: "))))


