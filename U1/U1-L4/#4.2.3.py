# 4.2.3 修改 #4.2.2 中的函数 make_shirt()，使其在默认情况下制作一件印有 "I love Python" 的短袖。
# 调用这个函数 3 次，分别制作 1 件大号短袖，印有 "I love Python"；
# 1 件中号短袖，印有 "I love Python"；1 件小号短袖，印有任意其它文字
def make_shirt(size, words):
    print("Please confirm that your shirt size is (%s) and the words you want to put on are (%s)" % (size, words))


make_shirt("L", "I love Python")
make_shirt("M", "I love Python")
make_shirt("S", "I do not love Python")
