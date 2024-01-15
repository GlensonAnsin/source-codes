from tkinter import *

main = Tk()
main.geometry("320x470")
main.configure(bg="dark gray")
main.title("Calculator")

#Logo
logo = PhotoImage(file="d:/Projects/Python/Calculator/logo.png")
main.iconphoto(False, logo)

#Calculator Label
cal_label = Label(main, text="CALCULATOR", font=("Arial", 12), width=12, bg="dark gray")
cal_label.grid(row=0, columnspan=3)

#Type Bar
type_num = Entry(main, width=28, borderwidth=5, font=("Arial", 14))
type_num.grid(row=1, columnspan=3)

#Functions
def click_btn(numbers):
    cur_num = type_num.get()
    type_num.delete(0, END)
    type_num.insert(0, str(cur_num) + str(numbers))

def btn_clear():
    type_num.delete(0, END)

def add():
    first_num = type_num.get()
    global f_num
    global calculate
    calculate = "Addition"
    f_num = int(first_num)
    type_num.delete(0, END)

def subtract():
    first_num = type_num.get()
    global f_num
    global calculate
    calculate = "Subtraction"
    f_num = int(first_num)
    type_num.delete(0, END)

def multiply():
    first_num = type_num.get()
    global f_num
    global calculate
    calculate = "Multiplication"
    f_num = int(first_num)
    type_num.delete(0, END)

def divide():
    first_num = type_num.get()
    global f_num
    global calculate
    calculate = "Division"
    f_num = int(first_num)
    type_num.delete(0, END)

def equal():
    sec_num = type_num.get()
    type_num.delete(0, END)
    if calculate == "Addition":
        type_num.insert(0, f_num + int(sec_num))
    elif calculate == "Subtraction":
        type_num.insert(0, f_num - int(sec_num))
    elif calculate == "Multiplication":
        type_num.insert(0, f_num * int(sec_num))
    elif calculate == "Division":
        type_num.insert(0, f_num / int(sec_num))

#Buttons
num_1 = Button(main, text="1", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(1))
num_2 = Button(main, text="2", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(2))
num_3 = Button(main, text="3", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(3))
num_4 = Button(main, text="4", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(4))
num_5 = Button(main, text="5", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(5))
num_6 = Button(main, text="6", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(6))
num_7 = Button(main, text="7", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(7))
num_8 = Button(main, text="8", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(8))
num_9 = Button(main, text="9", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(9))
num_0 = Button(main, text="0", padx=40, pady=20, bg="gray", activebackground="white", command=lambda: click_btn(0))
btn_plus = Button(main, text="+", padx=39, pady=20, bg="gray", activebackground="white", command=add)
btn_minus = Button(main, text="-", padx=40, pady=20, bg="gray", activebackground="white", command=subtract)
btn_times = Button(main, text="x", padx=40, pady=20, bg="gray", activebackground="white", command=multiply)
btn_divide = Button(main, text="÷", padx=39, pady=20, bg="gray", activebackground="white", command=divide)
btn_equal = Button(main, text="=", padx=147, pady=20, bg="gray", activebackground="white", command=equal)
clear = Button(main, text="C", padx=39, pady=20, bg="gray", activebackground="white", command=btn_clear)

#Buttons Positioning
btn_equal.grid(row=7, columnspan=3, pady=(0, 10))
btn_divide.grid(row=6, column=0)
btn_minus.grid(row=6, column=1)
btn_times.grid(row=6, column=2)
num_0.grid(row=5, column=0)
clear.grid(row=5, column=1)
btn_plus.grid(row=5, column=2)
num_1.grid(row=4, column=0)
num_2.grid(row=4, column=1)
num_3.grid(row=4, column=2)
num_4.grid(row=3, column=0)
num_5.grid(row=3, column=1)
num_6.grid(row=3, column=2)
num_7.grid(row=2, column=0, pady=(10, 0))
num_8.grid(row=2, column=1, pady=(10, 0))
num_9.grid(row=2, column=2, pady=(10, 0))

main.mainloop()