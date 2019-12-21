import tkinter as tk

def init():
    gui.title("2048")
    gui.geometry("800x700")
    gui.configure(background="gray")

    tk.Label(gui,width=13,height=4).place(x=0,y=0)
    tk.Label(gui,width=3,height=1).place(x=200,y=0)
    tk.Label(gui,width=3,height=1).place(x=400,y=0)
    tk.Label(gui,width=3,height=1).place(x=600,y=0)
    tk.Label(gui,width=3,height=1).place(x=0,y=150)
    tk.Label(gui,width=3,height=1).place(x=150,y=150)
    tk.Label(gui,width=3,height=1).place(x=300,y=150)
    tk.Label(gui,width=3,height=1).place(x=450,y=150)
    tk.Label(gui,width=3,height=1).place(x=0,y=300)
    tk.Label(gui,width=3,height=1).place(x=150,y=300)
    tk.Label(gui,width=3,height=1).place(x=300,y=300)
    tk.Label(gui,width=3,height=1).place(x=450,y=300)
    tk.Label(gui,width=3,height=1).place(x=0,y=450)
    tk.Label(gui,width=3,height=1).place(x=150,y=450)
    tk.Label(gui,width=3,height=1).place(x=300,y=450)
    tk.Label(gui,width=3,height=1).place(x=450,y=450)





if __name__=="__main__":
    gui=tk.Tk()
    init()
    gui.mainloop()