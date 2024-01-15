from tkinter import *

main = Tk()

#Header
header = Label(main, text="Welcome to XYZ Systems, please enter employee details.", font="Arial")
header.grid(row=0, column=0, columnspan=5, pady=(0, 20))

#Label
emp_name = Label(main, text="Employee Name:", font="Arial")
emp_id = Label(main, text="Employee ID:", font="Arial")
emp_pos = Label(main, text="Employee Position:", font="Arial")
emp_salary = Label(main, text="Employee Salary:", font="Arial")

#Label Position
emp_name.grid(row=1, column=0, columnspan=2)
emp_id.grid(row=2, column=0, columnspan=2)
emp_pos.grid(row=3, column=0, columnspan=2)
emp_salary.grid(row=4, column=0, columnspan=2)

#Type Bar
emp_name_bar = Entry(main, width=30, borderwidth=5, font="Arial")
emp_id_bar = Entry(main, width=30, borderwidth=5, font="Arial")
emp_pos_bar = Entry(main, width=30, borderwidth=5, font="Arial")
emp_salary_bar = Entry(main, width=30, borderwidth=5, font="Arial")

#Type Bar Position
emp_name_bar.grid(row=1, column=2, columnspan=3)
emp_id_bar.grid(row=2, column=2, columnspan=3)
emp_pos_bar.grid(row=3, column=2, columnspan=3)
emp_salary_bar.grid(row=4, column=2, columnspan=3)

#Submit Button
sub_btn = Button(main, text="Submit", font="Arial")
sub_btn.grid(row=5, column=2, pady=(20, 0))

mainloop()