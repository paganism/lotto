import random


class Game:
    
    def __init__(self, amount_card):
        rows = 3
        self.all_rows = amount_card * rows
        self.make_card()


    def make_card(self):
        num = set()
        while len(num) < self.all_rows * 5:
            num.add(random.randint(1, 91))
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
        for i, num in enumerate(card_player):
            if num_bag in num:
                card_player[i][num.index(num_bag)] = '-'
                self.score += 1
                if self.score == 15:
                    sys.exit(f'{self.name} Won!')
                return True
        return False


    def print_player_card(self, card_player):
        print('{:-^25}'.format(self.player_name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format( '-'))


class Player(Game):

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0


class Bag:
    
    def __init__(self, quantity):
        self.quantity = quantity
        self.generate_next_num = self.generate_num()


    def generate_num(self):
        lst = [x for x in range(1, self.quantity + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:*^30}'.format('*'))
            print(f'New number from bag: {y}')
            print(f'rest quantity in bag {self.quantity - (i+1)}')
            yield y
