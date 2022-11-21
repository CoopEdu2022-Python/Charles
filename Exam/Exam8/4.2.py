import random


class Player:
    def __init__(self):
        self.points = 0

    def punch(self):
        random_list = ["stone", "scissor", "paper"]
        return random.choice(random_list)

    def challenge(self):
        challenge_list = ["yes", "no"]
        return random.choice(challenge_list)


class Computer(Player):
    def __init__(self):
        super().__init__()
    pass


class Fraud:
    def lie(self):
        lie_list = ["lose", "tie"]
        return random.choice(lie_list)


def game(player, computer, fraud):
    a = player.punch()
    print(a)
    b = computer.punch()
    print(b)
    if a == "stone" and b == "scissor" or a == "scissor" and b == "paper" or a == "paper" and b == "stone":
        if player.challenge() == "yes":
            player.points += 2
            return "player wins"
        else:
            if fraud.lie() == "lose":
                computer += 1
                return "computer wins"
            else:
                return "Tie"
    elif a == "stone" and b == "paper" or a == "scissor" and b == "stone" or a == "paper" and b == "scissor":
        if player.challenge() == "yes":
            computer.points += 2
            return "computer wins"
        else:
            if fraud.lie() == "lose":
                computer += 1
                return "player wins"
            else:
                return "Tie"
    else:
        return "Tie"


player = Player()
computer = Computer()
fraud = Fraud()
print(game(player, computer, fraud))
