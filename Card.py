from mergesort import *
card_names_to_rank = {'A':14, 'K':13, 'Q':12, 'J':11, '10':10, '9':9, '8':8, '7':7, '6':6,
'5':5,'4':4,'3':3, '2':2}
class Card:
	#create a new card with inputs of num and suit, both strings
	def __init__(self,num,suit):
		self.rank = card_names_to_rank[num]
		self.suit = suit
	def get_rank(self):
		return self.rank
	def get_suit(self):
		return self.suit
class Hand:
	#create a new hand with array containing 5 cards
	def __init__(self,cards):
		self.hand = cards
	#functions to help classify hands
	def isHighCard(self):
		self.rank = 1
	#if there is a pair then the variable pair will be set to the rank of the pair
	def isPairsOrTripsOrQuadsOrFull(self):
		seen = [0]*15
		counter = 0
		pair = []
		for card in self.hand:
			if seen[card.get_rank()] != 0:
				counter += 1
				seen[card.get_rank()] += 1
				pair.append(card.get_rank())
			else:
				seen[card.get_rank()] += 1
		if counter == 1:
			self.rank = 2
			self.onepair = pair[0]
			self.kickers = []
			for card in self.hand:
				if card.get_rank() != self.onepair:
					self.kickers.append(card.get_rank())
		if counter == 2:
			if pair[0] == pair[1]:
				self.rank = 4
				self.trips = pair[0]
				self.kickers = []
				for card in self.hand:
					if card.get_rank() != self.trips:
						self.kickers.append(card.get_rank())
			else:
				self.rank = 3
				self.twopair = pair
				self.kickers = []
				for card in self.hand:
					if card.get_rank() != pair[0] and card.get_rank() != pair[1]:
						self.kickers.append(card.get_rank())
		if counter == 3:
			if pair[0] == pair[1] and pair[1] == pair[2]:
				self.rank = 8
				self.quads = pair[0]
				self.kickers = []
				for card in self.hand:
					if card.get_rank() != self.quads:
						self.kickers.append(card.get_rank())
			else:
				self.rank = 7
				if pair[0] == pair[1]:
					self.fulltrip = pair[0]
					self.fullpair = pair[2]
				elif pair[0] == pair[2]:
					self.fulltrip = pair[0]
					self.fullpair = pair[1]
				else:
					self.fulltrip = pair[1]
					self.fullpair = pair[0]
	def isStraight(self):
		ranks = []
		for card in self.hand:
			ranks.append(card.get_rank())
		ranks = mergesort(ranks)
		for i in range(1,5):
			if i == 4 and ranks[i] == 14 and ranks[i-1] == 5:
				self.rank = 5
				self.straight = 5
				return True
			elif i == 4 and ranks[i] == ranks[i-1] + 1:
				self.rank = 5
				self.straight = ranks[4]
				return True
			elif ranks[i] != ranks[i-1] + 1:
				return False
		return False
	def isFlush(self):
		suits = []
		for card in self.hand:
			suits.append(card.get_suit())
		for i in range(1,5):
			if suits[i] != suits[i-1]:
				return False
		self.rank = 6
		return True
	def caculate_rank(self):
		self.isHighCard()
		self.isPairsOrTripsOrQuadsOrFull()
		one = self.isStraight() 
		two = self.isFlush()
		if one and two:
			#straight flush
			self.rank = 9

