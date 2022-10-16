import os
winning_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player1_list = []
player2_list = []
place = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 棋盘
def plate():
    print("  {}  |  {}  |  {}  ".format(place[0], place[1], place[2]),
          " ——— + ——— + ——— ",
          "  {}  |  {}  |  {}  ".format(place[3], place[4], place[5]),
          " ——— + ——— + ——— ",
          "  {}  |  {}  |  {}  ".format(place[6], place[7], place[8]), sep="\n")


# 排列
def arrangement(player_list):   #
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


# 验证
def verdict():
    verdict_player1 = arrangement(player1_list)
    verdict_player2 = arrangement(player2_list)
    for items in verdict_player1:
        if items in winning_list:
            return 1
    for items in verdict_player2:
        if items in winning_list:
            return 2
    return 0


# 基本玩法的主体(基本上可以了，目前没测出来有什么问题，还没有设置重复输入的问题)
def basic_game_mode():
    plate()
    i = 0
    while i <= 9:
        print()
        a = int(input("Player1, it's time for you to make your choice:"))
        os.system("cls")
        player1_list.append(a)
        place[a - 1] = "x"
        plate()
        if i >= 3:
            if verdict() == 1:
                print("The winner is player1 !")
                break
        i += 1
        b = int(input("Player2, it's time for you to make your choice:"))
        os.system("cls")
        player2_list.append(b)
        place[b - 1] = "o"
        plate()
        if i >= 3:
            if verdict() == 2:
                print("The winner is player2 !")
                break
        i += 1
    if i == 9:
        print("tie")


# 变化玩法的主体(还有点问题，目前还没有完工)
def changing_game_mode():
    plate()
    record_1 = []
    record_2 = []
    while True:
        print()
        a = int(input("Player1, it's time for you to make your choice:"))
        os.system("cls")
        player1_list.append(a)
        place[a - 1] = "x"
        plate()
        if len(player1_list) > 3:
            place[player1_list[0]] = player1_list[0]
            player1_list.pop(0)
            if verdict() == 1:
                print("The winner is player1 !")
                break
        b = int(input("Player2, it's time for you to make your choice:"))
        os.system("cls")
        player2_list.append(b)
        place[b - 1] = "o"
        plate()
        if len(player2_list) > 3:
            place[player2_list[0]] = player2_list[0]
            player2_list.pop(0)
            if verdict() == 2:
                print("The winner is player2 !")
                break


Choice = input("Press 1 if you want to play the basic game mode, press 2 if you want to play the changing game mode:")
if Choice == "1":
    basic_game_mode()
elif Choice == "2":
    changing_game_mode()
else:
    print("如果你不想玩就把窗口关了，而不是在这里胡乱输入！！！让你输入1或者2你咋就那么愿意输入别的呢，故意的吧你！")
