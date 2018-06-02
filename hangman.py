######################Imports###################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from random import randint
import turtle
import atexit
import sys
######################Imports###################################

####################Global Variables############################
USER_WINDOW = tk.Tk()			#GUI used for user interaction
FINAL_DEF = []					#holds the final definition
DEFINITIONS = []				#holds ALL definitions (.txt file)
LETTER_ANS = StringVar()		#User letter answer to check
WORD_ANS = StringVar()			#User word answer to check
DIFFICULTY = ""					#holds user's difficulty for the round
ANS_FLAG = False				#checks if user selected difficulty
GAME_OVER = False               #checks if user guessed or lost
wordLabel = tk.Label()          #change word label text on buttonCLick
defLabel = tk.Message()         #change def label text on buttonClik
WORD = ""                       #holds word to be guessed
BLANK_WORD = []                 #holds blanks string that will change throughout
OUTPUTWORD = ""                 #word output based on blank_word[] changing
CHANCE_COUNTER = 7              #counts the chances user has left to solve
REPEAT_LIST = []                #checks if letter has already been used
LETTER_COUNT = 0                #compare to word length if equal, word was guessed
frank = turtle.Turtle()         #create turtle to move
#####################Global Variables############################


################Code for tkinter window###########################

def createWindow(window):
    '''Function creates gui window that user interacts with
    Widgets are grouped by frames (top,middle,bottom).
    wordLabel & defLabel are global so other methods can adjust'''
    global wordLabel, defLabel

    window.title("Hangman App")
    window.geometry('800x500+0+0')
    window.resizable(0,0)

    topFrame = tk.Frame(window,width=800,height=150)
    middleFrame = tk.Frame(window,width=800,height=200)
    bottomFrame = tk.Frame(window,width=800,height=150)


    window.grid_rowconfigure(1,weight=0)
    window.grid_columnconfigure(0,weight=0)

    topFrame.grid(row=0)
    middleFrame.grid(row=5)
    bottomFrame.grid(row=10)


    #left side labels
    label1 = ttk.Label(topFrame,text="Letter Guess: ")
    label2 = ttk.Label(topFrame,text="Word Guess: ")

    #middle labels
    label3 = ttk.Label(middleFrame,text="Word:")
    wordLabel = tk.Label(middleFrame,relief="solid")
    label4 = ttk.Label(middleFrame,text="Definition:")
    defLabel = tk.Message(middleFrame,relief="solid")

    #set entry
    letterBox = ttk.Entry(topFrame,textvariable=LETTER_ANS)
    wordBox = ttk.Entry(topFrame,textvariable=WORD_ANS)

    #right side buttons
    letterButton = tk.Button(topFrame,text="Guess Letter",
	command=guessLetterClick)
    wordButton = tk.Button(topFrame,text="Guess Word",
	command=guessWordClick)

    #Bottom buttons
    helpButton = tk.Button(bottomFrame,text="Help",command=helpClick)
    easyButton = tk.Button(bottomFrame,text="Easy",command=easyClick)
    medButton = tk.Button(bottomFrame,text="Medium",command=medClick)
    hardButton = tk.Button(bottomFrame,text="Hard",command=hardClick)
    closeButton = tk.Button(bottomFrame,text="Close",command=closeProg)


    #changing the font
    label1.config(font=44)
    label2.config(font=44)

    label3.config(font=33)
    label4.config(font=33)
    wordLabel.config(width=50,height=5,font=44)
    defLabel.config(font=44,width=500)


    label1.grid(row=0,column=0,pady=20)
    label2.grid(row=1,column=0)

    label3.grid(row=5,column=0)
    wordLabel.grid(row=5,columnspan=13,column=1,pady=20,padx=20)
    label4.grid(row=6,column=0)
    defLabel.grid(row=6,columnspan=13,column=1)

    letterBox.grid(row=0,column=1)
    wordBox.grid(row=1,column=1)

    letterButton.grid(row=0,column=2)
    wordButton.grid(row=1,column=2)


    helpButton.grid(row=10,column=0,pady=20,padx=20)
    easyButton.grid(row=10,column=1)
    medButton.grid(row=10,column=2)
    hardButton.grid(row=10,column=3)
    closeButton.grid(row=10,column=4,pady=20,padx=20)

    helpButton.config(height=2, width=7)
    closeButton.config(height=2,width=7)
    easyButton.config(height=2, width=7,bg="green")
    medButton.config(height=2,width=7,bg="yellow")
    hardButton.config(height=2,width=7,bg="red")

    #make user exit with close button
    window.protocol('WM_DELETE_WINDOW',closeMessage)
    window.deiconify()
    wn = turtle.Screen()
    drawOutline()

    window.mainloop()

#########################TKINTER code end########################

def helpClick():
    '''outputs help messages to the user'''
    messagebox.showinfo("Help","Adjust blank window if you cannot" +
    " see the hangman.")
    messagebox.showinfo("Help","Click easy, medium, or hard" +
    " for difficulty.")
    messagebox.showinfo("Help","Input a single letter, or a word" +
    " in the correct boxes.")
    messagebox.showinfo("Help","Hangman will draw on every" +
    " wrong answer.")
    messagebox.showinfo("Help","If hangman is completed, you lose!")

def closeProg():
	'''Closes program when user clicks the close button'''
	sys.exit(0)

def easyClick():
    '''Places easy into difficulty level. Calls fillDefinitions().
    Returns a randomly generated word from returnWord(). Prints
    definition and "blank" word to the screen.
    '''
    global ANS_FLAG, DIFFICULTY, WORD, OUTPUTWORD
    if (ANS_FLAG == False):
        ANS_FLAG = True
        DIFFICULTY = "easy"
        messagebox.showinfo("","Difficulty is: " + DIFFICULTY.upper())
        fillDefinitions()
        WORD = returnWord(DIFFICULTY)
        returnDef(WORD)
        initialBlankWord()
        wordLabel.config(text=OUTPUTWORD)
        defLabel.config(text=FINAL_DEF)

def medClick():
    '''Places medium into difficulty level. Calls fillDefinitions().
    Returns a randomly generated word from returnWord(). Prints
    definition and "blank" word to the screen.
    '''
    global ANS_FLAG, DIFFICULTY, WORD, OUTPUTWORD
    if (ANS_FLAG == False):
        ANS_FLAG = True
        DIFFICULTY = "medium"
        messagebox.showinfo("","Difficulty is: " + DIFFICULTY.upper())
        fillDefinitions()
        WORD = returnWord(DIFFICULTY)
        returnDef(WORD)
        initialBlankWord()
        wordLabel.config(text=OUTPUTWORD)
        defLabel.config(text=FINAL_DEF)

def hardClick():
    '''Places hard into difficulty level. Calls fillDefinitions().
    Returns a randomly generated word from returnWord(). Prints
    definition and "blank" word to the screen.
    '''
    global ANS_FLAG, DIFFICULTY, WORD, OUTPUTWORD
    if (ANS_FLAG == False):
        ANS_FLAG = True
        DIFFICULTY = "hard"
        messagebox.showinfo("","Difficulty is: " + DIFFICULTY.upper())
        fillDefinitions()
        WORD = returnWord(DIFFICULTY)
        returnDef(WORD)
        initialBlankWord()
        wordLabel.config(text=OUTPUTWORD)
        defLabel.config(text=FINAL_DEF)

def initialBlankWord():
    '''Populates the blank word list based on
    the randomly generated word. Returns word with
    dashes and spaces.'''
    global WORD, BLANK_WORD, OUTPUTWORD, wordLabel
    for x in WORD:
        BLANK_WORD.append("- ")
    OUTPUTWORD = ''.join(BLANK_WORD)

def checkLetter(guess):
    '''Function checks the complete list for the
    inputted letter. If it's in then blank_word list will
    populate. If not a limb will be drawn. Repeats will be
    considered a wrong answer. & limb will be drawn'''
    global WORD, BLANK_WORD, LETTER_COUNT, GAME_OVER, REPEAT_LIST
    word_length = len(WORD)
    flag = False
    skip = False

    for letter in REPEAT_LIST:
        if(guess.lower() == letter):
            skip = True
            break

    for i in range(0,word_length):
        if(guess.lower() == WORD[i].lower() and skip == False):
            flag = True
            REPEAT_LIST.append(guess.lower())
            BLANK_WORD[i] = guess.lower() + " "
            LETTER_COUNT = LETTER_COUNT + 1
            if(LETTER_COUNT == word_length):
                GAME_OVER = True
                messagebox.showinfo("Won!","You got the word!")

    OUTPUTWORD = ''.join(BLANK_WORD)
    wordLabel.config(text=OUTPUTWORD)
    checkComplete()

    if(skip == True):
        messagebox.showinfo("","Letter already entered.")
        drawBody(CHANCE_COUNTER)
        subtractChances()
        checkChances()
    else:
        if(flag == False):
            messagebox.showinfo("","Letter not in word!")
            drawBody(CHANCE_COUNTER)
            subtractChances()
            checkChances()

def checkWord(guess):
    '''Take word input and compare it to
    the real word. If correct user wins,
    if not body part will be drawn on hangman.
    '''
    global WORD, wordLabel, GAME_OVER
    isWord = True
    wordLength = len(WORD)
    if(len(guess) == wordLength):
        for i in range(0,wordLength):
            if (guess[i].lower() != WORD[i].lower()):
                isWord = False
                messagebox.showinfo("","Word guessed is not correct.")
                drawBody(CHANCE_COUNTER)
                subtractChances()
                checkChances()
                break
    else:
        messagebox.showinfo("","Word guessed is not correct.")
        drawBody(CHANCE_COUNTER)
        subtractChances()
        checkChances()
        isWord = False

    if(isWord == True):
        messagebox.showinfo("Correct","You got the correct word!")
        wordLabel.config(text=WORD.upper())
        GAME_OVER = True

def checkComplete():
    '''If game is finished output winning message'''
    global GAME_OVER
    if(GAME_OVER == True):
        messagebox.showinfo("You Won!","The word was: " +
        WORD.upper() + "!")

def checkChances():
    '''Check if chances are 0. If they are then
    game is over'''
    global GAME_OVER, CHANCE_COUNTER, WORD
    if(CHANCE_COUNTER == 0):
        GAME_OVER = True
        messagebox.showinfo("Lost","You lost, word was: "
        + WORD.upper() + "!")
        wordLabel.config(text=WORD)

def subtractChances():
    '''subtract one from chances.'''
    global CHANCE_COUNTER
    CHANCE_COUNTER = CHANCE_COUNTER - 1

def guessLetterClick():
    '''Take the user's letter guess. Checks if
    difficulty has been set & validates letter. If so,
    the method will send letter to checkLetter()
    to check if its in the word.
    '''
    global ANS_FLAG, CHANCE_COUNTER
    if(GAME_OVER == False):
        if(ANS_FLAG == True):
            letter = LETTER_ANS.get()

            if(len(letter) == 1 and letter.isalpha()):
                checkLetter(letter)
            else:
                messagebox.showinfo("","Input a SINGLE LETTER!")
                drawBody(CHANCE_COUNTER)
                subtractChances()
                checkChances()
        else:
            messagebox.showinfo("","Select a difficulty!")
    else:
        messagebox.showinfo("Complete","The game is over!")

def guessWordClick():
    '''Take the users word guess. Checks if
    difficulty has been set. If so then method will
    compare input word to actual word.'''
    global ANS_FLAG, GAME_OVER
    if(GAME_OVER == False):
    	if(ANS_FLAG == True):
            word = WORD_ANS.get()
            if(word.isalpha()):
                checkWord(word)
            else:
                messagebox.showinfo("","Word can only contain LETTERS!")
                drawBody(CHANCE_COUNTER)
                subtractChances()
                checkChances()
    	else:
    		messagebox.showinfo("","Select a difficulty!")
    else:
        messagebox.showinfo("Complete","The game is over!")


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
		"histrionic","benighted","arch","phantasmagorical","disabuse",
		"gerrymander","jejune","mulct","sartorial","pollyannaish","apotheosis",
		"sybarite","venial","sangfroid","bilious","propitiate"]
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

	#printFinalDeff()

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
	if(number == 7):
		drawHead()
	elif(number == 6):
		drawTorso()
	elif(number == 5):
		leftArm()
	elif(number == 4):
		rightArm()
	elif(number == 3):
		leftLeg()
	elif(number == 2):
		rightLeg()
	elif(number == 1):
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

def closeMessage():
    '''Use the close button to close'''
    messagebox.showinfo("Exit","Use close button to exit program.")

createWindow(USER_WINDOW)
