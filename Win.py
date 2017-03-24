from Card import *
#returns 1 if hand a is better, 2 is hand b is better, and 3 if it is a tie
def betterHand(a, b):
	'''Input type a and b are Hand objects
	Output type int'''
	rank_a = a.get_rank()
	rank_b = b.get_rank()
	if(rank_a > rank_b):
		return 1
	elif rank_a < rank_b:
		return 2
	else:
		card_ranks_a = []
		card_ranks_b = []
		for i in range(5):
			card_ranks_a.append(a.get_cards()[i].get_rank())
			card_ranks_b.append(b.get_cards()[i].get_rank())
		card_ranks_a = high_mergesort(card_ranks_a)
		card_ranks_b = high_mergesort(card_ranks_b)
		#if both high card then need to run through the cards in the hand from high to low
		#card ranks are already sorted high to low
		if rank_a == 1:
			for i in range(5):
				if(card_ranks_a[i] > card_ranks_b[i]):
					return 1
				elif(card_ranks_a[i] < card_ranks_b[i]):
					return 2
			return 3
		#if its pair then we first check the rank of the pair and then check kickers
		elif rank_a == 2:
			if a.onepair > b.onepair:
				return 1
			elif a.onepair < b.onepair:
				return 2
			else:
				#a one pair will always have 3 kickers
				#kickers is already sorted high to low
				for i in range(3):
					if a.kickers[i] > b.kickers[i]:
						return 1
					elif a.kickers[i] < b.kickers[i]:
						return 2
				return 3
		#next check two pair, the pair is already sorted from high to low
		elif rank_a == 3:
			for i in range(2):
				if a.twopair[i] > b.twopair[i]:
					return 1
				elif a.twopair[i] < b.twopair[i]:
					return 2
			#two pair will always have only 1 kicker
			if a.kickers[0] > b.kickers[0]:
				return 1
			elif a.kickers[0] < b.kickers[0]:
				return 2
			else:
				return 3
		#next check trips
		elif rank_a == 4:
			if a.trips > b.trips:
				return 1
			elif a.trips < b.trips:
				return 2
			else:
				#trips will always have 2 kickers sorted from high to low
				for i in range(2):
					if a.kickers[i] > b.kickers[i]:
						return 1
					elif a.kickers[i] < b.kickers[i]:
						return 2
				return 3
		#next check straight, a straight only cares about the high card
		elif rank_a == 5:
			if card_ranks_a[0] > card_ranks_b[0]:
				return 1
			elif card_ranks_a[0] < card_ranks_b[0]:
				return 2
			else:
				return 3
		#next check flush, same method of checking as checking for high card
		elif rank_a == 6:
			for i in range(5):
				if(card_ranks_a[i] > card_ranks_b[i]):
					return 1
				elif(card_ranks_a[i] < card_ranks_b[i]):
					return 2
			return 3
		#next check full house, first check the trips, then check the pair
		elif rank_a == 7:
			if a.fulltrip > b.fulltrip:
				return 1
			elif a.fulltrip < b.fulltrip:
				return 2
			else:
				if a.fullpair > b.fullpair:
					return 1
				elif a.fullpair < b.fullpair:
					return 2
				else:
					return 3
		#next check quads, quads only have 1 kicker
		elif rank_a == 8:
			if a.quads > b.quads:
				return 1
			elif a.quads < b.quads:
				return 2
			else:
				if a.kickers[0] > b.kickers[0]:
					return 1
				elif a.kickers[0] < b.kickers[0]:
					return 2
				else:
					return 3
		#it can only be a straight flush left, only care about high card
		else:
			if card_ranks_a[0] > card_ranks_b[0]:
				return 1
			elif card_ranks_a[0] < card_ranks_b[0]:
				return 2
			else:
				return 3
c1 = Card('A','h')
c2 = Card('K','h')
c3 = Card('7','h')
c4 = Card('9','h')
c5 = Card('2','h')
s = [c1,c2,c3,c4,c5]
handa = Hand(s)
c1 = Card('7','h')
c2 = Card('9','h')
c3 = Card('2','h')
c4 = Card('Q','h')
c5 = Card('J','h')
s = [c1,c2,c3,c4,c5]
handb = Hand(s)






