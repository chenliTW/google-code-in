import tkinter as tk
import webbrowser
import os


def open_github():
    webbrowser.open(url="https://github.com/")

def open_myplaylist():
    playlist="/home/chen/文件/GitHub/google-code-in/gui-automate/playlist/playlist.m3u"
    os.system('xdg-open '+playlist)    

def update_computer():
    os.system("sudo apt-get update && sudo apt-get dist-upgrade -y")

def main():
    gui=tk.Tk()
    gui.geometry('500x50')
    gui.title('Python automate')
    button_1=tk.Button(text='Open Github',command=open_github)
    button_1.place(x=0,y=0)
    button_2=tk.Button(text='Play playlist',command=open_myplaylist)
    button_2.place(x=150,y=0)
    button_3=tk.Button(text='update computer',command=update_computer)
    button_3.place(x=300,y=0)
    gui.mainloop()

if __name__=="__main__":
    main()
