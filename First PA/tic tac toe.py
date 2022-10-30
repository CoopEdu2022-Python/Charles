import os
winning_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player1_list = []
player2_list = []
place = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 数字棋盘


# 棋盘
def plate():  # 实体棋盘
    print("  {}  |  {}  |  {}  ".format(place[0], place[1], place[2]),
          " ——— + ——— + ——— ",
          "  {}  |  {}  |  {}  ".format(place[3], place[4], place[5]),
          " ——— + ——— + ——— ",
          "  {}  |  {}  |  {}  ".format(place[6], place[7], place[8]), sep="\n")


# 排列(逻辑合理，目前没发现问题)
def arrangement(player_list):   # 返回玩家列表中所有可能的三个数的组合，以便做进一步胜利失败的验证
    player_arranged_list = []
    player_arranged_list1 = []
    for x in range(0, len(player_list) - 2):
        for y in range(x + 1, len(player_list) - 1):
            for z in range(x + 2, len(player_list)):
                player_arranged_list.append(sorted([player_list[x], player_list[y], player_list[z]]))
    for p in player_arranged_list:
        if p not in player_arranged_list1:
            player_arranged_list1.append(p)
    return player_arranged_list


# 验证(逻辑合理，目前没发现问题)
def verdict():
    verdict_player1 = arrangement(player1_list)
    verdict_player2 = arrangement(player2_list)
    for items in verdict_player1:   # 验证，验证列表中是否包含胜利列表中的组合，下面的也如此
        if items in winning_list:
            return 1
    for items in verdict_player2:
        if items in winning_list:
            return 2
    return 0  # 两个验证都没返回就返回0，游戏继续


# 正确输入验证
def input_verification(player_input):
    while not player_input.isdigit():
        print("Wrong input! Only numbers are allowed!")
        if len(player_input) > 1:
            print("and you can only enter one number")
        player_input = input("Please make your choice again:")
    while player_input in (player1_list or player2_list):
        print("This place has been taken!")
        player_input = input("Please make your choice again:")
    return player_input


# 基本玩法的主体(基本上可以了，目前没测出来有什么问题)
def basic_game_mode():
    nothing = input("For all players, you can only input numbers!!!(press enter to continue)")
    os.system("cls")
    plate()  # 展示棋盘
    i = 0
    while i <= 9:
        print()  # 换行
        a = int(input_verification(input("Player1, it's time for you to make your choice:")))  # Player1输入棋子
        os.system("cls")
        player1_list.append(a)  # 放置棋子
        place[a - 1] = "x"  # 棋盘显示
        plate()
        if i >= 3:
            if verdict() == 1:  # 验证
                return "The winner is player1 !"

        i += 1
        if i == 9:
            return "Tie"  # 平局提醒

        print()  # 换行
        b = int(input_verification(input("Player2, it's time for you to make your choice:")))  # Player2输入棋子
        os.system("cls")
        player2_list.append(b)
        place[b - 1] = "o"  # 棋盘显示
        plate()
        if i >= 3:
            if verdict() == 2:  # 验证
                return "The winner is player2 !"
        i += 1


# 变化玩法的主体(差不多了)
def changing_game_mode():
    nothing = input("For all players, you can only input numbers!!!\n"
                    "The changing game mode will only keep 7 piece in the plate.\n"
                    "don't worry, we will remind you when and which pieces will be deleted.\n"
                    "(press enter to continue)")
    os.system("cls")
    plate()  # 展示棋盘
    while True:
        print()
        if len(set(player1_list)) == 3:
            print("%s will be deleted" % player1_list[0])  # 提示删除棋子
            place[player1_list[0] - 1] = player1_list[0]  # 删除棋盘列表中的棋子，替换为原始数字
            player1_list.pop(0)  # 玩家列表中删除棋子
        a = int(input_verification(input("Player1, it's time for you to make your choice:")))  # Player1输入棋子
        player1_list.append(a)
        place[a - 1] = "x"  # 棋盘显示
        os.system("cls")
        plate()
        if verdict() == 1:  # 验证
            return "The winner is player1 !"

        print()
        if len(player2_list) == 3:
            print("%s will be deleted" % player2_list[0])  # 提示删除棋子
            place[player2_list[0] - 1] = player2_list[0]  # 删除棋盘列表中的棋子，替换为原始数字
            player2_list.pop(0)
        b = int(input_verification(input("Player2, it's time for you to make your choice:")))  # Player2输入棋子
        player2_list.append(b)
        place[b - 1] = "o"  # 棋盘显示
        os.system("cls")
        plate()
        if verdict() == 2:  # 验证
            return "The winner is player2 !"


set_up_number = 0
while 1:
    if set_up_number > 0:
        enter = input("If you want to play again, press enter.\n"
                      "If not, you can close the command window.")
        player1_list = []
        player2_list = []
        place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        os.system("cls")
    Choice = input("Press 1 if you want to play the basic game mode, \n"
                   "press 2 if you want to play the changing game mode:")
    os.system("cls")
    if Choice == "1":
        print(basic_game_mode())
        set_up_number += 1
    elif Choice == "2":
        print(changing_game_mode())
        set_up_number += 1
    else:
        print("如果你不想玩就把窗口关了，而不是在这里胡乱输入！！！让你输入1或者2你咋就那么愿意输入别的呢，故意的吧你！")
