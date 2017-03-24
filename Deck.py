from Win import *
import random
import time
cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
suits = ['h','d','s','c']
class Game:
	#create a new game with 2 hands which is an array of 2 cards
	#deals a set of random community cards, 5 of them
	def __init__(self,handa,handb):
		self.deck = []
		self.deck_backup = []
		self.community = []
		self.handa = handa
		self.handb = handb
		for card in cards:
			for suit in suits:
				self.deck.append((card,suit))
				self.deck_backup.append((card,suit))
		for i in range(2):
			self.deck.remove((handa[i].get_name(),handa[i].get_suit()))
			self.deck.remove((handb[i].get_name(),handb[i].get_suit()))
			self.deck_backup.remove((handa[i].get_name(),handa[i].get_suit()))
			self.deck_backup.remove((handb[i].get_name(),handb[i].get_suit()))
		for i in range(5):
			self.deal_random_community_card()
	#deals a random card to the community array and removes it from the deck
	def deal_random_community_card(self):
		random_card = random.choice(self.deck)
		random_name = random_card[0]
		random_suit = random_card[1]
		self.deck.remove(random_card)
		self.community.append(Card(random_name,random_suit))
	#restores deck from backup and deals another set of community cards
	def redeal_community(self):
		self.deck = self.deck_backup[:]
		self.community = []
		for i in range(5):
			self.deal_random_community_card()
	#given 2 cards in an array hand, return the best 5 card hand you can make with the community cards
	def best_hand_out_of_seven(self,hand):
		possibilities = []
		#one possibility is you play the board
		board_hand = Hand(self.community)
		possibilities.append(board_hand)
		#one possibility is that you take one hole card and 4 commmunity
		for i in range(2):
			for j in range(5):
				community_copy = self.community[:]
				community_copy[j] = hand[i]
				new_hand = Hand(community_copy)
				possibilities.append(new_hand)
		#or you take 2 hole cards and 3 community
		for i in range(5):
			for j in range(i+1,5):
				community_copy = self.community[:]
				community_copy[i] = hand[0]
				community_copy[j] = hand[1]
				new_hand = Hand(community_copy)
				possibilities.append(new_hand)
		best_hand = possibilities[0]
		#start_time = time.time()
		for i in range(1,len(possibilities)):
			if betterHand(possibilities[i],best_hand) == 1:
				best_hand = possibilities[i]
		#print("%s seconds for one best hand" % (time.time() - start_time))
		return best_hand
	def print_community(self):
		for i in range(5):
			print(self.community[i].get_name() + self.community[i].get_suit()),

'''a = [Card('A','h'),Card('K','h')]
b = [Card('Q','h'),Card('J','h')]
game = Game(a,b)
ba = game.best_hand_out_of_seven(a)
bb = game.best_hand_out_of_seven(b)
game.print_community()
print('\nplayer A hand')
ba.print_hand()
print('\nplayer B hand')
bb.print_hand()
print(betterHand(ba,bb))'''






