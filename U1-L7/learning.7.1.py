# 1. 用多行注释的方式，写出 Python 目前所有的内置函数
"""
内置函数

A
abs()
aiter()
all()
any()
anext()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()

E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()




R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()
"""


# 2. 用多行注释的方式，说明什么是公共方法；同时，用一些代码举几个简单的例子
"""
字符串，列表，字典，元组都可以使用的方法叫做公共方法
包含内置函数，切片，运算符，以及完整的 for 循环语法
内置函数                    描述                   备注
len(item)                 计算容器中元素个数
del(item)                 删除变量                两种方式: del(item); del item
max(item)                 返回容器中最大值          如果是字典，只针对 key 比较
min(item)                 返回容器中最小值          如果是字典，只针对 key 比较
cmp(item1, item2)                                取消了

                Python表达式            结果        支持的数据类型
切片          "0123456789"[::-2]      "97531"         除了字典

运算符                       Python 表达式                   结果                           描述              支持的数据类型
+                           [1, 2] + [3, 4]               [1, 2, 3, 4]                   合并                除了字典
*                           ["Hi"] * 4                    ["Hi", "Hi", "Hi", "Hi", ]     重复                除了字典
in                          3 in [1, 2, 3]                True                           元素是否存在          所有
not in                      4 not in [1, 2, 3]            True                           元素是否不存在        所有
>; >=; ==; <=; <            (1, 2, 3) < (2, 2, 3)         True                           元素比较             除了字典

"""

# 3. 用多行注释的方式，简单描述公共方法和内置函数的关系
"""
内置函数主要是针对数字类型的使用的，虽然公共方法中也存在内置函数，不过可以绝大多数数据类型进行使用，不仅限于数字类型。
"""
