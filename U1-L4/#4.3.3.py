# 4.3.3 改写 #4.2.3：函数内不打印消息，将消息作为函数的返回值。调用 3 次函数，分别传入不同的参数，打印出不同的消息。并且，使用 2 种调用的方式
def make_shirt(size, words):
    return "Please confirm that your shirt size is (%s) and the words you want to put on are (%s)" % (size, words)


a = make_shirt("L", "I love Python")
print(a)
print(make_shirt("M", "I love Python"))
print(make_shirt("S", "I do not love Python"))