# game!
import random
from random import shuffle
import time

while True:
    class Card:
        def __init__(self, val, suit):
            # Attributes
            self.value = val
            self.suit = suit
            self.played = False

    class Deck:
        def __init__(self):
            self.cards = []
        def buildDeck(self):
            self.cards = []
          # create a deck 4 suits, each suit has 13 cards
            for suit in ['♥ hearts', '♣ clubs', '♦ diamonds', '♠ spades']:
                for i in range(1, 14):
                    self.cards.append(Card(i, suit))
            return self
        def shuffle(self):
        # fisher yates shuffle 
            for _ in range(1):
                for i in range(len(self.cards)-1, 0, -1):
                    random_i = random.randint(0, i)
                    if i == random_i:
                        continue
                    self.cards[i], self.cards[random_i] = self.cards[random_i], self.cards[i]
            random.shuffle(self.cards)
            return self
          
        def show(self):
            for i in range(len(self.cards)):
                print(self.cards[i].value, self.cards[i].suit)
                time.sleep(0.05)
            print('cards length ->>', len(self.cards))
            return self
        
        def compare_cards(self, player_card_i, name, player1, player2):
            # if player1.player_card_value > player2.player_card_value:
            #   print(f'{player1.name} has a card of {player1.player_card_value}, which is > than {player2.name} of card {player2.player_card_value}')
            print(f'{name} has a card -> {self.cards[player_card_i].value}, {self.cards[player_card_i].suit}')
            # player2.player_card = self.cards[player_card_i].value
            # player1.player_card.append({self.cards[player_card_i].value}, {self.cards[player_card_i].suit})
            # player2.player_card.append({self.cards[player_card_i].value}, {self.cards[player_card_i].suit})
            # player2.player_card.append({self.cards[playe_card_i].value}, {self.cards[player_card_i].suit})
            return self
              
    newDeck = Deck()
    newDeck.buildDeck()
    print('\n🃏 building deck....')
    time.sleep(1)
    newDeck.show().shuffle()
    print("     _            __  __ _       ")
    print("    | |          / _|/ _| |      ")
    print(" ___| |__  _   _| |_| |_| | ___  ")
    print("/ __| '_ \| | | |  _|  _| |/ _ \ ")
    print("\__ \ | | | |_| | | | | | |  __/ ")
    print("|___/_| |_|\__,_|_| |_| |_|\___| ")
    print(" ")
    print(" fisher yates shuffling deck... 🔀")
    # print('\nshuffling deck... 🔀')
    time.sleep(2)
    newDeck.show()

    class User:
        def __init__(self, name):
            self.name = name
            self.player_card = ""
          
        def take_a_card(self):
            self.player_card_i = random.randint(1, 51)
            # print(f'{self.name} picked a card at idx {self.player_card_i}')
            # newDeck.compare_cards(self.player_card_i, self.name)
            self.player_card_value = newDeck.cards[self.player_card_i].value
            self.player_card_suit = newDeck.cards[self.player_card_i].suit
            print(f'{self.name}, took a card form deck, {self.player_card_value}{self.player_card_suit}')
            return self
        
        def show_player_card(self):
            # print(f'USER CLASS -> {self.name} has card -> {self.player_card_value}')
            pass
      
    print('\n players turn... 👈')
    player1 = User(input("Type player 1's name:"))
    player2 = User(input("Type player 2's name:"))

    print('*'*28)

    player1.take_a_card()
    player1.show_player_card()
    time.sleep(1)

    player2.take_a_card()
    player2.show_player_card()
    time.sleep(1)

    # newDeck.compare_cards(player1, player2)

    # player1.show_player_card()
    # player2.show_player_card()


    print('*'*28)
    # print(player1.player_card_value)

    if int(player1.player_card_value) > int(player2.player_card_value):
        print(player1.name, ' WON !!! 🎉🎆🎊\n')
    elif int(player1.player_card_value) < int(player2.player_card_value):
        print(player2.name, ' WON !!! 🎉🎆🎊\n')

    if int(player1.player_card_value) == int(player2.player_card_value):
        print('🙀    ¯\_(ツ)_/¯     😨 \n')

    time.sleep(1)

    play_again = input("PLAY AGAIN? 'y' / 'n': ")
    if play_again == "yes" or play_again == "y":
        continue
    else:
        break