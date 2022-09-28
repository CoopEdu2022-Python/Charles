# 字典是一个无序的数据集合，使用print函数输出字典时，通常
# 输出的顺序和定义的顺序是不一致的！(python 改版了，现在的输出是一样的顺序了)

xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 75.5}
print(xiaoming)

""""""""""""""""""""""""""""""""""""""""""""""""

xiaoming_dict = {"name": "小明"}

# 1.取值
# 如果指定的key不存在，程序就会报错
print(xiaoming_dict["name"])
# 2.增加/修改
# key不存在则会增加
xiaoming_dict["age"] = 18  # 增加
# key存在则会修改
xiaoming_dict["name"] = "小小明"  # 修改
# 3。删除
# 如果指定的key不存在，程序就会报错
xiaoming_dict.pop("name")  # 删除

""""""""""""""""""""""""""""""""""""""""""""""""

xiaoming = {"name": "小明",
            "age": 18,}
# 1.统计键值对数量
print(len(xiaoming_dict))
# 2.合并字典
temp_dict={"height": 1.75,
           "age": 20}
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
# 3.清空字典
xiaoming_dict.clear()

print(xiaoming_dict)

""""""""""""""""""""""""""""""""""""""""""""""""

xiaoming_dict={"name": "小明",
               "qq": "123456",
               "phone": "10086"}
# 送代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:

    print("%s-%s"%(k, xiaoming_dict[k]))


# 使用多个键值对，存储描述一个物体的相关信息—描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历
card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]
for card_info in card_list:
    print(card_info)
