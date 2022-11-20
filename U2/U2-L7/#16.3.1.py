import random


class Citizen:
    def vote(self, k):
        return random.sample(k, 1)


class Judge:
    def lights_off(self):
        pass

    def lights_on(self):
        pass


class Mafia:
    def kill(self, k):
        return random.sample(k, 1)

    def vote(self, k):
        return random.sample(k, 1)


def votes(player):
    player.vote(player)
    return


players = {}
for i in range(9):
    if i < 6:
        players[i] = Citizen()
    else:
        players[i] = Mafia()
judge = Judge()
judge.lights_off()


