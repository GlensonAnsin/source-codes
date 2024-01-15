from tkinter import *

root = Tk()
root.title("1R14 Bacolanta and H.Amer Comp Prog P.I.T")
width = 826
height = 400
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenwidth() - height) // 5
rootGeometry = f"{width}x{height}+{x}+{y}"
root.geometry(rootGeometry)
root.resizable(False, False)

# Bubble Sort
lbl1 = Label(root, text="Enter the numbers to be sorted")
lbl1.place(x=65, y=25)
lbl2 = Label(root, text="(numbers separated with a space)")
lbl2.place(x=58, y=50)

entry1 = Entry(root, width=40)
entry1.place(x=30, y=80)

output1 = Text(root, width=30, height=10, state='disabled')
output1.place(x=30, y=120)


def bubbleSort():
    output1.config(state='normal')
    nums = list(map(int, entry1.get().split()))
    n = len(nums)
    for i in range(n):
        sorted = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                sorted = True
        if not sorted:
            break
        step = f"Step {i + 1}: {nums}\n"
        output1.insert(END, step)
    output1.config(state='disabled')


def clearBubbleSort():
    output1.config(state='normal')
    entry1.delete(0, END)
    output1.delete(1.0, END)
    output1.config(state='disabled')


button1 = Button(root, text="Bubble Sort", command=bubbleSort)
button1.place(x=30, y=300)

clear_button1 = Button(root, text="Clear", command=clearBubbleSort)
clear_button1.place(x=120, y=300)


# Insertion Sort
lbl3 = Label(root, text="Enter the numbers to be sorted")
lbl3.place(x=330, y=25)
lbl4 = Label(root, text="(numbers separated with a space)")
lbl4.place(x=323, y=50)

entry2 = Entry(root, width=40)
entry2.place(x=290, y=80)

output2 = Text(root, width=30, height=10, state='disabled')
output2.place(x=290, y=120)


def insertionSort():
    output2.config(state='normal')
    nums = list(map(int, entry2.get().split()))
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        step = f"Step {i}: {nums}\n"
        output2.insert(END, step)
    output2.config(state='disabled')


def clearInsertionSort():
    output2.config(state='normal')
    entry2.delete(0, END)
    output2.delete(1.0, END)
    output2.config(state='disabled')


button2 = Button(root, text="Insertion Sort", command=insertionSort)
button2.place(x=290, y=300)

clear_button2 = Button(root, text="Clear", command=clearInsertionSort)
clear_button2.place(x=389, y=300)


# Selection Sort
lbl5 = Label(root, text="Enter the numbers to be sorted")
lbl5.place(x=590, y=25)
lbl6 = Label(root, text="(numbers separated with a space)")
lbl6.place(x=583, y=50)

entry3 = Entry(root, width=40)
entry3.place(x=551, y=80)

output3 = Text(root, width=30, height=10, state='disabled')
output3.place(x=551, y=120)


def selectionSort():
    output3.config(state='normal')
    nums = list(map(int, entry3.get().split()))
    n = len(nums)
    for i in range(n):
        sorted = False
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            sorted = True
        if not sorted:
            break
        step = f"Step {i + 1}: {nums}\n"
        output3.insert(END, step)
    output3.config(state='disabled')


def clearSelectionSort():
    output3.config(state='normal')
    entry3.delete(0, END)
    output3.delete(1.0, END)
    output3.config(state='disabled')


button3 = Button(root, text="Selection Sort", command=selectionSort)
button3.place(x=550, y=300)

clear_button3 = Button(root, text="Clear", command=clearSelectionSort)
clear_button3.place(x=650, y=300)

root.mainloop()