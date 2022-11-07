# 4.2.4 编写一个名为 describe_city() 的函数，它接受 1 座城市的名字以及该城市所属的国家。
# 这个函数应打印 1 个简单的句子，如 "Beijing is in China"。
# 给用于存储国家的形参指定默认值。为 3 座不同的城市调用这个函数，且其中至少有 1 座城市不属于默认国家
def describe_city(city, country="China"):
    print("%s is in %s" % (city, country))


describe_city("Shanghai")
describe_city("Beijing")
describe_city("London", "the UK")
