from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text = (players[1] + " turn"))
            elif check_winner() is True:
                label.config(text = (players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text = ("Tie!!"))

        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text = (players[0] + " turn"))
            elif check_winner() is True:
                label.config(text = (players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text = ("Tie!!"))

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
        

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    elif empty_spaces() is False:
        return "Tie"

def empty_spaces():
    pass

def new_game():
    pass


window = Tk()
window.title("Tic-Tac-Toe")

window.resizable(False, False)
window_height = 500
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
label = Label(text = player + "turn")
label.pack(side = "top")

reset_button = Button(text = "Restart", command = new_game)
reset_button.place(x = 50, y = 400)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", width = 5, height = 2,
                                      command = lambda row = row, column = column: next_turn(row, column))
        buttons[row][column].grid( row = row, column = column)

window.mainloop()

#https://www.youtube.com/watch?v=V9MbQ2Xl4CE