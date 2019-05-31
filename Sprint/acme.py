import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        # Validate attributes
        assert price > 0, 'price attribute must be greater than zero'
        assert weight > 0, 'weight must be greater than zero'
        assert flammability > 0, 'flammability must be greater than zero'

        # Set attributes
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)
        self.security_score = self.price * self.flammability

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

    def security_level(self):
        if self.security_score < 5:
            return 'No worries!'
        elif (self.security_score >= 5) and (self.security_score < 50):
            return 'Put product behind the counter!'
        else:
            return 'Put product in the vault!!'


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
