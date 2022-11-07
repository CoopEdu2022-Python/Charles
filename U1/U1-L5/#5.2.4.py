# 5.2.4 定义一个元祖类型的购物车，用户可以不断的输入想添加的商品，输入 'q' 结束，打印出当前购物车中商品的数量，以及所有的商品
cart_list = []

while 1:
    a = input("请添加商品：")
    cart_list.append(a)
    if a == "q":
        cart_list.pop()
        break
cart_tuple = (cart_list, "购物车中有 %s 件物品" % len(cart_list))
print(cart_tuple)
