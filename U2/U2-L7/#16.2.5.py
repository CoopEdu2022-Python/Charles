import random


class Dealer:
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


    def award(self, rounds):
        return 10 - (rounds - 1)


class Player:
    def __init__(self):
        self.points = 0

    def guess_number(self, n1, n2):
        return random.randint(n1, n2)


class Rule:
    def __init__(self):
        self.rounds = 0

    def judge(self, player, dealer):
        player.points += dealer.award(self.rounds)


dealer = Dealer()
player = Player()
judger = Rule()


def game(player, dealer, judger):
    a = dealer.set_number()
    print(a)
    n1 = 0
    n2 = 100
    guess_number = player.guess_number(n1, n2)
    while player.guess_number(n1, n2) != a:
        judge = dealer.hint(guess_number)
        if judge == 1:
            n2 = guess_number - 1
        elif judge == -1:
            n1 = guess_number + 1
        judger.rounds += 1
    judger.judge(player, dealer)
    print("游戏结束。玩家经历了 %d 轮猜数字， 获得了 %d 分。" % (judger.rounds, player.points))
    return player.points


game(player, dealer, judger)
