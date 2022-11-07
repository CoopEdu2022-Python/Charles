# 2.1.2 像 #2.1.1 那样设置外星人的颜色，并编写一个 if-else 结构
# 如果外星人不是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个 points
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 10 个 points
# 编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块
# First version
alien_color = "yellow"
if alien_color != "green":
    print("Five points gained for killing that alien!")
else:
    print("Ten points gained!")
# Second version
alien_color = "green"
if alien_color != "green":
    print("Five points gained for killing that alien!")
else:
    print("Ten points gained!")
