#Import random library
import random

#Array declaration
user_choice = []
users = []
choice = []
stacks = []
users2 = []
colour = []
colourend = []

#Array declaration for colours
colours = ['p', 'o', 'b', 'y', 'g', 'r', 'w']

#Declaration of integers
wro_pos = 0
cor_pos = 0
ct = 0
atp = 0

#Generation of 4 random colours from 'colours' list
def random_generator():
  for x in range(4):
    gen =(random.choice(colours))
    choice.append(gen)
    print(choice)

#Colour input from the user
def user_input():
  x = 0
  i = 1
  while x < 4:
    print("")
    user_choice = str(input("                          Enter no. %s colour letter: " %(i))).lower()
    if (user_choice == 'p') or (user_choice == 'o') or (user_choice == 'b') or (user_choice == 'y') or (user_choice == 'g') or (user_choice == 'r') or (user_choice == 'w'):
      users.append(user_choice)
      x += 1
      i += 1
    else:
      print("")
      print ("                        |Please enter a valid letter.|")

#Function for random colour generator
random_generator()

#User Interface
print("")
print("")
print ("================================================================================")
print ("                              THE MASTERMIND GAME")
print ("--------------------------------------------------------------------------------")
print ("Game Rules: ")
print ("1. Select 4 colours from the digits displayed. (e.g. 2, 4, 5, 4)")
print ("2. To end the game, you need all answers of correct colours in same positions.")
print ("3. The goal of the game is to attempt the number of times as little as possible!")
print("")
print ("                            Good luck and have fun!")
print ("--------------------------------------------------------------------------------")
while True:
  #Colour selection interface
  print ("                          The choices of colours are: ")
  print("")
  print ("                                  P - Pink")
  print ("                                  O - Orange")
  print ("                                  B - Blue")
  print ("                                  Y - Yellow")
  print ("                                  G - Green")
  print ("                                  R - Red")
  print ("                                  W - White")
  print ("           (Please enter the colours in the letters as shown above)")
  print ("                    (Can be in capital or lowercase form)")
  print("")

  #function's header is placed here
  user_input()

  #Do display users colour input
  for e in range(4):
    if users[e] == 'p':
      colourin = 'Pink'
      colourend.append(colourin)
    elif users[e] == 'o':
      colourin = 'Orange'
      colourend.append(colourin)
    elif users[e] == 'b':
      colourin = 'Blue'
      colourend.append(colourin)
    elif users[e] == 'y':
      colourin = 'Yellow'
      colourend.append(colourin)
    elif users[e] == 'g':
      colourin = 'Green'
      colourend.append(colourin)
    elif users[e] == 'r':
      colourin = 'Red'
      colourend.append(colourin)
    elif users[e] == 'w':
      colourin = 'White'
      colourend.append(colourin)
  print("")
  print("  The colours you have selected are: " , colourend)

  #Correct colour in correct position & in wrong position decision
  for x in range(4):
    if users[x] == choice[x]:
      cor_pos += 1
    else:
      users2.append(users[x])
      stacks.append(choice[x])
      
  y = 0
  while y < len(users2):
    z = 0
    while z < len(stacks):
      if users2[y] == stacks[z]:
        stacks.pop(z)
        wro_pos += 1
        break
      else:
        z += 1
    y += 1

  #if-else statement to determine the win-continue situation of the game
  if cor_pos == 4:
    atp += 1
    print("")
    print("")
    print ("--------------------------------------------------------------------------------")
    print ("Correct colour in correct placement: " , cor_pos)
    print ("Correct colour but in wrong placement: " , wro_pos)
    print ("--------------------------------------------------------------------------------")
    print ("     You have attempted the game %s times and have now become a mastermind!" % (atp))
    print ("                  Thank you for playing THE MASTERMIND GAME!")
    print ("                              Developed by Shaun")
    break
  else:
    atp += 1
    print("")
    print("")
    print ("--------------------------------------------------------------------------------")
    print ("Correct colour in correct placement: " , cor_pos)
    print ("Correct colour but in wrong placement: " , wro_pos)
    print ("--------------------------------------------------------------------------------")
    wro_pos = 0
    cor_pos = 0
    users.clear()
    users2.clear()
    stacks.clear()
    colourend.clear()
    continue

