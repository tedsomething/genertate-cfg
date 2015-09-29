#!/usr/bin/python
import os


max_length = 8 # maximum length of a word (words can be < or == )
words = [] # store all words
productions = {	# production rules
	"E": ("E+E", "E*E", "(E)", "xI"), 
	"I": ("0I", "1I", "0", "1")
}

terminals = ['0', '1', 'x', '+', '*', '(', ')']


# generate all possible strings
def generate(symbols):
	global productions
	global words

	# discard strings that are too long
	if len(symbols) > max_length: return 

	# add new words
	if is_word(symbols) and not old_word(symbols): words.append(symbols)

	for i in range(0, len(symbols)):
		
		# skip terminal simbols (since nothing to replace)
		if is_terminal(symbols[i]): continue

		for j in productions:

			if symbols[i] == j: 
				for k in range(0, len(productions[j])):

					temp = symbols[0:i] + productions[j][k] + symbols[i+1: len(symbols)]
					generate(temp)


# checks if symbol is terminal or non-terminal
def is_terminal(symbol):
	global terminals

	for i in range(0, len(terminals)):
		if terminals[i] == symbol: return 1

	return 0


# checks if word already was generated somewhere in past
def old_word(symbols):
	for i in range(0, len(words)):
		if symbols == words[i]: return 1

	return 0


# checks if string of simbols is word (e.g. consists only of terminal symbols)
def is_word(symbols):
	for i in range(0, len(symbols)):
		if not is_terminal(symbols[i]): return 0

	return 1


# prints array of all words
def print_words():
	global words

	print(words)


# print total words generated
def print_total():
	global words

	print(len(words))


# UI
max_length = int(raw_input("Please enter maximum length of a word:\n"))
print "Generating ..."

generate("E")
print_words()
print_total()

