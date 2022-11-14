class Animal:
    def __init__(self, health=100):
        self.health = health


class Manager:
    def feed(self):
        pass

    def perform(self):
        pass

    def __inspect(self):
        pass


class Keeper(Manager):
    def __init__(self, number):
        self.performance = number

