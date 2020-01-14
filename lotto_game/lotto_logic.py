import random
from constants import COUNT_OF_NUMS_IN_BAG, WIN_SCORE


class Game:
    """Main Class to init game"""
    def __init__(self, amount_card):
        rows = 3
        self.all_rows = amount_card * rows
        self.make_card()


    def make_card(self):
        """This function initializes playing card."""
        num = set()
        while len(num) < self.all_rows * 5:
            num.add(random.randint(1, COUNT_OF_NUMS_IN_BAG+1))
        cards = list(num)
        random.shuffle(cards)
        
        while len(cards) % self.all_rows != 0:
            cards.append(None)
        self.all_rows = int(len(cards) / self.all_rows)
        cards = [cards[i: i + self.all_rows] for i in range(0,len(cards),self.all_rows)]

        for i in range(len(cards)):
            sorted(cards[i])
        self.card_user = cards[:3]
        self.card_other = cards[3:]


    def search_number_on_card(self, card_player, num_bag):
        """This function is for search number from bag on playing card"""

        for i, num in enumerate(card_player):
            if num_bag in num:
                card_player[i][num.index(num_bag)] = '-'
                self.score += 1
                if self.score == WIN_SCORE:
                    sys.exit(f'{self.name} Won!')
                return True
        return False


    def print_player_card(self, card_player):
        print(f'{self.player_name:-^25}')
        print(f'{card_player[0][0]:>2} {card_player[0][1]:<10} {card_player[0][2]:<5} {card_player[0][3]} {card_player[0][4]}')
        print(f'{card_player[1][0]:>4} {card_player[1][1]:<6} {card_player[1][2]:<4} {card_player[1][3]:<4} {card_player[1][4]}')
        print(f'{card_player[2][0]} {card_player[2][1]:<5} {card_player[2][2]:<5} {card_player[2][3]:<5} {card_player[2][4]}')
        print(f'{"":-^25}')


class Player(Game):

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0


class Bag:
    """Class for generate playing bag"""

    def __init__(self, quantity):
        self.quantity = quantity
        self.generate_next_num = self.generate_num()


    def generate_num(self):
        lst = [x for x in range(1, self.quantity + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print(f'{"":*^30}')
            print(f'New number from bag: {y}')
            print(f'rest quantity in bag {self.quantity - (i+1)}')
            yield y
