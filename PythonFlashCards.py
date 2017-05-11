import random         
import sys
from itertools import islice #imports required tools for program
file = open("painters.txt").read().splitlines()  #loads file and splits lines allowing to create the 'cards'

def ask_question():
	with open('painters.txt') as question_file:
		question_lines = list()
		for line in open('painters.txt'):
			line = line.strip()
			if len(line) > 0:
				question_lines.append(line) #turns lines into questions
		
		for i in range (1):		
			my_questions = random.choice(question_lines)
			
			firstpart, secondpart = my_questions[:len(my_questions)/2], my_questions[len(my_questions)/2:] #splits the lines in half, allowing for questions and answers
			print "\nWhat did this person paint?"
			print firstpart #prints the 'question'
			raw_input() #player types in answer
			print "\nThe Answer is:"
			print secondpart  #prints the 'answer'
		ask_question()  #asks another question, creating an infinte loop
		
		# file = open("painters.txt").read().splitlines()

print "######################################"
print "PYTHON FLASHCARDS:" #just a nice looking title screen
print "ART AND ARCHITECTURE EDITION"
print """
- Press Enter to play
- Press CNTRL-C to quit

By NotedQuotient9
######################################
"""
raw_input()
ask_question() #begins the question loop