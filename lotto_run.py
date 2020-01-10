from lotto_logic import Game, Bag, Player
import sys


def start_game():

    player1 = Player('First player card')
    player2 = Player('Second player card')
    game = Game(2)
    bag = Bag(90)
    

    while True:
        num_bag = next(bag.generate_next_num)
        player1.print_player_card(game.card_user)
        player2.print_player_card(game.card_other)
        
        user_input = input('Drop_number? Type y/n: ')
        
        if user_input == 'n':
            if player1.search_number_on_card(game.card_user, num_bag):
                sys.exit('The Game Over')
            elif player2.search_number_on_card(game.card_other, num_bag):
                continue
        if user_input == 'y':
            if player1.search_number_on_card(game.card_user, num_bag):
                continue
            else:
                sys.exit('The Game Over')
        if user_input != 'n' and user_input != 'y':
            print('Please, type y or n')
            continue
    

if __name__ == '__main__':
    start_game()
