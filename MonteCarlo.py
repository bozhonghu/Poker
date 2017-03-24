from Deck import *
#number of simulations
n = 10000
#hands to caculate win percentages
a = [Card('A','h'),Card('K','h')]
b = [Card('Q','h'),Card('J','h')]
wins = 0
game = Game(a,b)
for i in range(n):
	start_time = time.time()
	ba = game.best_hand_out_of_seven(a)
	bb = game.best_hand_out_of_seven(b)
	w = betterHand(ba,bb)
	if w == 1:
		wins += 1
	game.redeal_community()
print(float(wins)/float(n))
#currently takes 15 seconds to run one simulation, definitely need to make more efficient