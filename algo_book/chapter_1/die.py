import random
class MSDie:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides
        self.current_value = self.roll()

    def __str__(self):
        return f'D{self.no_of_sides}'

    def __repr__(self):
        return f'MSDie({self.no_of_sides})'

    def roll(self):
        return random.randint(1, self.no_of_sides + 1)

my_die = MSDie(6)
       
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()
    
