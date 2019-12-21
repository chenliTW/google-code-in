import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from io import BytesIO

def scrap():
    res=requests.get("https://codeforces.com/api/user.info?handles="+username.get()).json()
    if res["status"]=='OK':
        res=res["result"][0]
        print(res)
        handle.configure(text="Handle : "+res["handle"])
        current_rating.configure(text="Current Rating : "+str(res["rating"]))
        rank.configure(text="Rank : "+res["rank"])
        max_rating.configure(text="Max Rating : "+str(res["maxRating"]))
        max_rank.configure(text="Max Rank : "+res["maxRank"])
        img_url="https:"+res["avatar"]
        real_image=Image.open(BytesIO(requests.get(img_url).content))
        #real_image.show()
        img = ImageTk.PhotoImage(real_image)
        img_label = tk.Label(gui,image=img)
        img_label.image=img
        img_label.place(x=0,y=240)
    else:
        messagebox.showinfo(title='Error', message='User not Found!!!!')

gui=tk.Tk()
username=tk.StringVar()
gui.title("codeforce_scrapper")
gui.geometry("520x350")
tk.Label(gui,text="input username : ").place(x=0,y=1)
username_entry=tk.Entry(gui,textvariable=username)
username_entry.pack()
username_entry.place(x=170,y=1)
scrap_button=tk.Button(gui,text="scrap!!!",command=scrap)
scrap_button.pack()
scrap_button.place(x=400,y=1)
handle=tk.Label(gui,text="Handle : ")
handle.pack()
handle.place(x=0,y=80)
current_rating=tk.Label(gui,text="Current Rating : ")
current_rating.pack()
current_rating.place(x=0,y=110)
rank=tk.Label(gui,text="Rank : ")
rank.pack()
rank.place(x=0,y=140)
max_rating=tk.Label(gui,text="Max Rating : ")
max_rating.pack()
max_rating.place(x=0,y=170)
max_rank=tk.Label(gui,text="Max Rank : ")
max_rank.pack()
max_rank.place(x=0,y=200)

def main():
    gui.mainloop()
    
if __name__=="__main__":
    main()