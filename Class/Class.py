
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from Global import Global as G
import random as rand

#Class Defination

class Card:										#Card defination
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' of ' +self.suit


class Deck:										#Deck formation
	def __init__(self):
		self.deck = []							#Start with empty deck
		for suit in G.suits:
			for rank in G.ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''  						#Start with empty string
		for card in self.deck:
			deck_comp += '\n ' +card.__str__() 	#add
		return 'The deck has: ' + deck_comp

	def shuffle(self):
		rand.shuffle(self.deck)

	def deal(self):								#To deal a card
		single_card = self.deck.pop()
		return single_card


class Hand:
	def __init__(self):
		self.cards = []							#Number of cards a player has
		self.values = 0							#Value of the cards
		self.aces = 0							# Aces to calculate hand value to maximum
		self.pure = False
	def add_card(self,card):
		self.cards.append(card)
		self.values += G.values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1						#Adding aces to the hand

	def adjust_for_aces(self):
		while self.values > 21 and self.aces:
			self.values -= 10
			self.aces -= 1



class Chips:									#Chips winning and losing function
	def __init__(self,total = 1000):
		self.total = total
		self.bet = 0
		self.insure = False

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet