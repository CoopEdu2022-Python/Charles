# 5.2.1 回忆你在学校吃过的 5 道菜品，并存储在元组 menu 中
# 使用 for 循环将菜单的菜品打印出来
# 尝试修改其中的一个元素，查看错误信息，以注释的形式将错误信息添加在上面一行；然后，将发生错误的代码注释，保证程序能正常运行
# 学校调整了菜单，替换了它提供的其中 2 道菜品。想办法修改菜单，并打印新版本的菜单
menu = ("比萨", "牛排", "锅包肉", "西湖醋鱼", "西红柿炒鸡蛋")
# menu[1] = "面包"
# TypeError: 'tuple' object does not support item assignment
menu1 = ("面包", "烤冷面", "锅包肉", "西湖醋鱼", "西红柿炒鸡蛋")
menu = menu1
print(menu)