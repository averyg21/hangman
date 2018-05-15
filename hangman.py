import turtle
from random import randint

#global variables
FINAL_DEF = []
DEFINITIONS = []
BLANKSTRING = []

def fillDefinitions():
	"""Populate the definition lists with dictionary"""
	try:
		with open('dictionary.txt','r',encoding='UTF-8') as file_object:
			for line in file_object:
				DEFINITIONS.append(line)
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
		DIF_LIST = ["dupe","mesmerize","underwrite","pinnacle",
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
		rand_end = len(DIF_LIST) - 1
		randNum = randint(0,rand_end)
		final_word = DIF_LIST[randNum]
	elif(difficulty.lower() == "medium"):
		#input into medium word lists
		DIF_LIST = ["harangue","calumny","prodigal","ambiguous","upbraid",
		"parsimony","impertinent","prevaricate","castigate","betray",
		"venerate","disinterested","laconic","intimate","commensurate",
		"mercurial","maintain","restive","amenable","anomalous","artful",
		"belie","frugal","qualify","undermine","gregarious","involved",
		"demur","amalgam","innocuous","vindicate","ingenuous","wanting",
		"enervate","galvanize","ambivalent","iconoclast","acrimony", "extant",
		"censure","auspicious","chastise","parochial","aberration","amorphous",
		"veracious","equivocal","profligate","egregious"]

		#pick random word based on random number
		#place into finalWord
		rand_end = len(DIF_LIST) - 1
		randNum = randint(0,rand_end)
		final_word = DIF_LIST[randNum]
	else:
		#input into hard word lists
		DIF_LIST = ["jaundiced","cupidity","schadenfreude","blinkered",
		"execrate","malapropism","hedge","tendentious","excoriate","limpid",
		"histrionic"]
		rand_end = len(DIF_LIST) - 1
		randNum = randint(0,rand_end)
		final_word = DIF_LIST[randNum]

	return final_word

def returnDef(word):
	"""Method returns word/definition based on
	dictionary.txt
	"""
	for sentence in DEFINITIONS:
		str1 = sentence
		wordsList = str1.split()
		end = len(wordsList)

		#checks to see if lists is empty
		#skips blank lines
		if not wordsList:
			pass
		else:
			if(word.lower() == wordsList[0].lower()):
				for x in range(1,end):
					FINAL_DEF.append(wordsList[x])
				break
			else:
				continue

	printFinalDeff()

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
			print("\nPlease enter a correct answer.\n")

	return answer

def userAnswer(validWord):
	"""Get answer from user. Let them guess whole word or one
	letter at a time. Also draws body on wrong answer throgh
	counter and drawBody() method
	"""
	counter = 6
	wordLength = len(validWord)
	complete = wordLength
	repeatList = []
	for letter in validWord:
		BLANKSTRING.append("_")
	while True and counter >= 0:
		try:
			#guessing the word
			printFinalWord()
			guessType = int(input("\n1 to guess word, 2 to guess letter," +
			" 3 for definition: "))
			if (guessType == 1):
				ansGuess = input("Guess the word: ")
				if(ansGuess.lower() == validWord.lower()):
					print("\nYou guessed the correct answer!")
					print("Word was: " + validWord + "\n")
					print("Exit the hangman window to" +
					" close the program...")
					break
				else:
					print("Not the answer")
					drawBody(counter)
					counter = counter - 1

			#individually guessing letters
			elif (guessType == 2):
				#initialize list to hold letters & retrive
				#the length of the word, set flag to see if
				#anything was entered into the list
				flag = False

				ansLetter = input("Input ONE letter: ")
				check = len(ansLetter)
				#check to see if your receiving one valid letter
				if (ansLetter.lower() not in repeatList):
					if(check == 1 and ansLetter.isalpha()):
						for x in range(0,wordLength):
							if(ansLetter.lower() == validWord[x]):
								BLANKSTRING[x] = ansLetter.lower()
								complete = complete - 1
								flag = True
								repeatList.append(ansLetter.lower())

						#print message whether right or wrong
						if(flag == False):
							print('\nLetter not in word.')
							drawBody(counter)
							counter = counter - 1
						else:
							print()

						if (complete == 0):
							print("\nYou guessed the word!")
							print("Word was: " + validWord + "\n")
							print("Exit the hangman window to" +
							" close the program...")
							break
					else:
						print("INPUT ONLY ONE VALID LETTER! GUESS TAKEN AWAY!")
						drawBody(counter)
						counter = counter - 1
				else:
					print("Letter already input, guess taken away")
					drawBody(counter)
					counter = counter - 1

			elif(guessType == 3):
				print()
				printFinalDeff()

			else:
				print("Please input a 1 2 or 3.\n")
				continue
		except ValueError:
			print("Please enter a correct NUMBER!\n")

	if(counter < 0):
		print("\nSorry you didn't solve for the word.")
		print("Word was: ", validWord)
		print("Exit the hangman window to close the program...")


def drawOutline():
	"""Initially reset the starting position then draw the outline"""
	frank.hideturtle()
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
	frank.setheading(275)
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


def drawBody(number):
	"""Holds all methods for drawing
	the body. For every wrong answer
	a body part is drawn."""
	if(number == 6):
		drawHead()
	elif(number == 5):
		drawTorso()
	elif(number == 4):
		leftArm()
	elif(number == 3):
		rightArm()
	elif(number == 2):
		leftLeg()
	elif(number == 1):
		rightLeg()
	elif(number == 0):
		drawFace()

def drawTorso():
	frank.setheading(270)
	frank.penup()
	frank.setx(50)
	frank.sety(60)
	frank.pendown()
	frank.forward(100)
	frank.backward(80)

def leftArm():
	frank.setheading(270)
	frank.penup()
	frank.setx(49.99)
	frank.sety(40)
	frank.pendown()
	frank.right(45)
	frank.forward(30)
	frank.penup()
	frank.backward(30)
	frank.pendown()
	frank.left(45)

def rightArm():
	frank.setheading(270)
	frank.penup()
	frank.setx(49.99)
	frank.sety(40)
	frank.pendown()
	frank.left(45)
	frank.forward(30)
	frank.penup()
	frank.backward(30)
	frank.pendown()
	frank.right(45)

def leftLeg():
	"""X is: 49.9, Y is: -39.9"""
	frank.setheading(270)
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
	frank.setheading(270)
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

def drawHead():
	frank.setheading(180)
	frank.circle(20)
	frank.left(90)
	frank.penup()
	frank.forward(40)

def printFinalDeff():
	"""Print definition for user"""
	print("------------------------------------------------" +
	"------------------------------")
	print("DEFINITION: ", *FINAL_DEF)
	print("------------------------------------------------"+
	"------------------------------")

def printFinalWord():
	"""Print word for user"""
	print("------------------------------------------------" +
	"------------------------------")
	print("WORD: ", *BLANKSTRING)
	print("------------------------------------------------"+
	"------------------------------")



#welcome()
fillDefinitions()
answer = promptUser()
word = returnWord(answer)
returnDef(word)
wn = turtle.Screen()		#create turtle screen (window)
frank = turtle.Turtle()		#create turtle to use on window
drawOutline()
userAnswer(word)
wn.mainloop()
