from random import randrange
import re

class Card:
		def __init__(self, suit, val):
				self.suit = suit
				self.val = val
				if val > 1 and val < 11:
					self.string = str(val)
				elif val == 13:
					self.string = 'K'
				elif val == 12:
					self.string = 'Q'
				elif val == 11:
					self.string = 'J'
				else:
					self.string = 'A'

		def show(self):
				print(self.suit + self.string)
				return self
		
		def __str__(self):
				return self.suit + self.string
		
# ================================================
class Deck:
		def __init__(self):
			self.cards = []

		def reset(self):
			suits = ["♠", "♦", "♣", "♥"]
			self.cards = [Card(suit, val) for suit in suits for val in range(1, 14)]
			return self
		
		def shuffle(self):
			idx = len(self.cards) - 1
			while idx > 1:
				r = randrange(idx) 
				self.cards[r], self.cards[idx] = self.cards[idx], self.cards[r]
				idx = idx - 1
			return self

		def deal(self):
				if self.cards:
						return self.cards.pop()

		def show(self):
				print('Deck of Cards:', ', '.join([f'{card!s}' for card in self.cards]))
				return self
	# instead of the location information of the class, print a more readable information...
		def __str__(self):
				cards = ', '.join([f'{card!s}' for card in self.cards])
				return f'Deck({cards})'
	# ==============================================
class Player:
		def __init__(self, name):
				self.name = name.capitalize()
				self.hand = []
		
		def draw(self, deck):
				card = deck.deal()
				self.hand.append(card)
				return self
		
		def show(self):
				print(f'{self.name}:', ', '.join([f'{card.suit} {card.string}' for card in self.hand]))
				return self
				
		def play(self):
				return self.hand.pop()

		def discard(self):
				pass

		def __str__(self):
				return f'Player({self.name})'
	

# ====================================================
class Game:
		def __init__(self):
				self.players = []
				self.deck = Deck()
		
		def play(self, count):
				result = {'player1': 0, 'player2': 0}
				print()
				for i in range(count+1):
						val = []
						for player in self.players:
								if i == 0:
										print(f'{player.name:<10}', end='')
								else:	
										card = player.draw(self.deck).play()
								val.append(14 if card.val == 1 else card.val)
								print(f'{card.show():<10}', end='')
				if val:
						val1, val2 = val
						if val1 > val2:
								result['player1'] += 1
								print(self.players[0].name, 'Win!')
						elif val2 > val1:
								result['player2'] += 1
								print(self.players[1].name, 'Win!')
						else:
								print('Draw!')
				else:
						print()
				print(f'\n{self.players[0].name} win {result["player1"]} times  VS.  {self.players[1].name} win {result["player2"]} times')

		def start(self):
				n = 1
				self.deck.reset().shuffle()
				print(50*'=')
				print('Welcome to Deck of Cards!'.center(50))
				print(50*'=')
				while n < 3:
						name = input(f'Please input Player{n} name: ')
						if not name or name.isspace():
								name = f'Player{n}'
						self.players.append(Player(name))
						n = n + 1
				while True:
						count = input('How many cards does each player draw? ')
						if re.search(r'\D+', count) or not count:
								print('Input a number!')
						elif int(count) == 0 or int(count) > len(self.deck.cards)/2:
								print('Input a valid number!')
						else:
								break
				self.play(int(count))

# ====================================================================

# game = Game()
# game.start()

deck = Deck()
deck.reset().show()
print()
deck.shuffle().show()
print()
p1 = Player('Coco')
print(p1)
# p1.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
# p1.show()
print()
print(deck)