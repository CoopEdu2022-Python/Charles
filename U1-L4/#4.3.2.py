# 4.3.2 改写 #4.2.2：函数内不打印消息，将消息作为函数的返回值。调用函数时，在 print 语句中直接调用函数，打印提示信息
def make_shirt(size, words):

    return "L", "I'm the boss"


print(make_shirt())

# 现在这个样子貌似也不太对
# 我感觉我没太理解这个return到底要干什么，周中找时间问您吧，这次作业就先空着了
