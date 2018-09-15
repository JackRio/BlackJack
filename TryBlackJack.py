'''
Game of BlacJack
'''
import random as rand
from Class import Class as C
from Module import Functions as F
from Global import Global as G

# Lets start playing we are done with all the function we need 
print('\n\nWelcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.\n\n')
print("Stand/Hit/Double down/Surrender/Insurnce/Push: Option are available for now")

player_chips = C.Chips()

while True:
	ans = input("You will start with 1000 chips would you like to add more?\n")
	if ans[0].lower() == 'y':
		add_chips(player_chips)
		break
	else:
		ans[0].lower() == 'n'
		break

while G.playing:
	while True:
		if not player_chips.total:
			try:
				ans = input("You don't have any chips,Do you want to add more chips?\n")
			except:
				raise
			else:
				if ans[0].lower() == 'y':
					F.add_chips(player_chips)
					break
				else:
					ans[0].lower() == 'n'
					exit()
		else:
			break

	print("Amount of chips in hand",player_chips.total )
	print("Round commence:\n")
	#Create a deck and shuffle the cards
	deck = C.Deck()
	deck.shuffle()

	player_hand = C.Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())
	if player_hand.values == 21:
		player_hand.pure = True
	
	dealer_hand = C.Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())
	if dealer_hand.values == 21:
		dealer_hand.pure = True

	#Ask for bet
	F.take_bet(player_chips)

	#Show Cards
	F.show_some(player_hand,dealer_hand)

	if 	G.values[dealer_hand.cards[1].rank] == 10 or G.values[dealer_hand.cards[1].rank] == 11 :
		F.surrender(player_chips)

	if dealer_hand.cards[1].rank == 'Ace':
		F.insurance(player_chips)

	if not G.playing:
		G.playing = True
		continue

	while G.playing:  # recall this variable from our hit_or_stand function
        
    	 # Prompt for Player to Hit or Stand
		F.hit_stand_double(deck,player_hand,player_chips)
		F.show_some(player_hand,dealer_hand)
        
		if player_hand.values > 21:
			F.player_busts(player_hand,dealer_hand,player_chips)
			break
    
    # If Player hasn't busted, play Dealer's hand        
	if player_hand.values <= 21:
        
		while dealer_hand.values < 17:
			F.hit(deck,dealer_hand)
            
        # Show all cards
		F.show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
		if dealer_hand.values > 21:
			F.dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.values > player_hand.values:
			F.dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.values < player_hand.values:
			F.player_wins(player_hand,dealer_hand,player_chips)

		else:
			F.push(player_hand,dealer_hand,player_chips)

	F.calc_insure(player_hand,dealer_hand,player_chips)			#Calculate insurance money

    # Inform Player of their chips total    
	print("\nPlayer's winnings stand at",player_chips.total)

	while True:
		# Ask to play again
		try:
			new_game = input("Would you like to play another hand? Enter 'y' or 'n'\n")
		except ValueError :
			print('Enter the value again')
		else:
			break

	if new_game[0].lower()=='y':
		G.playing=True
		continue
	else:
		print("Thanks for playing!")
		break
