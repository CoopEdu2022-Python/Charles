# 5.3.5 编写一个函数 update_dict(dict_sample)，功能如下
# 用户输入一个 key-value（分 2 次输入），value 为数字类型，key 为 str 类型
# 如果原有的 dict_sample 中没有用户输入的 key，就添加这个 key-value
# 如果原有的 dict_sample 中存在用户输入的 key，保留较大的 value
# 将修改后的字典作为返回值

def update_dict(key1, value1, key2, value2):
    dict_sample = {"number1": 17, "number2": 53}
    dict_input1 = {key1: value1}
    dict_input2 = {key2: value2}
    a = 0
    b = 0
    for key in dict_sample:
        if key1 == key:
            if value1 != dict_sample.get(key):
                if value1 > dict_sample.get(key):
                    dict_sample[key1] = value1
                elif value1 < dict_sample.get(key):
                    dict_input1[key1] = dict_sample.get(key)
                a += 1
        elif key2 == key:
            if value2 != dict_sample.get(key):
                if value2 > dict_sample.get(key):
                    dict_sample[key2] = value2
                elif value2 < dict_sample.get(key):
                    dict_input2[key2] = dict_sample.get(key)
                b += 1
    if a == 0:
        dict_sample.update(dict_input1)
    if b == 0:
        dict_sample.update(dict_input2)
    return dict_sample


output = update_dict(str(input("Enter the first key: ")), int(input("Enter a value for the first key: ")),
                     str(input("Enter the second key: ")), int(input("Enter a value for the second key: ")))
print(output)

