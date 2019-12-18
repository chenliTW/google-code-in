import tkinter as tk

gui=tk.Tk()

announce=None

player1_turn=True

buttons=[i for i in range(9)]

def init():
    gui.title("Tic Tac Toe")
    gui.geometry("600x700")
    gui.configure(background="black")
    # 0 3 6
    # 1 4 7
    # 2 5 8
    global announce
    announce=tk.Label(gui,text="player1 's turn                          ")
    announce.pack()
    announce.place(x=0,y=625)

    global buttons

    buttons=[i for i in range(9)]

    buttons[0]=tk.Button(gui,text="",command=lambda:button_pressed(0),width=15,height=6)
    buttons[1]=tk.Button(gui,text="",command=lambda:button_pressed(1),width=15,height=6)
    buttons[2]=tk.Button(gui,text="",command=lambda:button_pressed(2),width=15,height=6)

    buttons[3]=tk.Button(gui,text="",command=lambda:button_pressed(3),width=15,height=6)
    buttons[4]=tk.Button(gui,text="",command=lambda:button_pressed(4),width=15,height=6)
    buttons[5]=tk.Button(gui,text="",command=lambda:button_pressed(5),width=15,height=6)

    buttons[6]=tk.Button(gui,text="",command=lambda:button_pressed(6),width=15,height=6)
    buttons[7]=tk.Button(gui,text="",command=lambda:button_pressed(7),width=15,height=6)
    buttons[8]=tk.Button(gui,text="",command=lambda:button_pressed(8),width=15,height=6)
    x=0
    y=0
    for i in range(9):
        buttons[i].pack()
        if i%3==0 and i:
            x+=200
        buttons[i].place(x=x,y=y)
        y=(y+200)%600
        tk.Button(gui,text="RESET",command=init).place(x=400,y=625)
def button_pressed(id):
    global player1_turn
    global buttons
    if player1_turn:
        buttons[id].configure(text="O",state='disabled')
    else:
        buttons[id].configure(text="X",state='disabled')
    player1_turn=not player1_turn
    if player1_turn:
        announce.configure(text="player1's turn                          ")
    else:
        announce.configure(text="player2's turn                          ")
    check_win()
def check_win():
    opt=lambda x:1 if x=="O" else 2
    if buttons[0]['text']==buttons[1]['text']==buttons[2]['text'] and len(buttons[2]['text']):
        win(opt(buttons[0]['text']))
    elif buttons[3]['text']==buttons[4]['text']==buttons[5]['text'] and len(buttons[5]['text']):
        win(opt(buttons[3]['text']))
    elif  buttons[6]['text']==buttons[7]['text']==buttons[8]['text'] and len(buttons[8]['text']):
        win(opt(buttons[6]['text']))
    elif buttons[0]['text']==buttons[4]['text']==buttons[8]['text'] and len(buttons[8]['text']):
        win(opt(buttons[0]['text']))
    elif buttons[2]['text']==buttons[4]['text']==buttons[6]['text'] and len(buttons[6]['text']):
        win(opt(buttons[2]['text']))
    elif buttons[0]['text']==buttons[3]['text']==buttons[6]['text'] and len(buttons[6]['text']):
        win(opt(buttons[0]['text']))
    elif buttons[1]['text']==buttons[4]['text']==buttons[7]['text'] and len(buttons[7]['text']):
        win(opt(buttons[1]['text']))
    elif buttons[2]['text']==buttons[5]['text']==buttons[8]['text'] and len(buttons[8]['text']):
        win(opt(buttons[2]['text']))
def win(winner):
    announce.configure(text="!!!!!!PLAYER "+str(winner)+" WINS!!!!!!")
    for i in buttons:
        i.configure(state="disabled")
        
def main():
    init()
    gui.mainloop()

if __name__=="__main__":
    main()