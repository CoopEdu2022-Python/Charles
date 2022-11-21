import random


class Player:
    def __init__(self):
        self.points = 0

    def punch(self):
        random_list = ["stone", "scissor", "paper"]
        return random.choice(random_list)


class Computer(Player):
    def __init__(self):
        super().__init__()
    pass


def game(player, computer):
    a = player.punch()
    print(a)
    b = computer.punch()
    print(b)
    if a == "stone" and b == "scissor" or a == "scissor" and b == "paper" or a == "paper" and b == "stone":
        player.points += 1
        return "player wins"
    elif a == "stone" and b == "paper" or a == "scissor" and b == "stone" or a == "paper" and b == "scissor":
        computer.points += 1
        return "computer wins"
    else:
        return "Tie"


player = Player()
computer = Computer()
print(game(player, computer))
