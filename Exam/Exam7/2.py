class Animal:
    def __init__(self, health):
        self.health = health


class Manager:
    def feed(self):
        Animal(self).health += 20
        pass

    def perform(self):
        Animal(self).health -= 20
        pass

    def __inspect(self):
        if Keeper(self).performance >= 80:
            return "nice work, keep going"
        pass


class Keeper(Manager):
    def __init__(self, number):
        self.performance = number
        if Animal(self).health < 80:
            self.performance -= 20

    def perform(self):
        print("There's no 'perform' method for the Animal Keeper")


class Trainer(Manager):
    def __init__(self, number):
        self.performance = number
        if Animal(self).health < 80:
            self.performance -= 20


    def feed(self):
        print("There's no 'feed' method for the Animal Trainer")


animal = Animal(100)
keeper = Keeper
trainer = Trainer


def everyday():
    pass