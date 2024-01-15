from tkinter import *
from functools import partial

main = Tk()
main.title("Calculator")
main.configure(bg="gray")
exp = StringVar()

def click(nums):
    exp.set(exp.get() + nums)

def answer():
    result = eval(exp.get())
    exp.set(result)

def clear():
    exp.set("")

#Cal Label
cal_label = Label(main, text="Ansin Calculator", font=("Arial", 11), bg="gray")
cal_label.grid(row=0, column=1, columnspan=2)

#Type Bar
type_num = Entry(main, width=20, font="Arial", borderwidth=5, text=exp)
type_num.grid(row=1, column=0, columnspan=4)

#Button
zero_btn = Button(main, text="0", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "0"))
one_btn = Button(main, text="1", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "1"))
two_btn = Button(main, text="2", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "2"))
three_btn = Button(main, text="3", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "3"))
four_btn = Button(main, text="4", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "4"))
five_btn = Button(main, text="5", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "5"))
six_btn = Button(main, text="6", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "6"))
seven_btn = Button(main, text="7", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "7"))
eight_btn = Button(main, text="8", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "8"))
nine_btn = Button(main, text="9", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "9"))
plus_btn = Button(main, text="+", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "+"))
minus_btn = Button(main, text="-", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "-"))
times_btn = Button(main, text="x", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "*"))
divide_btn = Button(main, text="÷", font=("Arial", 11), width=5, height=3, bg="gray", command=partial(click, "/"))
equal_btn = Button(main, text="=", font=("Arial", 11), width=5, height=3, bg="gray", command=answer)
clear_btn = Button(main, text="C", font=("Arial", 11), width=5, height=3, bg="gray", command=clear)

#Button position
zero_btn.grid(row=5, column=0)
one_btn.grid(row=2, column=0)
two_btn.grid(row=2, column=1)
three_btn.grid(row=2, column=2)
four_btn.grid(row=3, column=0)
five_btn.grid(row=3, column=1)
six_btn.grid(row=3, column=2)
seven_btn.grid(row=4, column=0)
eight_btn.grid(row=4, column=1)
nine_btn.grid(row=4, column=2)
plus_btn.grid(row=2, column=3)
minus_btn.grid(row=3, column=3)
times_btn.grid(row=4, column=3)
divide_btn.grid(row=5, column=3)
equal_btn.grid(row=5, column=1)
clear_btn.grid(row=5, column=2)

mainloop()
