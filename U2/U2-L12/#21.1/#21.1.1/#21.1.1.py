import linecache

filename = 'txt'
text = linecache.getline(filename, 3)
print(text)


import os

result = os.popen('sed -n {}p {}'.format(2, filename)).read()

"""
我查的那个文档里面发现了这两种方法，第一种比较适合文本数量不多的情况，第二种比较适合文本数量非常多的情况。
但是第二种我在控制台好像看不到输出就有点奇怪。
"""
