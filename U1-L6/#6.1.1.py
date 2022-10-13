# 6.1.1 设计用例，尝试常用（加粗）的字符串方法，打印对应的结果
words = "今天我要早睡觉"
print(words)
print(words.replace("早", "晚"))
numbers = "1234"
numbers_1 = "11112哈112333"
print(" and ".join(numbers))
print(numbers_1.strip("123"))
print(numbers_1.lstrip("123"))
print(numbers_1.rstrip("123"))

print(numbers_1.removeprefix("11112"))
print(numbers_1.removesuffix("112333"))
print(words.partition("我"))
words_1 = "我今天我要早睡！"
print(words_1.rpartition("我"))
txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("apples"))
words_2 = "I wish to sleep early today"
print(words_2.split())
txt = "hello, my name is Bill, I am 63 years old"
print(txt.split(", "))
txt = "apple#banana#cherry#orange"
print(txt.split("#"))
txt = "apple#banana#cherry#orange"
print(txt.split("#", 1))  # 假设max数值为x，就从左到右，识别出x个分隔符，进行分隔操作，超出不报错。
txt = "apple, banana, cherry"
print(txt.rsplit(", ", 1))  # 从右开始找
txt = "Thank you for your visiting\nWelcome to China"
print(txt.splitlines())
print(txt.splitlines(True))
# 查找统计
txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))
print(txt.count("a"))
print(txt.find("apple"))
txt = "Hello, welcome to my world."
print(txt.startswith("wel", 7, 20))
print(txt.endswith("my world."))
txt = "   "
print(txt.isspace())  # 检查是否都是空格
txt = "CompanyX"
print(txt.isalpha())  # 检查是否都是字母
txt = "Company47"
print(txt.isalnum())  # 检查是否都是数字和数字
print(txt.upper())
print(txt.lower())


