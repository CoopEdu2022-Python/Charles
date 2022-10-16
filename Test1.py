winning_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
player1_list = []
player2_list = []


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


i = 0
while i <= 9:
    a = int(input("Player1, it's time for you to make your choice:"))
    player1_list.append(a)
    if i >= 3:
        if verdict() == 1:
            print("The winner is player1 !")
            break
    i += 1
    b = int(input("Player2, it's time for you to make your choice:"))
    player2_list.append(b)
    if i >= 3:
        if verdict() == 2:
            print("The winner is player2 !")
            break
    i += 1
if i == 9:
    print("tie")
