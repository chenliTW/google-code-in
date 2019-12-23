import tkinter as tk
from tkinter import messagebox

problem_list=[
{"question":"find the value of x:\nx=4+5x","answer":["5","-1","3","None of the above"],"correct_answer":"B","point":1},
{"question":"find the value of x:\n{x + 3y = 6\n{3x + y - 2 = 0","answer":["1/sin(60°)","1/sin(30°)","1/cos(30°)","1/cos(60°)"],"correct_answer":"D","point":3},
{"question":"what is the shortest distance\nbetween (1,3,5) and (-2,-1,5)?\n","answer":["5","3√3","√5","√11"],"correct_answer":"A","point":2},
{"question":"what is the shortest distance \n form line 3x+4y+5=0 to (1,3)","answer":["6","2","4","None of the above"],"correct_answer":"C","point":4},
{"question":"what equals to log(2)+log(5)","answer":["0","1","2","1/2"],"correct_answer":"B","point":2},
{"question":"what is the root of \nx^3-x^2+4x-4=0:(i=√-1)\n","answer":["2","i","-i","-2i"],"correct_answer":"D","point":2},
{"question":"50°≦∠A<∠B≦60° \nchose the correct answer","answer":["sin∠A<sin∠B","cos∠A<cos∠B","sin∠C<cos∠C","∠A>∠B"],"correct_answer":"A","point":4},
{"question":"1+1=?","answer":["cos(π)","log(π)","π","2"],"correct_answer":"D","point":1},
{"question":"4x-3y= 50\n what the min value of x^2 +y^2?","answer":["50","100","150","None of the above"],"correct_answer":"B","point":5},
{"question":"x=?,y=? when the min value of\n x^2 +y^2 equals 100","answer":["(7,-1)","(3,4)","(8,-6)","None of the above"],"correct_answer":"C","point":10}
]

gui=None
inp=None
current_level=0
group_num=int(0)
group_checkbox=list()
group_stat=dict()
level_label=None
question_label=None
answer_label=None

def end_setup():
    global group_num
    group_num=int(inp.get())
    gui.destroy()
    main()

def setup():
    global gui
    gui=tk.Tk()
    gui.title("game setup")
    gui.geometry("520x200")
    tk.Label(text="Please enter group count(value between 1~4):").place(x=0,y=0)
    global inp
    inp=tk.Entry(gui)
    inp.place(x=150,y=40)
    tk.Button(text="Start the game!!!",command=end_setup).place(x=165,y=90)
    gui.mainloop()

def end_game():
    output="result:\n"
    for i in range(group_num):
        output+=("group "+str(1+i)+" : "+str(group_stat[i]["point"])+" pt(s)"+"\n")
    messagebox.showinfo("Game ended!!!",output)
    exit(0)

def answered():
    global level_label,question_label,answer_label,group_stat,group_checkbox,current_level
    print("some one answered\n next level")
    current_level+=1
    if current_level==len(problem_list):
        end_game()
    level_label.configure(text="Level "+str(current_level+1)+" ["+str(problem_list[current_level]["point"])+"pt(s)]")
    question_label.configure(text=problem_list[current_level]["question"])
    answer_choice_str="A){}    B){}  C){}    D){}".format(problem_list[current_level]["answer"][0],problem_list[current_level]["answer"][1],problem_list[current_level]["answer"][2],problem_list[current_level]["answer"][3])
    answer_label.configure(text=answer_choice_str)
    for i in range(group_num):
        group_checkbox[i].set(0)
        group_stat[i]["answered"]=False

def submit():
    chk=sum([i.get() for i in group_checkbox])
    if chk!=1:
        messagebox.showwarning("Error","Please select a group or only select a group!!!")
    else:
        group=0
        for i in range(group_num):
            if group_checkbox[i].get()==1:
                group=i
        global group_stat
        if group_stat[group]["answered"]==True:
            messagebox.showwarning("Error","group "+str(group+1)+" has already answered")
        else:
            group_stat[group]["answered"]=True
            if inp.get()==problem_list[current_level]["correct_answer"]:
                group_stat[group]["point"]+=problem_list[current_level]["point"]
                print("group "+str(group)+" correct")
            answered()

def main():
    global gui
    gui=tk.Tk()
    gui.title("Math game")
    gui.geometry("700x400")
    global level_label
    level_label=tk.Label(text="Level "+str(current_level+1)+" ["+str(problem_list[current_level]["point"])+"pt(s)]",font=("Courier", 20))
    level_label.place(x=160,y=0)
    global question_label
    question_label=tk.Label(text=problem_list[current_level]["question"],font=("Courier",16))
    question_label.place(x=0,y=60)
    answer_choice_str="A){}    B){}  C){}    D){}".format(problem_list[current_level]["answer"][0],problem_list[current_level]["answer"][1],problem_list[current_level]["answer"][2],problem_list[current_level]["answer"][3])
    global answer_label
    answer_label=tk.Label(text=answer_choice_str,font=("Courier",10))
    answer_label.place(x=0,y=200)
    y=250
    global group_stat
    for i in range(group_num):
        group_stat[i]={"point":0,"answered":False}
        group_checkbox.append(tk.Variable())
        group_checkbox[i].set(0)
        tk.Checkbutton(gui, text="group "+str(i+1),variable=group_checkbox[i],onvalue=1, offvalue=0,).place(x=0,y=y)
        y+=35
    tk.Label(text="Answer (enter A,B,C or D) : ").place(x=200,y=260)
    global inp
    inp=tk.Entry()
    inp.place(x=220,y=300)
    tk.Button(text="Submit",command=submit).place(x=520,y=280)
    gui.mainloop()

if __name__=="__main__":
    setup()
