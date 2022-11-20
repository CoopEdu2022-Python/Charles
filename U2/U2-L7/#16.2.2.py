import random


class Dealer:
    def set_number(self):
        return random.randint(0, 100)

    def hint(self, n):
        if n > self.set_number():
            print("猜大了")
        elif n < self.set_number():
            print("猜小了")
        else:
            print("猜对了")

    def award(self, rounds):
        return 10 - (rounds - 1)


class Player:
    def __init__(self):
        self.points = 0

    def guess_number(self):
        return random.randint(0, 100)


dealer = Dealer()
player = Player()


def game(player, dealer):
    rounds = 0
    while player.guess_number() != dealer.set_number():
        dealer.hint(player.guess_number())
        rounds += 1
    player.points += dealer.award(rounds)
    print("游戏结束。玩家经历了 %d 轮猜数字， 获得了 %d 分。" % (rounds, player.points))
    return player.points


while 1:
    if game(player, dealer) < -10:
        print("游戏结束")
        break
