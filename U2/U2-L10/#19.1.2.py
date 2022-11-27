list_1 = [1, 2, 3, 4]
try:
    print(list_1[20])
finally:
    print('index out of bound!')
# 这个是先运行完毕然后打印一个提示
list_2 = [1, 2, 3, 4]
try:
    print(list_2[20])
except:
    print('index out of bound!')
# 这个是捕获异常然后做出提示
