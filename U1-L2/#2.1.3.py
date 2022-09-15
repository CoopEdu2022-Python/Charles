# 2.1.3 将 #2.1.2 中的 if-else 结构改为 if-elif-else 结构
# 如果外星人是红色的，就打印一条消息，指出玩家获得了 5 个 points
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了 10 个 points
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了 15 个 points
# 编写这个程序的三个版本，它们分别在外星人为红色、绿色和黄色时打印一条消息
alien_color = int(input("Enter the color of the alien(Green(1),Yellow(2), Red(3): "))
if alien_color == 1:
    print("Five points gained")
elif alien_color == 2:
    print("Ten points gained")
elif alien_color == 3:
    print("Fifteen points gained")
