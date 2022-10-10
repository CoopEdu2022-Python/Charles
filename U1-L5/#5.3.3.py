# 5.3.3 下方是一个字典，按要求完成操作
# ① 字典的长度是多少
# ② 请修改 'java' 这个 key 对应的 value 值为 98
# ③ 删除 c 这个 key
# ④ 增加一个 key-value 对，key 值为 php, value 是 90
# ⑤ 获取所有的 key 值，存储在列表里
# ⑥ 获取所有的 value 值，存储在列表里
# ⑦ 判断 javascript 是否在字典中
# ⑧ 获得字典里所有 value 的和
# ⑨ 获取字典里最大的 value
# ⑩ 获取字典里最小的 value
# ⑪ 字典 dic1 = {'php': 97}，将 dic1 的数据更新到 dic 中
dict = {
    'python': 95,
    'java': 99,
    'c': 100
}
print(len(dict))

dict['java'] = 98
print(dict)

dict.pop('c')
print(dict)

dict['php'] = 90
print(dict)

key_list = []
for key in dict:
    key_list.append(key)
print(key_list)

value_list = []
for value in dict.values():
    value_list.append(value)
print(value_list)

print("javascript" in dict)

i = 0
for item in value_list:
    i += item
print(i)

value_list.sort()
print(value_list[0])

print(value_list[2])

dict['php'] = 97
print(dict)
