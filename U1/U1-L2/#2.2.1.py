# 2.2.1 用两种不同的逻辑嵌套方式，完成火车站安检的例子
# 0 = false   1 = true
# 我稍微加了点料进去了哈哈哈哈哈，但貌似这俩乘客总是没有办法通过安检
import random
print("乘客1")
has_ticket = random.randint(0, 1)  # 是否有车票
knife_length = random.randint(1, 40)  # 刀的长度，单位：厘米

if has_ticket:  # 首先检查是否有车票，如果有，才允许进行安检
    print("有车票，可以开始安检...")

    if knife_length >= 20:  # 如果超过 20 厘米，提示刀的长度，不允许上车
        print("不允许携带 %d 厘米长的刀上车" % knife_length)
    else:  # 如果不超过 20 厘米，安检通过
        print("安检通过，祝您旅途愉快……")

else:  # 如果没有车票，不允许进门
    print("大哥，您要先买票啊")

print("乘客2")
has_ticket = random.randint(0, 1)  # 是否有车票
knife_length = random.randint(1, 40)  # 刀的长度，单位：厘米
if has_ticket and knife_length < 20:  # 两项都符合才允许上车
    print("可以上车，祝您旅途愉快……")
elif not has_ticket:  # 没有车票
    print("大哥，您要先买票啊")
elif knife_length >= 20:
    print("不允许携带 %d 厘米长的刀上车" % knife_length)
