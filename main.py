from tkinter import *


check = [''] * 9
def stop_game():
    global check
    for i in range(9):
        buttons[i].config(state='disabled')
player = 1
def click(index):
    global check
    global player
    if (player == 1):
        buttons[index].config(text='X',state='disabled')
        check[index] = 'X'
        player = 2
        if check_win('X') == True:
            label.config(text='Игрок № 1 победил!')
            stop_game()
    elif player == 2:
        buttons[index].config(text='O',state='disabled')
        check[index] = 'O'
        player = 1
        if check_win('O') == True:
            label.config(text='Игрок № 2 победил!')
            stop_game()

    
game = Tk()
game.title('Крестики - нолики')
label = Label(game,text='Игра крестики-нолики',font=('Arial',20,'bold'))
label.grid(row=0,column=0,columnspan=3)
buttons = [Button(game, text = '', width=7, height=5,font=('Arial',20), command=lambda x=i: click(x)) for i in range(9)]
row = 1
col = 0
for j in range(9):
    buttons[j].grid(row=row,column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

def check_win(str):
    win = False
    if ((str == check[0] and str == check[1] and str == check[2]) or 
        (str == check[3] and str == check[4] and str == check[5]) or 
        (str == check[6] and str == check[7] and str == check[8]) or 
        (str == check[0] and str == check[3] and str == check[6]) or 
        (str == check[1] and str == check[4] and str == check[7]) or 
        (str == check[2] and str == check[5] and str == check[8]) or 
        (str == check[0] and str == check[4] and str == check[8]) or 
        (str == check[2] and str == check[4] and str == check[6])):
        win = True
        return win


game.mainloop()