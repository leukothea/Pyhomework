"""
Python Certificate: Fall-Winter 2013 Term
Final Project
Iteration 0.01
Catherine Warren

"""

# -- Data -- #
# declare variables and constants. 

import random

# My dictionary will go here. There are 25 cards, each with 4 meanings. It makes the most sense to code
# each picture with the picture name, plus a number to mark the key, and then the desired meaning 
# as its paired value. 

Meaning = {"Rose1" : "Some meaning", 
"Rose2" : "Another meaning", 
"Rose3" : "Yet another meaning", 
"Rose4" : "You guessed it, another meaning!", 
"Bread1" : "And so on",
"Bread2" : "And so forth", 
"Bread3" : "Et cetera", 
"Bread4" : "kai ta alla"}

class Card(object):
	# to hold the 25 cards 
	# Each card is denoted by a letter, to make later comparison between cards easier (we will need to determine
	# which card comes "first"). 
	# Tuple values are entered on each card in order from lowest number going clockwise around the card.
	a = ("Rose", "Bread", "Demons", "Fish")
	b = ("House", "Birds", "Fish", "Ring")
	c = ("Rose", "Demons", "House", "Letter")
	d = ("Bear", "Letter", "Ring", "Bread")

	# def __getitem__(Card):
	# maybe getitem will be useful: operator.__getitem__(a, b) - Return the value of a at index b.
	# Standard operators as functions: http://docs.python.org/2/library/operator.html#operator.getitem



def PictureMeaning(numberofcards):
# right now this is just to return a random single-picture reading so I know that part works
	for name, meaning in random.sample(Meaning.items(), numberofcards):
		print ("{lhs} : {rhs}".format(lhs=name, rhs=meaning))

			
# -- Processing -- #


print PictureMeaning(1)

