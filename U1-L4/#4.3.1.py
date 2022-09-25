# 4.3.1 改写 #4.2.1：函数内不打印消息，将消息作为函数的返回值。调用函数时，用一个变量接受函数的返回值，打印这个变量
def favorite_book(title):

    return title


variable = favorite_book(str(input("Which is one of your favorite book: ")))
print("One of my favorite book is", variable)
