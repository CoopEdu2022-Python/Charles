number = input("please enter a number: ")
print(number)

type(number)
print(type(number))  # 原来type是这么用的

# 买苹果
# 1. 输入苹果单价
price_str = input("请输入苹果价格：")

# 2. 要求苹果重量
weight_str = input("请输入苹果重量：")

# 3. 计算金额
# 1> 将苹果单价转换成小数
price = float(price_str)

# 2> 将苹果重量转换成小数
weight = float(weight_str)

# 3> 计算付款金额
money = price * weight

print(money)

"""
改进版本的好处：
1. 节约空间，只需要为一个变量分配空间
2. 起名字方便，不需要为中间变量起名字
"""
price = float(input("请输入价格:"))


"""
格式化字符	    含义
    %s	        字符串
    %d	        有符号十进制整数，%06d 示输出的整数显示位数，不足的地方使用0补全. 
                (06 的含义是数位不足6位的时候使用0补齐，若超过了，该是多少就是多少)
    %f	        浮点数，%.2f 表示小数点后只显示两位 (.2 and .02 are the same)
    %%	        输出 %
"""
name = "Tim"
print("My name is %s, please take care!" % name)

# 定义整数变量 student_no，输出 我的学号是 000001
stu_no = 1
print("My stu ID is %06d." % stu_no)

# 定义小数 price、weight、money，输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 9
weight = 5
money = price * weight
print("苹果单价 %.02f 元／斤，购买了 %.02f 斤，需要支付 %.02f 元" % (price, weight, money))
# 这里的%.02f指的是显示小数点后2位。如果不加的话小数点后面的位数会太多。

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.1
print("The ratio of the dat is %.2f%%" % (scale * 100))
scale = 0.1 * 100
print("The ratio of the dat is %.2f%%" % scale)
# 上面和下面的两种输出的是一个结果。




