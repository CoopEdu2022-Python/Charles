# 4.3.4 改写 #4.2.4：函数内不打印消息，如果输入的城市和国家匹配，将返回值设置为 'YES'；如果不匹配，将返回值设置为 'NO'。
# 调用 3 次函数，传入不同的参数，输出不同的结果。并且，使用 2 种调用的方式
China = ["Beijing", "Shanghai"]
def city_country(city, country):
    if city is not country:
        return "No"
    else:
        return "Yes"


print(city_country("Beijing", China))
# 我不知道这个从属关系在代码里面应该怎么设置了
