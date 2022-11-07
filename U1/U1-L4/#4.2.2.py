# 4.2.2 编写一个名为 make_shirt() 的函数，用户输入尺码以及要印到短袖上的文字。
# 这个函数应打印一个句子，告知用户短袖的尺码和文字，便于用户确认
def make_shirt(size, words):
    print("Please confirm that your shirt size is (%s) and the words you want to put on are (%s)" % (size, words))


make_shirt(str(input("please enter your shirt size: ")),
           str(input("please enter the words you want to put on your shirt: ")))
# 我靠原来代码太长还可以这样换行的么
