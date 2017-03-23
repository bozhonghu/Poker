from Win import *
import random
cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
suits = ['h','d','s','c']
class Game:
	#create a new game with 2 hands which is an array of 2 cards
	def __init__(self,handa,handb):
		self.deck = []
		for card in cards:
			for suit in suits:
				self.deck.append(card+suit)
		for i in range(2):
			self.deck.remove(handa[i].get_name()+handa[i].get_suit())
			self.deck.remove(handb[i].get_name() + handb[i].get_suit())
		self.random_community_cards()
	def random_community_cards(self):
		self.community = []
		for i in range(5):
			random_card = random.choice(self.deck)
			random_name = random_card[0]
			random_suit = random_card[1]
			self.deck.remove(random_card)
			self.community.append(Card(random_name,random_suit))
a = [Card('A','h'),Card('K','h')]
b = [Card('Q','h'),Card('J','h')]
game = Game(a,b)


