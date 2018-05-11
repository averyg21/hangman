import turtle

#wn = turtle.Screen()		#create turtle screen (window)
#frank = turtle.Turtle()		#create turtle to use on window

def returnWord():
	"""Return the word that you're looking for"""
	#may need to put utf coding for windows
	myFile = open("dictionary.txt","r", encoding="UTF-8")
	xs = myFile.read()
	#split file into sentences
	sentences = xs.split('\n')
	flag = True
	x = 0
	while(flag == True):
		if(x > 15):
			break
		#individual = sentences.pop(0)
		print(sentences[x])
		#print("Last sentence is: ", individual)
		x = x + 1
	#for sentence in sentences:
	#	print(sentence)
	myFile.close()
	#print(words)
	#print(xs)

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

	return answer.lower()

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
answer = promptUser()
#drawOutline()
#drawBody()
#randWord()
#returnWord()
