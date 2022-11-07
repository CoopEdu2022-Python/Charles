# 5.3.4 下方是一个字典，记录了小明和小刚买水果的详细情况，为小明和小刚分别打印一条消息，描述他们买了哪些水果，花了多少钱
info = {
    '小明': {
        'fruits': ['苹果', '草莓', '香蕉'],
        'money': 89
    },
    '小刚': {
        'fruits': ['葡萄', '橘子', '樱桃'],
        'money': 87
    }
}
# "小明" = A     "小刚" = B
dict_A = info["小明"]
dict_B = info["小刚"]
name = list(info.keys())

# print(info["小明"]['fruits'][0])

print(
    "%s买了%s，%s，%s，一共花了%s元"
    % (name[0],
       info["小明"]['fruits'][0],
       info["小明"]['fruits'][1],
       info["小明"]['fruits'][2],
       info["小明"]['money'])
)

print(
    "%s买了%s，%s，%s，一共花了%s元"
    % (name[0],
       info["小刚"]['fruits'][0],
       info["小刚"]['fruits'][1],
       info["小刚"]['fruits'][2],
       info["小刚"]['money'])
)

print(
    f"{name[0]}买了{info['小明']['fruits'][0]}，{info['小明']['fruits'][1]}，{info['小明']['fruits'][2]}，一共花了{info['小明']['money']}元")
# 最后这个是个什么输出方式啊，我看这是pycharm给我推荐的（帮我改的）一个
