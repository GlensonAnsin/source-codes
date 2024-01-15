from tkinter import *

main = Tk()
main.title('Employee Details')

idStr = StringVar()
nameStr = StringVar()
posStr = StringVar()

mainFrame = Frame(main)
showFrame = Frame(main)

##########FUNCTIONS##########
def add():
    emp_details = idStr.get()+','+nameStr.get()+','+posStr.get()+'\n'
    file = open('employee.txt', 'a+')
    file.write(emp_details)
    file.close()
    idStr.set('')
    nameStr.set('')
    posStr.set('')

def show():
    with open('employee.txt') as f:
        emp = f.readlines()
    showFrame.grid(row=6, column=0)

    count = 1
    for i in emp:
        e = i.split(',')
        print(e)

        idDis = Label(showFrame, text=e[0])
        idDis.grid(row=count, column=0)
        nameDis = Label(showFrame, text=e[1])
        nameDis.grid(row=count, column=1, columnspan=2)
        posDis = Label(showFrame, text=e[2].strip())
        posDis.grid(row=count, column=3, columnspan=2)

        count += 1

def showAdd():
    mainFrame.grid(row=0, column=0, rowspan=6)

##########MAIN FRAME##########
header = Label(mainFrame, text='Welcome to XYZ Company, enter employee details.')
header.grid(row=0, column=0, columnspan=6)

idLbl = Label(mainFrame, text='Employee ID:')
idLbl.grid(row=1, column=0, columnspan=2, sticky='w')
nameLbl = Label(mainFrame, text='Employee Name:')
nameLbl.grid(row=2, column=0, columnspan=2, sticky='w')
posLbl = Label(mainFrame, text='Employee Position:')
posLbl.grid(row=3, column=0, columnspan=2, sticky='w')

idEntry = Entry(mainFrame, text=idStr)
idEntry.grid(row=1, column=2, columnspan=3)
nameEntry = Entry(mainFrame, text=nameStr)
nameEntry.grid(row=2, column=2, columnspan=3)
posEntry = Entry(mainFrame, text=posStr)
posEntry.grid(row=3, column=2, columnspan=3)

submitBtn = Button(mainFrame, text='Submit', command=add)
submitBtn.grid(row=4, column=2)

##########SHOW FRAME##########
idShow = Label(showFrame, text='ID')
idShow.grid(row=0, column=0)
nameShow = Label(showFrame, text='Name')
nameShow.grid(row=0, column=1, columnspan=2)
posShow = Label(showFrame, text='Position')
posShow.grid(row=0, column=3, columnspan=2)

##########MENU##########
menuBar = Menu(main)
actionMenu = Menu(menuBar, tearoff=0)
actionMenu.add_command(label='Add Employee', command=showAdd)
actionMenu.add_command(label='Show Employee', command=show)
menuBar.add_cascade(label='Action', menu=actionMenu)
main.config(menu=menuBar)

main.mainloop()