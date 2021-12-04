import random
import tkinter as tk
window = tk.Tk()
window.geometry("250x250")
window.title("Rock Paper Scissors Game")
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""
def choice_to_number(choice):
    rps = {'rock':0, 'paper':1, 'scissors':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0:'rock', 1:'paper', 2:'scissors'}
    return rps[number]
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def result(human_choice, comp_choice):
    global user_score
    global comp_score
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print('Tie!')
    elif((user-comp)%3==1):
        print('You Win!')
        user_score+=1
    else:
        print('Computer Wins :(')
        comp_score+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#79cdcd")
    text_area.grid(column=0,row=4)
    answer = "Your Choice : {uc} \nComputer's Choice : {cc} \nYour Score : {u} \nComputer Score : {c} ".format(uc=user_choice,cc=comp_choice,u=user_score,c=comp_score)
    text_area.insert(tk.END,answer)
def rock():
    global user_choice
    global comp_choice
    user_choice='rock'
    comp_choice=random_computer_choice()
    result(user_choice,comp_choice)
def paper():
    global user_choice
    global comp_choice
    user_choice='paper'
    comp_choice=random_computer_choice()
    result(user_choice,comp_choice)
def scissors():
    global user_choice
    global comp_choice
    user_choice='scissors'
    comp_choice=random_computer_choice()
    result(user_choice,comp_choice)
button1 = tk.Button(text='         Rock         ',bg="#548f8f",fg="white",command=rock)
button1.grid(column=0, row=1)
button2 = tk.Button(text='         Paper         ',bg="#60a4a4",fg="white",command=paper)
button2.grid(column=0, row=2)
button3 = tk.Button(text='        Scissors         ',bg="#6cb8b8",fg="white",command=scissors)
button3.grid(column=0, row=3)
window.mainloop()
