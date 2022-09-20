a = int(input("请输入高度："))
for i in range(1, a + 1):
    b = " "
    c = "*"
  #  if i % 2 != 0:

# 写不出来
# 下面是查到的
def draw(num):
    a = "*" * (2 * (4 - num) + 1)
    print(a.center(9, ' '))
    if num != 1:
        draw(num - 1)
        print(a.center(9, ' '))

draw(int(input("请输入4：")))
