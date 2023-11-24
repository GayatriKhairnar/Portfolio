import tkinter as tk
from tkinter import *
import random

win = tk.Tk()
win.configure(bg="light blue")
win.geometry("650x550")
win.title("Number Guessing Game")

result = StringVar()
choice = IntVar()
no = random.randint(1, 100)
result.set("Guess a number between 1 to 100 ")

guesses = [0]


def fun():

        guesses.append(choice.get())

        if guesses[-2]:
            if abs(no - guesses[-1]) < abs(no - guesses[-2]):
                result.set('WARMER!')
            else:
                result.set('COLDER!')

        else:
            if abs(no - choice.get()) <= 10:
                result.set('WARM!')
            else:
                result.set('COLD!')
        if choice.get() == no:
            result.set("Congratulations!!! You have guessed the number")


ent1 = Entry(win, textvariable=choice, width=3,
             font=('Ubuntu', 50))
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)


ent2 = Entry(win, textvariable=result, width=50,
                    font=('Courier', 15))
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)


msg = Label(win, text='Guess a number between 1 to 100 ',bg='yellow',
            font=("Courier", 25))
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg1 = Label(win, text=no, font=("Courier", 25))
msg1.place(relx=0.5, rely=0.9, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=(
    'Courier', 25), command=fun)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)


win.mainloop()
