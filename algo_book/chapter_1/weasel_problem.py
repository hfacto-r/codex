#This is the actual weasel problem
#Its hard to see that the problem converge
#MUTATION_RATE is the most important and deciding value
"""If mutation rate is too high then many character change once and convergence become practically impossible.
If mutation rate is too low, the mutation rate become so slow and convergence takes time, though convergence is guaranteed"""
import random

ALPH = 'abcdefghijklmnopqrstuvwxyz '
MUTATION_RATE = 0.0005 #A letter has 5% chance to change
POPULATION_SIZE = 200
TARGET = 'me thinks its a weasel'

def random_string(length):
    target = [random.choice(ALPH) for _ in range(length)]
    return ''.join(target)

def scoring(new_str):
    return sum([1 for i in range(len(new_str)) if new_str[i]==TARGET[i]])

def mutate(parent):
    result = []
    for ch in parent:
        if random.random() < MUTATION_RATE:
            result.append(random.choice(ALPH))
        else:
            result.append(ch)
    return ''.join(result)

def main():
    parent = random_string(len(TARGET))
    population = []
    while True:
        for _ in range(POPULATION_SIZE):
            child = mutate(parent)
            population.append(child)

        parent = max(population, key = scoring)
        print(parent)

        if parent == TARGET:
            return parent

if __name__ == '__main__':
    main()
