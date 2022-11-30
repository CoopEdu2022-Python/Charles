file = open("bad_boy.py", "r+")
a = file.readlines()
count = 0
line = 0
for items in a:
    line += 1
    alpha = 0
    if items[0].isalpha():
        continue
    for item in items:
        if item.isalpha():
            file.write((" " * ((count // 4 + 1) - count)) + items)
            print((count // 4 + 1) - count)
            print((" " * ((count // 4 + 1) - count)) + items)
            break
        count += 1
file.close()
"""
不用麻烦跑了，这个不对，但是我不会了
"""

