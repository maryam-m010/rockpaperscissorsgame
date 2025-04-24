from tkinter import *
import random
import tkinter.font as font

root = Tk()
root.title("rock paper scissors game")
appfont = font.Font(size = 12)

options  = [("rock", 0), ("paper", 1), ("scissors", 2)]

computer_score = 0
player_score = 0

def computer_choice():
    return random.choice(options)

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    gamestart.config(text = "Computer Wins!")
    g.config(text = "Computer Score:" + str(computer_score))
    e.config(text = "Player Score:" + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    gamestart.config(text = "You Win!")
    g.config(text = "Computer Score:" + str(computer_score))
    e.config(text = "Player Score:" + str(player_score))

def tie_func():
    global computer_score, player_score
    gamestart.config(text = "Its a draw!")
    g.config(text = "Computer Score:" + str(computer_score))
    e.config(text = "Player Score:" + str(player_score))

def playerchoice(player_input):
    computer_input = computer_choice()
    print(player_input)
    print(computer_input)
    d.config(text = "You Selected:" + player_input[0])
    f.config(text = "Computer Selected:" + computer_input[0])
    
    if(player_input == computer_input):
        tie_func()
    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_wins()
        elif(computer_input[1] == 2):
            player_wins()

    elif(player_input[1] == 1):
        if(computer_input[1] == 2):
            computer_wins()
        elif(computer_input[1] == 0):
            player_wins()

    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
        elif(computer_input[1] == 1):
            player_wins()


gametitle = Label(root, text = "Rock Paper Scissors!", font = font.Font(size = 20), fg = "grey")
gametitle.pack()

gamestart = Label(root, text = "Lets Start the Game!", font = font.Font(size = 16), fg = "black")
gamestart.pack()

a = Frame(root)
a.pack()

b = Label(a, text = "Your Options:", font = appfont, fg = "grey")
b.grid(row = 0, column = 0)

rock = Button(a, text = "Rock", width = 15, bg = "powder blue", command = lambda: playerchoice(options[0]))
rock.grid(row = 1, column = 1, padx = 25)

paper = Button(a, text = "Paper", width = 15, bg = "medium aquamarine", command = lambda: playerchoice(options[1]))
paper.grid(row = 1, column = 2, padx = 25)

scissors = Button(a, text = "Scissors", width = 15, bg = "salmon", command = lambda: playerchoice(options[2]))
scissors.grid(row = 1, column = 3, padx = 25)

c = Label(a, text = "Score:", font = appfont, fg = "grey")
c.grid(row = 2, column = 0)

d = Label(a, text = "You Selected:", font = appfont, fg = "black")
d.grid(row = 3, column = 1)

e = Label(a, text = "Your Score:", font = appfont, fg = "black")
e.grid(row = 3, column = 2)

f = Label(a, text = "Computer Selected:", font = appfont, fg = "black")
f.grid(row = 4, column = 1)

g = Label(a, text = "Computer Score:", font = appfont, fg = "black")
g.grid(row = 4, column = 2)
root.mainloop()
