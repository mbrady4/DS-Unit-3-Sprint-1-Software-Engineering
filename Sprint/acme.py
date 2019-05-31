import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif (ratio >= 0.5) and (ratio < 1):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        flame_score = self.flammability * self.weight
        if flame_score < 10:
            return '...fizzle.'
        elif (flame_score >= 10) and (flame_score < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10, flammability=0.5, weight=10):
        super().__init__(name=name, weight=weight, price=price,
                         flammability=flammability)

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif (self.weight >= 5) and (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
