import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.calc_value()

    def calc_value(self):
        RANK_VALUES = {2:2, 3:3, 4:4, 5:5, 6:6,
                       7:7, 8:8, 9:9, 'J':10, 'Q':11, 'K':12, 'A':13
                       }
        self.value = RANK_VALUES[self.rank]


class Deck():
    def __init__(self):
        self.create_deck()
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


    def create_deck(self):
        suits = ['S', 'H', 'D', 'C']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
        self.deck = []
        for suit in suits:
            for rank in ranks:
                temp_card = Card(suit, rank)
                self.deck.append(temp_card)
    

def main():
    d = Deck()
    score_a = 0
    score_b = 0
    for i in range(10):
        score_a += d.deal().value
        score_b += d.deal().value
    if score_a > score_b:
        print('Player A wins')
    elif score_b > score_a:
        print('Player B wins')
    else:
        print('Match tied')

if __name__ == '__main__':
    main()
