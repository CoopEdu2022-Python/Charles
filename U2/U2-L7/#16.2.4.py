import random


class Dealer:
    def __init__(self):
        self.number = 0

    def set_number(self):
        self.number = random.randint(0, 100)
        return self.number

    def hint(self, n):
        if n > self.number:
            print("猜大了")
            return 1
        elif n < self.number:
            print("猜小了")
            return -1
        else:
            print("猜对了")
            return 0

    def award(self, rounds, player):
        player.points = 10 - (rounds - 1)


class Player:
    def __init__(self, points):
        self.points = points

    def guess_number(self, n1, n2):
        return random.randint(n1, n2)


dealer = Dealer()
player = Player(0)


def game(player, dealer):
    a = dealer.set_number()
    print(a)
    rounds = 0
    n1 = 0
    n2 = 100
    guess_number = player.guess_number(n1, n2)
    while True:
        rounds += 1
        judge = dealer.hint(guess_number)
        if judge == 1:
            n2 = guess_number - 1
        elif judge == -1:
            n1 = guess_number + 1
        else:
            break
        guess_number = player.guess_number(n1, n2)

    dealer.award(rounds, player)
    print("游戏结束, 玩家经历了 %d 轮猜数字， 获得了 %d 分。" % (rounds, player.points))
    return player.points


game(player, dealer)
