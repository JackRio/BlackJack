#Function defination
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from Global import Global as G

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet?\n"))
		except ValueError:
			print("Value must be integer!")
		else:
			if chips.bet > chips.total:
				print("Sorry you can't bet that many chips because you have:",chips.total)
			else:
				break


def add_chips(chips):
	while True:
		try:
			chips_add = int(input("How many chips would you like to add?\n"))
		except ValueError:
			print("Please enter a integer value")
		else:
			chips.total += chips_add
			break


def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_aces()



def surrender(p_chips):
	G.playing
	
	ans = input("\nSurrender\nYou have a option to surrender do u want to?\n")
	if ans[0].lower() == 'y':
		p_chips.total -= (1/2) * p_chips.bet
		G.playing = False
	else:
		print("Game continues")


def insurance(p_chips):
	if p_chips.total >= (3/2) * p_chips.bet:
		ans = input("\nInsurance\nYou also have a option to insure do u want to?\n")
		if ans[0].lower() == 'y':
			p_chips.insure = True
		elif ans[0].lower() == 'n':
			print("Game continues")


def calc_insure(player_hand,dealer_hand,player_chips):
	if player_chips.insure:
		if dealer_hand.pure:
			player_chips.total += player_chips.bet
		else:
			player_chips.total -=  (1/2) * player_chips.bet


def hit_stand_double(deck,hand,player_chips):
	G.playing

	while True:
		x = input("Would you like to hit,stand or double down?\n")

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print('Player stands. Dealer is playing.')
			G.playing = False
		elif x[0].lower() == 'd':
			if 2*player_chips.bet > player_chips.total:
				print("You can't double you dont have enough money")
				continue
			else:
				hand.add_card(deck.deal())
				hand.adjust_for_aces()
				player_chips.bet += player_chips.bet
				G.playing = False

		else:
			print("Sorry,please try again")
			continue
		break


def show_some(player,dealer):
	print("\nDealer's Hand:")
	print(" <card hidden>")
	print('',dealer.cards[1])  
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
 

def show_all(player,dealer):
	print("\nDealer's Hand:", *dealer.cards, sep='\n ')
	print("Dealer's Hand =",dealer.values)
	print("\nPlayer's Hand:", *player.cards, sep='\n ')
	print("Player's Hand =",player.values)


def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose_bet()


def player_wins(player,dealer,chips):
	print("Player wins!")
	if player.pure:
		chips.bet = (3/2) * chips.bet
	chips.win_bet()


def dealer_busts(player,dealer,chips):
	print("Dealer busts!")
	chips.win_bet()

    
def dealer_wins(player,dealer,chips):
	print("Dealer wins!")
	chips.lose_bet()

    
def push(player,dealer,chips):
	if player.pure:
		if dealer.pure:
			print("Dealer and Player tie! It's a push.")
		else:
			player_wins(player,dealer,chips)
