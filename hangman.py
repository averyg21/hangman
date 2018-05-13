import turtle
from random import randint

#wn = turtle.Screen()		#create turtle screen (window)
#frank = turtle.Turtle()		#create turtle to use on window
final_def = []
definitions = []
dif_list = []

def fillDefinitions():
	"""Populate the definition lists with dictionary"""
	try:
		with open('dictionary.txt','r',encoding='UTF-8') as file_object:
			for line in file_object:
				definitions.append(line)
	except IOError:
		print("Couldn't open file.")


def returnWord(difficulty):
	"""Method returns randomly generated word from difficulty lists.

	***For later iteration improvements***
	When returning the string after you found word
	slice from 2nd to end so you won't show word too.
	1. Look at inserting into 2D List like: [word,definition]
	2. Checkout tuples if those don't work.

	Method gets a randomNum (one less than list length) and selects word
	Following lines check to see if word is found with flag,
	turn sentence -> string, split the sentence into words lists.
	Checks to see if lists is empty (.txt file spacing), passes if
	it is. Else checks for vocab word in hardDef lists & prints it
	to screen. Also changes flag to false.
	"""

	if(difficulty.lower() == "easy"):
		#input easy words into lists
		dif_list = ["dupe","mesmerize","underwrite","pinnacle",
		"embroiled","profuse","vindictive","censor","unnerve",
		"zenith","summit","thrifty","spendthrift","candid",
		"insolvent","erratic","amiable","indict","indigenous",
		"acme","tender","tirade","dog","remiss","pine","reprobate",
		"inundate","telling","diabolical","macabre","inflammatory",
		"demure","variance","peruse","affable","indignant","slapdash",
		"screed","affluent","thoroughgoing","bleak","stipend","demean",
		"hound","serendipity","miser","telltale","voracious","retiring",
		"err"]

		#pick random word based on random number
		#place into finalWord
		rand_end = len(dif_list) - 1
		randNum = randint(0,rand_end)
		final_word = dif_list[randNum]
	elif(difficulty.lower() == "medium"):
		#input into medium word lists
		print("Medium works")
	else:
		#input into hard word lists
		print("Hard works")

	return final_word

def returnDef(word):
	"""Method returns word/definition based on
	dictionary.txt
	"""
	for sentence in definitions:
		str1 = sentence
		wordsList = str1.split()

		#checks to see if lists is empty
		if not wordsList:
			pass
		else:
			if(word.lower() == wordsList[0].lower()):
				final_def = wordsList[1:]
				print(word, "-", *final_def)
				break
			else:
				continue

def welcome():
	"""Welcome message for the game"""
	print("Welcome to the hangman game.")
	print("If you guess the word before")
	print("the hangman is built, you win!\n")

def promptUser():
	"""Ask the user for difficulty of the word
	& return the correct answer.
	"""
	flag = True

	while(flag == True):
		print("Difficulty levels are: Easy, Medium, & Hard")
		answer = input("Input difficulty: ")

		if(answer.lower() == "easy" or answer.lower() == "e"):
			answer = "easy"
			print("You've answered Easy.\n")
			flag = False
		elif(answer.lower() == "medium" or answer.lower() == "m"):
			answer = "medium"
			print("You've answered Medium.\n")
			flag = False
		elif(answer.lower() == "hard" or answer.lower() == "h"):
			answer = "hard"
			print("You've answered Hard.\n")
			flag = False
		else:
			print("Please enter a correct answer.\n")

	return answer

def drawOutline():
	"""Initially reset the starting position then draw the outline"""
	frank.penup()
	frank.setx(-100)
	frank.sety(-100)
	frank.pendown()
	frank.pensize(1)
	frank.forward(100)
	frank.back(50)
	frank.left(90)
	frank.forward(200)
	frank.right(90)
	frank.forward(100)
	frank.right(180)

def drawFace():
    """start x: 50 & y: 80"""
    frank.penup()
    frank.setx(50)
    frank.sety(80)
    frank.pendown()
    frank.left(135)
    frank.forward(14)
    frank.backward(7)
    frank.left(90)
    frank.forward(7)
    frank.backward(14)
    frank.penup()
    frank.forward(7)
    frank.left(45)
    frank.forward(13)
    frank.left(45)
    frank.pendown()
    frank.forward(7)
    frank.backward(14)
    frank.penup()
    frank.forward(7)
    frank.left(90)
    frank.backward(7)
    frank.pendown()
    frank.forward(14)
    frank.penup()
    frank.right(45)
    frank.forward(10)
    frank.left(90)
    frank.backward(5)
    frank.pendown()
    frank.forward(20)
    frank.penup()


def drawBody():
	frank.circle(20)
	frank.left(90)
	frank.penup()
	frank.forward(40)
	#drawFace()
	drawTorso()
	leftArm()
	rightArm()
	leftLeg()
	rightLeg()
	drawFace()
	frank.penup()
	frank.forward(100)
	wn.mainloop()

def drawTorso():
	frank.pendown()
	frank.forward(100)
	frank.backward(80)

def leftArm():
    frank.right(45)
    frank.forward(30)
    frank.penup()
    frank.backward(30)
    frank.pendown()
    frank.left(45)

def rightArm():
    frank.left(45)
    frank.forward(30)
    frank.penup()
    frank.backward(30)
    frank.pendown()
    frank.right(45)

def leftLeg():
    """X is: 49.9, Y is: -39.9"""
    frank.penup()
    frank.setx(49.9)
    frank.sety(-39.9)
    frank.pendown()
    frank.right(45)
    frank.forward(45)
    frank.penup()
    frank.backward(45)
    frank.pendown()
    frank.left(45)

def rightLeg():
    """X is: 49.9, Y is: -39.9"""
    frank.penup()
    frank.setx(49.9)
    frank.sety(-39.9)
    frank.pendown()
    frank.left(45)
    frank.forward(45)
    frank.penup()
    frank.backward(45)
    frank.pendown()
    frank.right(45)

welcome()
fillDefinitions()
answer = promptUser()
word = returnWord(answer)
returnDef(word)
#drawOutline()
#drawBody()
#randWord()
#returnWord()
