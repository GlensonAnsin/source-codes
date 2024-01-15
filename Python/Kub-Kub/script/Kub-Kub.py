from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

# ==============================MAIN-WINDOW============================== #
main = Tk()
main.title('KUB-KUB')
main_width = 800
main_height = 500
x_pos = (main.winfo_screenwidth() - main_width) // 2
y_pos = (main.winfo_screenwidth() - main_height) // 6
mainGeometry = f'{main_width}x{main_height}+{x_pos}+{y_pos}'
main.geometry(mainGeometry)
main.resizable(False, False)
main.iconbitmap('Kub-Kub-Icon.ico')

# ==============================DELIVERY-WINDOW============================== #
def delivery_window():
    main.withdraw()
    del_win = Toplevel()
    del_win.title('KUB-KUB')
    del_win_width = 800
    del_win_height = 500
    x_pos = (del_win.winfo_screenwidth() - del_win_width) // 2
    y_pos = (del_win.winfo_screenwidth() - del_win_height) // 6
    del_winGeometry = f'{del_win_width}x{del_win_height}+{x_pos}+{y_pos}'
    del_win.geometry(del_winGeometry)
    del_win.resizable(False, False)
    del_win.iconbitmap('Kub-Kub-Icon.ico')

    show_orders = []
    order_prices = []

    # ==============================DELIVERY-WINDOW-NAVBAR============================== #
    def return_to_main():
        del_win.destroy()
        main.deiconify()

    nav_frame = Frame(del_win)
    nav_frame.pack(side=TOP, fill=X)
    navbar = Frame(nav_frame, width=800, height=80, bg='#4b91f1')
    navbar.grid(row=0, column=0, columnspan=6)
    logo_img = Image.open('Kub-Kub Logo.jpg')
    logo_img.thumbnail((100, 70))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo = Label(nav_frame, image=logo_photo)
    logo.grid(row=0, column=0, padx=(8, 0), columnspan=2, sticky='w')
    returnBtn = Button(nav_frame, text='Home', font=('Kristen ITC', 10, 'bold'), command=return_to_main)
    returnBtn.grid(row=0, column=5)

    # ==============================DELIVERY-WINDOW-SCROLLBAR============================== #
    cont_frame = Frame(del_win)
    cont_frame.pack(fill=BOTH, expand=1)
    cont_canvas = Canvas(cont_frame)
    cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
    cont_scrollbar.pack(side=RIGHT, fill=Y)
    cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
    cont_canvas.bind('<Configure>', lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
    secondcont_frame = Frame(cont_canvas)
    cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

    # ==============================DELIVERY-WINDOW-CONTENT============================== #
    # ==========BREAKFAST-CALCULATIONS========== #
    def bf_orderbtn1():
        if BFquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty1.set(0)
        elif BFquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty1.set(0)
        elif int(BFquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty1.set(0)
        elif int(BFquantity1.get()) > 0 and int(BFquantity1.get()) <= 50:
            bf_1_total = int(BFquantity1.get()) * 185.00
            current_val.set(bf_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Oatmeal with Berries\nand Nuts'+','+f'185.00'+','+f'{BFquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_1_total
            order_prices.append(food_price)

            BFqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty1.set(0)

    def bf_orderbtn2():
        if BFquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty2.set(0)
        elif BFquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty2.set(0)
        elif int(BFquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty2.set(0)
        elif int(BFquantity2.get()) > 0 and int(BFquantity2.get()) <= 50:
            bf_2_total = int(BFquantity2.get()) * 35.00
            current_val.set(bf_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Avocado Toast'+','+'35.00'+','+f'{BFquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_2_total
            order_prices.append(food_price)

            BFqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty2.set(0)

    def bf_orderbtn3():
        if BFquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty3.set(0)
        elif BFquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty3.set(0)
        elif int(BFquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty3.set(0)
        elif int(BFquantity3.get()) > 0 and int(BFquantity3.get()) <= 50:
            bf_3_total = int(BFquantity3.get()) * 120.00
            current_val.set(bf_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Greek Yogurt with\nGranola with Honey'+','+'120.00'+','+f'{BFquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_3_total
            order_prices.append(food_price)

            BFqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty3.set(0)

    def bf_orderbtn4():
        if BFquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty4.set(0)
        elif BFquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty4.set(0)
        elif int(BFquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty4.set(0)
        elif int(BFquantity4.get()) > 0 and int(BFquantity4.get()) <= 50:
            bf_4_total = int(BFquantity4.get()) * 99.00
            current_val.set(bf_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Veggie Omelet'+','+'99.00'+','+f'{BFquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_4_total
            order_prices.append(food_price)

            BFqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty4.set(0)

    def bf_orderbtn5():
        if BFquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty5.set(0)
        elif BFquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty5.set(0)
        elif int(BFquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty5.set(0)
        elif int(BFquantity5.get()) > 0 and int(BFquantity5.get()) <= 50:
            bf_5_total = int(BFquantity5.get()) * 299.00
            current_val.set(bf_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Smoothie Bowl'+','+'299.00'+','+f'{BFquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_5_total
            order_prices.append(food_price)

            BFqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty5.set(0)

    def bf_orderbtn6():
        if BFquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty6.set(0)
        elif BFquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty6.set(0)
        elif int(BFquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty6.set(0)
        elif int(BFquantity6.get()) > 0 and int(BFquantity6.get()) <= 50:
            bf_6_total = int(BFquantity6.get()) * 150.00
            current_val.set(bf_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Whole Grain Pancakes\nwith Maple Syrup'+','+'150.00'+',' + f'{BFquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_6_total
            order_prices.append(food_price)

            BFqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty6.set(0)

    def bf_orderbtn7():
        if BFquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty7.set(0)
        elif BFquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty7.set(0)
        elif int(BFquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty7.set(0)
        elif int(BFquantity7.get()) > 0 and int(BFquantity7.get()) <= 50:
            bf_7_total = int(BFquantity7.get()) * 175.00
            current_val.set(bf_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Breakfast Burrito'+','+'175.00'+','+f'{BFquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_7_total
            order_prices.append(food_price)

            BFqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty7.set(0)

    def bf_orderbtn8():
        if BFquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty8.set(0)
        elif BFquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty8.set(0)
        elif int(BFquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty8.set(0)
        elif int(BFquantity8.get()) > 0 and int(BFquantity8.get()) <= 50:
            bf_8_total = int(BFquantity8.get()) * 250.00
            current_val.set(bf_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Quinoa Breakfast Bowl'+','+'250.00'+','+f'{BFquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_8_total
            order_prices.append(food_price)

            BFqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty8.set(0)

    # ==========LUNCH-CALCULATIONS========== #
    def lunch_orderbtn1():
        if LUquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty1.set(0)
        elif LUquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty1.set(0)
        elif int(LUquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty1.set(0)
        elif int(LUquantity1.get()) > 0 and int(LUquantity1.get()) <= 50:
            lunch_1_total = int(LUquantity1.get()) * 550.00
            current_val.set(lunch_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Grilled Chicken Salad'+','+'550.00'+','+f'{LUquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_1_total
            order_prices.append(food_price)

            LUqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty1.set(0)

    def lunch_orderbtn2():
        if LUquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty2.set(0)
        elif LUquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty2.set(0)
        elif int(LUquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty2.set(0)
        elif int(LUquantity2.get()) > 0 and int(LUquantity2.get()) <= 50:
            lunch_2_total = int(LUquantity2.get()) * 385.00
            current_val.set(lunch_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Quinoa and Roasted\nVegetable Bowl'+','+'385.00'+','+f'{LUquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_2_total
            order_prices.append(food_price)

            LUqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty2.set(0)

    def lunch_orderbtn3():
        if LUquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty3.set(0)
        elif LUquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty3.set(0)
        elif int(LUquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty3.set(0)
        elif int(LUquantity3.get()) > 0 and int(LUquantity3.get()) <= 50:
            lunch_3_total = int(LUquantity3.get()) * 120.00
            current_val.set(lunch_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Turkey and Avocado\nWrap'+','+'120.00'+','+f'{LUquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_3_total
            order_prices.append(food_price)

            LUqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty3.set(0)

    def lunch_orderbtn4():
        if LUquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty4.set(0)
        elif LUquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty4.set(0)
        elif int(LUquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty4.set(0)
        elif int(LUquantity4.get()) > 0 and int(LUquantity4.get()) <= 50:
            lunch_4_total = int(LUquantity4.get()) * 75.00
            current_val.set(lunch_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Caprese Salad'+','+'75.00'+','+f'{LUquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_4_total
            order_prices.append(food_price)

            LUqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty4.set(0)

    def lunch_orderbtn5():
        if LUquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty5.set(0)
        elif LUquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty5.set(0)
        elif int(LUquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty5.set(0)
        elif int(LUquantity5.get()) > 0 and int(LUquantity5.get()) <= 50:
            lunch_5_total = int(LUquantity5.get()) * 110.00
            current_val.set(lunch_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Lentil Soup'+','+'110.00'+','+f'{LUquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_5_total
            order_prices.append(food_price)

            LUqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty5.set(0)

    def lunch_orderbtn6():
        if LUquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty6.set(0)
        elif LUquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty6.set(0)
        elif int(LUquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty6.set(0)
        elif int(LUquantity6.get()) > 0 and int(LUquantity6.get()) <= 50:
            lunch_6_total = int(LUquantity6.get()) * 145.00
            current_val.set(lunch_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Grilled Salmon with\nSteamed Vegetables'+','+'145.00'+','+f'{LUquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_6_total
            order_prices.append(food_price)

            LUqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty6.set(0)

    def lunch_orderbtn7():
        if LUquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty7.set(0)
        elif LUquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty7.set(0)
        elif int(LUquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty7.set(0)
        elif int(LUquantity7.get()) > 0 and int(LUquantity7.get()) <= 50:
            lunch_7_total = int(LUquantity7.get()) * 600.00
            current_val.set(lunch_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Quinoa Salad with\nChickpeas and Feta\nCheese'+','+'600.00'+','+f'{LUquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_7_total
            order_prices.append(food_price)

            LUqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty7.set(0)

    def lunch_orderbtn8():
        if LUquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty8.set(0)
        elif LUquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty8.set(0)
        elif int(LUquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty8.set(0)
        elif int(LUquantity8.get()) > 0 and int(LUquantity8.get()) <= 50:
            lunch_8_total = int(LUquantity8.get()) * 125.00
            current_val.set(lunch_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Veggie Wrap with\nHummus'+','+'125.00'+','+f'{LUquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_8_total
            order_prices.append(food_price)

            LUqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty8.set(0)

    # ==========DINNER-CALCULATIONS========== #
    def dinner_orderbtn1():
        if DIquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty1.set(0)
        elif DIquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty1.set(0)
        elif int(DIquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty1.set(0)
        elif int(DIquantity1.get()) > 0 and int(DIquantity1.get()) <= 50:
            dinner_1_total = int(DIquantity1.get()) * 360.00
            current_val.set(dinner_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Grilled Chicken with\nRoasted Sweet Potatoes'+','+'360.00'+','+f'{DIquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_1_total
            order_prices.append(food_price)

            DIqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty1.set(0)

    def dinner_orderbtn2():
        if DIquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty2.set(0)
        elif DIquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty2.set(0)
        elif int(DIquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty2.set(0)
        elif int(DIquantity2.get()) > 0 and int(DIquantity2.get()) <= 50:
            dinner_2_total = int(DIquantity2.get()) * 167.00
            current_val.set(dinner_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Spaghetti with Marinara\nSauce'+','+'167.00'+','+f'{DIquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_2_total
            order_prices.append(food_price)

            DIqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty2.set(0)

    def dinner_orderbtn3():
        if DIquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty3.set(0)
        elif DIquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty3.set(0)
        elif int(DIquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty3.set(0)
        elif int(DIquantity3.get()) > 0 and int(DIquantity3.get()) <= 50:
            dinner_3_total = int(DIquantity3.get()) * 138.00
            current_val.set(dinner_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Baked Salmon with\nQuinoa Pilaf'+','+'138.00'+','+f'{DIquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_3_total
            order_prices.append(food_price)

            DIqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty3.set(0)

    def dinner_orderbtn4():
        if DIquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty4.set(0)
        elif DIquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty4.set(0)
        elif int(DIquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty4.set(0)
        elif int(DIquantity4.get()) > 0 and int(DIquantity4.get()) <= 50:
            dinner_4_total = int(DIquantity4.get()) * 322.00
            current_val.set(dinner_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Stir-Fried Tofu\nand Vegetables'+','+'322.00'+','+f'{DIquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_4_total
            order_prices.append(food_price)

            DIqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty4.set(0)

    def dinner_orderbtn5():
        if DIquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty5.set(0)
        elif DIquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty5.set(0)
        elif int(DIquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty5.set(0)
        elif int(DIquantity5.get()) > 0 and int(DIquantity5.get()) <= 50:
            dinner_5_total = int(DIquantity5.get()) * 449.00
            current_val.set(dinner_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Shrimp and Vegetable\nKebabs'+','+'449.00'+','+f'{DIquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_5_total
            order_prices.append(food_price)

            DIqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty5.set(0)

    def dinner_orderbtn6():
        if DIquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty6.set(0)
        elif DIquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty6.set(0)
        elif int(DIquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty6.set(0)
        elif int(DIquantity6.get()) > 0 and int(DIquantity6.get()) <= 50:
            dinner_6_total = int(DIquantity6.get()) * 389.00
            current_val.set(dinner_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Stuffed Bell Peppers'+','+'389.00'+','+f'{DIquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_6_total
            order_prices.append(food_price)

            DIqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty6.set(0)

    def dinner_orderbtn7():
        if DIquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty7.set(0)
        elif DIquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty7.set(0)
        elif int(DIquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty7.set(0)
        elif int(DIquantity7.get()) > 0 and int(DIquantity7.get()) <= 50:
            dinner_7_total = int(DIquantity7.get()) * 325.00
            current_val.set(dinner_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Eggplant Parmesan'+','+'325.00'+','+f'{DIquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_7_total
            order_prices.append(food_price)

            DIqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty7.set(0)

    def dinner_orderbtn8():
        if DIquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty8.set(0)
        elif DIquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty8.set(0)
        elif int(DIquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty8.set(0)
        elif int(DIquantity8.get()) > 0 and int(DIquantity8.get()) <= 50:
            dinner_8_total = int(DIquantity8.get()) * 299.00
            current_val.set(dinner_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Mexican-Style Chicken\nFajitas'+','+'299.00'+','+f'{DIquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_8_total
            order_prices.append(food_price)

            DIqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty8.set(0)

    # ==========DRINKS-CALCULATIONS========== #
    def drink_orderbtn1():
        if DRquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty1.set(0)
        elif DRquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty1.set(0)
        elif int(DRquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty1.set(0)
        elif int(DRquantity1.get()) > 0 and int(DRquantity1.get()) <= 50:
            drink_1_total = int(DRquantity1.get()) * 37.00
            current_val.set(drink_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Coca-Cola'+','+'37.00'+','+f'{DRquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_1_total
            order_prices.append(food_price)

            DRqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty1.set(0)

    def drink_orderbtn2():
        if DRquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty2.set(0)
        elif DRquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty2.set(0)
        elif int(DRquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty2.set(0)
        elif int(DRquantity2.get()) > 0 and int(DRquantity2.get()) <= 50:
            drink_2_total = int(DRquantity2.get()) * 37.00
            current_val.set(drink_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Pineapple Juice'+','+'37.00'+','+f'{DRquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_2_total
            order_prices.append(food_price)

            DRqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty2.set(0)

    def drink_orderbtn3():
        if DRquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty3.set(0)
        elif DRquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty3.set(0)
        elif int(DRquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty3.set(0)
        elif int(DRquantity3.get()) > 0 and int(DRquantity3.get()) <= 50:
            drink_3_total = int(DRquantity3.get()) * 45.00
            current_val.set(drink_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Mango Lassi'+','+'45.00'+','+f'{DRquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_3_total
            order_prices.append(food_price)

            DRqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty3.set(0)

    def drink_orderbtn4():
        if DRquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty4.set(0)
        elif DRquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty4.set(0)
        elif int(DRquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty4.set(0)
        elif int(DRquantity4.get()) > 0 and int(DRquantity4.get()) <= 50:
            drink_4_total = int(DRquantity4.get()) * 59.00
            current_val.set(drink_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Fruit Punch'+','+'59.00'+','+f'{DRquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_4_total
            order_prices.append(food_price)

            DRqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty4.set(0)

    def drink_orderbtn5():
        if DRquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty5.set(0)
        elif DRquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty5.set(0)
        elif int(DRquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty5.set(0)
        elif int(DRquantity5.get()) > 0 and int(DRquantity5.get()) <= 50:
            drink_5_total = int(DRquantity5.get()) * 44.00
            current_val.set(drink_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Sparkling Lemonade'+','+'44.00'+','+f'{DRquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_5_total
            order_prices.append(food_price)

            DRqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty5.set(0)

    def drink_orderbtn6():
        if DRquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty6.set(0)
        elif DRquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty6.set(0)
        elif int(DRquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty6.set(0)
        elif int(DRquantity6.get()) > 0 and int(DRquantity6.get()) <= 50:
            drink_6_total = int(DRquantity6.get()) * 66.00
            current_val.set(drink_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Pomegranate Spritzer'+','+'66.00'+','+f'{DRquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_6_total
            order_prices.append(food_price)

            DRqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty6.set(0)

    def drink_orderbtn7():
        if DRquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty7.set(0)
        elif DRquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty7.set(0)
        elif int(DRquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty7.set(0)
        elif int(DRquantity7.get()) > 0 and int(DRquantity7.get()) <= 50:
            drink_7_total = int(DRquantity7.get()) * 83.00
            current_val.set(drink_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Virgin Mojito'+','+'83.00'+','+f'{DRquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_7_total
            order_prices.append(food_price)

            DRqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty7.set(0)

    def drink_orderbtn8():
        if DRquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty8.set(0)
        elif DRquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty8.set(0)
        elif int(DRquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty8.set(0)
        elif int(DRquantity8.get()) > 0 and int(DRquantity8.get()) <= 50:
            drink_8_total = int(DRquantity8.get()) * 77.00
            current_val.set(drink_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Cucumber Cooler'+','+'77.00'+','+f'{DRquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_8_total
            order_prices.append(food_price)

            DRqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty8.set(0)

    # ==========BREAKFAST========== #
    breakfastLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'),  text='Breakfast')
    breakfastLbl.grid(row=0, column=0, columnspan=2, padx=(8, 0), pady=(8, 0))

    # THIS IS FIRST COLUMN IN BREAKFAST
    # ==========IMAGE========== #
    bf_1 = Image.open(r'Foods\Breakfast\bf-1.png')
    bf_2 = Image.open(r'Foods\Breakfast\bf-2.png')
    bf_3 = Image.open(r'Foods\Breakfast\bf-3.png')
    bf_4 = Image.open(r'Foods\Breakfast\bf-4.png')
    bf_1.thumbnail((100, 100))
    bf_2.thumbnail((100, 100))
    bf_3.thumbnail((100, 100))
    bf_4.thumbnail((100, 100))
    bf_1_photo = ImageTk.PhotoImage(bf_1)
    bf_2_photo = ImageTk.PhotoImage(bf_2)
    bf_3_photo = ImageTk.PhotoImage(bf_3)
    bf_4_photo = ImageTk.PhotoImage(bf_4)
    bf_1_Lbl = Label(secondcont_frame, image=bf_1_photo)
    bf_2_Lbl = Label(secondcont_frame, image=bf_2_photo)
    bf_3_Lbl = Label(secondcont_frame, image=bf_3_photo)
    bf_4_Lbl = Label(secondcont_frame, image=bf_4_photo)
    bf_1_Lbl.grid(row=1, column=1, columnspan=2, padx=40, pady=(8, 0))
    bf_2_Lbl.grid(row=1, column=3, columnspan=2, padx=40, pady=(8, 0))
    bf_3_Lbl.grid(row=1, column=5, columnspan=2, padx=40, pady=(8, 0))
    bf_4_Lbl.grid(row=1, column=7, columnspan=2, padx=40, pady=(8, 0))

    # ==========NAME========== #
    bf_1_name = Label(secondcont_frame, text='Oatmeal with Berries\nand Nuts', font=('Kristen ITC', 9))
    bf_2_name = Label(secondcont_frame, text='Avocado Toast', font=('Kristen ITC', 9))
    bf_3_name = Label(secondcont_frame, text='Greek Yogurt with\nGranola with Honey', font=('Kristen ITC', 9))
    bf_4_name = Label(secondcont_frame, text='Veggie Omelet', font=('Kristen ITC', 9))
    bf_1_name.grid(row=2, column=1, columnspan=2, padx=40, pady=(8, 0))
    bf_2_name.grid(row=2, column=3, columnspan=2, padx=40, pady=(8, 0))
    bf_3_name.grid(row=2, column=5, columnspan=2, padx=40, pady=(8, 0))
    bf_4_name.grid(row=2, column=7, columnspan=2, padx=40, pady=(8, 0))

    # ==========PRICE========== #
    bf_1_price = Label(secondcont_frame, text='₱185.00', font=('Arial', 11, 'bold'))
    bf_2_price = Label(secondcont_frame, text='₱35.00', font=('Arial', 11, 'bold'))
    bf_3_price = Label(secondcont_frame, text='₱120.00', font=('Arial', 11, 'bold'))
    bf_4_price = Label(secondcont_frame, text='₱99.00', font=('Arial', 11, 'bold'))
    bf_1_price.grid(row=3, column=1, columnspan=2, padx=40)
    bf_2_price.grid(row=3, column=3, columnspan=2, padx=40)
    bf_3_price.grid(row=3, column=5, columnspan=2, padx=40)
    bf_4_price.grid(row=3, column=7, columnspan=2, padx=40)

    # ==========ORDER-BUTTON========== #
    BForderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn1)
    BForderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn2)
    BForderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn3)
    BForderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn4)
    BForderBtn1.grid(row=4, column=1, columnspan=2)
    BForderBtn2.grid(row=4, column=3, columnspan=2)
    BForderBtn3.grid(row=4, column=5, columnspan=2)
    BForderBtn4.grid(row=4, column=7, columnspan=2)

    # ==========QUANTITY========== #
    BFqty1 = IntVar()
    BFqty2 = IntVar()
    BFqty3 = IntVar()
    BFqty4 = IntVar()
    BFquantity1 = Entry(secondcont_frame, textvariable=BFqty1, font='Arial', width=2)
    BFquantity2 = Entry(secondcont_frame, textvariable=BFqty2, font='Arial', width=2)
    BFquantity3 = Entry(secondcont_frame, textvariable=BFqty3, font='Arial', width=2)
    BFquantity4 = Entry(secondcont_frame, textvariable=BFqty4, font='Arial', width=2)
    BFquantity1.grid(row=4, column=1, columnspan=2, padx=(90, 0))
    BFquantity2.grid(row=4, column=3, columnspan=2, padx=(90, 0))
    BFquantity3.grid(row=4, column=5, columnspan=2, padx=(90, 0))
    BFquantity4.grid(row=4, column=7, columnspan=2, padx=(90, 0))
    BFqty1.set(0)
    BFqty2.set(0)
    BFqty3.set(0)
    BFqty4.set(0)

    # THIS IS SECOND COLUMN IN BREAKFAST
    # ==========IMAGE========== #
    bf_5 = Image.open(r'Foods\Breakfast\bf-5.png')
    bf_6 = Image.open(r'Foods\Breakfast\bf-6.png')
    bf_7 = Image.open(r'Foods\Breakfast\bf-7.png')
    bf_8 = Image.open(r'Foods\Breakfast\bf-8.png')
    bf_5.thumbnail((100, 100))
    bf_6.thumbnail((100, 100))
    bf_7.thumbnail((100, 100))
    bf_8.thumbnail((100, 100))
    bf_5_photo = ImageTk.PhotoImage(bf_5)
    bf_6_photo = ImageTk.PhotoImage(bf_6)
    bf_7_photo = ImageTk.PhotoImage(bf_7)
    bf_8_photo = ImageTk.PhotoImage(bf_8)
    bf_5_Lbl = Label(secondcont_frame, image=bf_5_photo)
    bf_6_Lbl = Label(secondcont_frame, image=bf_6_photo)
    bf_7_Lbl = Label(secondcont_frame, image=bf_7_photo)
    bf_8_Lbl = Label(secondcont_frame, image=bf_8_photo)
    bf_5_Lbl.grid(row=5, column=1, columnspan=2, pady=(8, 0))
    bf_6_Lbl.grid(row=5, column=3, columnspan=2, pady=(8, 0))
    bf_7_Lbl.grid(row=5, column=5, columnspan=2, pady=(8, 0))
    bf_8_Lbl.grid(row=5, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    bf_5_name = Label(secondcont_frame, text='Smoothie Bowl', font=('Kristen ITC', 9))
    bf_6_name = Label(secondcont_frame, text='Whole Grain Pancakes\nwith Maple Syrup', font=('Kristen ITC', 9))
    bf_7_name = Label(secondcont_frame, text='Breakfast Burrito', font=('Kristen ITC', 9))
    bf_8_name = Label(secondcont_frame, text='Quinoa Breakfast\nBowl', font=('Kristen ITC', 9))
    bf_5_name.grid(row=6, column=1, columnspan=2, pady=(8, 0))
    bf_6_name.grid(row=6, column=3, columnspan=2, pady=(8, 0))
    bf_7_name.grid(row=6, column=5, columnspan=2, pady=(8, 0))
    bf_8_name.grid(row=6, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    bf_5_price = Label(secondcont_frame, text='₱299.00', font=('Arial', 11, 'bold'))
    bf_6_price = Label(secondcont_frame, text='₱150.00', font=('Arial', 11, 'bold'))
    bf_7_price = Label(secondcont_frame, text='₱175.00', font=('Arial', 11, 'bold'))
    bf_8_price = Label(secondcont_frame, text='₱250.00', font=('Arial', 11, 'bold'))
    bf_5_price.grid(row=7, column=1, columnspan=2)
    bf_6_price.grid(row=7, column=3, columnspan=2)
    bf_7_price.grid(row=7, column=5, columnspan=2)
    bf_8_price.grid(row=7, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    BForderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn5)
    BForderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn6)
    BForderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn7)
    BForderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn8)
    BForderBtn5.grid(row=8, column=1, columnspan=2)
    BForderBtn6.grid(row=8, column=3, columnspan=2)
    BForderBtn7.grid(row=8, column=5, columnspan=2)
    BForderBtn8.grid(row=8, column=7, columnspan=2)

    # ==========QUANTITY========== #
    BFqty5 = IntVar()
    BFqty6 = IntVar()
    BFqty7 = IntVar()
    BFqty8 = IntVar()
    BFquantity5 = Entry(secondcont_frame, textvariable=BFqty5, font='Arial', width=2)
    BFquantity6 = Entry(secondcont_frame, textvariable=BFqty6, font='Arial', width=2)
    BFquantity7 = Entry(secondcont_frame, textvariable=BFqty7, font='Arial', width=2)
    BFquantity8 = Entry(secondcont_frame, textvariable=BFqty8, font='Arial', width=2)
    BFquantity5.grid(row=8, column=1, columnspan=2, padx=(90, 0))
    BFquantity6.grid(row=8, column=3, columnspan=2, padx=(90, 0))
    BFquantity7.grid(row=8, column=5, columnspan=2, padx=(90, 0))
    BFquantity8.grid(row=8, column=7, columnspan=2, padx=(90, 0))
    BFqty5.set(0)
    BFqty6.set(0)
    BFqty7.set(0)
    BFqty8.set(0)

    # ==========LUNCH========== #
    lunchLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Lunch')
    lunchLbl.grid(row=9, column=0, columnspan=2, padx=(8, 0), pady=(18, 0))

    # THIS IS FIRST COLUMN IN LUNCH
    # ==========IMAGE========== #
    lunch_1 = Image.open(r'Foods\Lunch\lunch-1.png')
    lunch_2 = Image.open(r'Foods\Lunch\lunch-2.png')
    lunch_3 = Image.open(r'Foods\Lunch\lunch-3.png')
    lunch_4 = Image.open(r'Foods\Lunch\lunch-4.png')
    lunch_1.thumbnail((100, 100))
    lunch_2.thumbnail((100, 100))
    lunch_3.thumbnail((100, 100))
    lunch_4.thumbnail((100, 100))
    lunch_1_photo = ImageTk.PhotoImage(lunch_1)
    lunch_2_photo = ImageTk.PhotoImage(lunch_2)
    lunch_3_photo = ImageTk.PhotoImage(lunch_3)
    lunch_4_photo = ImageTk.PhotoImage(lunch_4)
    lunch_1_Lbl = Label(secondcont_frame, image=lunch_1_photo)
    lunch_2_Lbl = Label(secondcont_frame, image=lunch_2_photo)
    lunch_3_Lbl = Label(secondcont_frame, image=lunch_3_photo)
    lunch_4_Lbl = Label(secondcont_frame, image=lunch_4_photo)
    lunch_1_Lbl.grid(row=10, column=1, columnspan=2, pady=(8, 0))
    lunch_2_Lbl.grid(row=10, column=3, columnspan=2, pady=(8, 0))
    lunch_3_Lbl.grid(row=10, column=5, columnspan=2, pady=(8, 0))
    lunch_4_Lbl.grid(row=10, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    lunch_1_name = Label(secondcont_frame, text='Grilled Chicken Salad', font=('Kristen ITC', 9))
    lunch_2_name = Label(secondcont_frame, text='Quinoa and Roasted\nVegetable Bowl', font=('Kristen ITC', 9))
    lunch_3_name = Label(secondcont_frame, text='Turkey and Avocado\nWrap', font=('Kristen ITC', 9))
    lunch_4_name = Label(secondcont_frame, text='Caprese Salad', font=('Kristen ITC', 9))
    lunch_1_name.grid(row=11, column=1, columnspan=2, pady=(8, 0))
    lunch_2_name.grid(row=11, column=3, columnspan=2, pady=(8, 0))
    lunch_3_name.grid(row=11, column=5, columnspan=2, pady=(8, 0))
    lunch_4_name.grid(row=11, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    lunch_1_price = Label(secondcont_frame, text='₱550.00', font=('Arial', 11, 'bold'))
    lunch_2_price = Label(secondcont_frame, text='₱385.00', font=('Arial', 11, 'bold'))
    lunch_3_price = Label(secondcont_frame, text='₱120.00', font=('Arial', 11, 'bold'))
    lunch_4_price = Label(secondcont_frame, text='₱75.00', font=('Arial', 11, 'bold'))
    lunch_1_price.grid(row=12, column=1, columnspan=2)
    lunch_2_price.grid(row=12, column=3, columnspan=2)
    lunch_3_price.grid(row=12, column=5, columnspan=2)
    lunch_4_price.grid(row=12, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    LUorderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn1)
    LUorderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn2)
    LUorderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn3)
    LUorderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn4)
    LUorderBtn1.grid(row=13, column=1, columnspan=2)
    LUorderBtn2.grid(row=13, column=3, columnspan=2)
    LUorderBtn3.grid(row=13, column=5, columnspan=2)
    LUorderBtn4.grid(row=13, column=7, columnspan=2)

    # ==========QUANTITY========== #
    LUqty1 = IntVar()
    LUqty2 = IntVar()
    LUqty3 = IntVar()
    LUqty4 = IntVar()
    LUquantity1 = Entry(secondcont_frame, textvariable=LUqty1, font='Arial', width=2)
    LUquantity2 = Entry(secondcont_frame, textvariable=LUqty2, font='Arial', width=2)
    LUquantity3 = Entry(secondcont_frame, textvariable=LUqty3, font='Arial', width=2)
    LUquantity4 = Entry(secondcont_frame, textvariable=LUqty4, font='Arial', width=2)
    LUquantity1.grid(row=13, column=1, columnspan=2, padx=(90, 0))
    LUquantity2.grid(row=13, column=3, columnspan=2, padx=(90, 0))
    LUquantity3.grid(row=13, column=5, columnspan=2, padx=(90, 0))
    LUquantity4.grid(row=13, column=7, columnspan=2, padx=(90, 0))
    LUqty1.set(0)
    LUqty2.set(0)
    LUqty3.set(0)
    LUqty4.set(0)

    # THIS IS SECOND COLUMN IN LUNCH
    # ==========IMAGE========== #
    lunch_5 = Image.open(r'Foods\Lunch\lunch-5.png')
    lunch_6 = Image.open(r'Foods\Lunch\lunch-6.png')
    lunch_7 = Image.open(r'Foods\Lunch\lunch-7.png')
    lunch_8 = Image.open(r'Foods\Lunch\lunch-8.png')
    lunch_5.thumbnail((100, 100))
    lunch_6.thumbnail((100, 100))
    lunch_7.thumbnail((100, 100))
    lunch_8.thumbnail((100, 100))
    lunch_5_photo = ImageTk.PhotoImage(lunch_5)
    lunch_6_photo = ImageTk.PhotoImage(lunch_6)
    lunch_7_photo = ImageTk.PhotoImage(lunch_7)
    lunch_8_photo = ImageTk.PhotoImage(lunch_8)
    lunch_5_Lbl = Label(secondcont_frame, image=lunch_5_photo)
    lunch_6_Lbl = Label(secondcont_frame, image=lunch_6_photo)
    lunch_7_Lbl = Label(secondcont_frame, image=lunch_7_photo)
    lunch_8_Lbl = Label(secondcont_frame, image=lunch_8_photo)
    lunch_5_Lbl.grid(row=14, column=1, columnspan=2, pady=(8, 0))
    lunch_6_Lbl.grid(row=14, column=3, columnspan=2, pady=(8, 0))
    lunch_7_Lbl.grid(row=14, column=5, columnspan=2, pady=(8, 0))
    lunch_8_Lbl.grid(row=14, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    lunch_5_name = Label(secondcont_frame, text='Lentil Soup', font=('Kristen ITC', 9))
    lunch_6_name = Label(secondcont_frame, text='Grilled Salmon with\nSteamed Vegetables', font=('Kristen ITC', 9))
    lunch_7_name = Label(secondcont_frame, text='Quinoa Salad with\nChickpeas and Feta\nCheese', font=('Kristen ITC', 9))
    lunch_8_name = Label(secondcont_frame, text='Veggie Wrap with\nHummus', font=('Kristen ITC', 9))
    lunch_5_name.grid(row=15, column=1, columnspan=2, pady=(8, 0))
    lunch_6_name.grid(row=15, column=3, columnspan=2, pady=(8, 0))
    lunch_7_name.grid(row=15, column=5, columnspan=2, pady=(8, 0))
    lunch_8_name.grid(row=15, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    lunch_5_price = Label(secondcont_frame, text='₱110.00', font=('Arial', 11, 'bold'))
    lunch_6_price = Label(secondcont_frame, text='₱145.00', font=('Arial', 11, 'bold'))
    lunch_7_price = Label(secondcont_frame, text='₱600.00', font=('Arial', 11, 'bold'))
    lunch_8_price = Label(secondcont_frame, text='₱125.00', font=('Arial', 11, 'bold'))
    lunch_5_price.grid(row=16, column=1, columnspan=2)
    lunch_6_price.grid(row=16, column=3, columnspan=2)
    lunch_7_price.grid(row=16, column=5, columnspan=2)
    lunch_8_price.grid(row=16, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    LUorderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn5)
    LUorderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn6)
    LUorderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn7)
    LUorderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn8)
    LUorderBtn5.grid(row=17, column=1, columnspan=2)
    LUorderBtn6.grid(row=17, column=3, columnspan=2)
    LUorderBtn7.grid(row=17, column=5, columnspan=2)
    LUorderBtn8.grid(row=17, column=7, columnspan=2)

    # ==========QUANTITY========== #
    LUqty5 = IntVar()
    LUqty6 = IntVar()
    LUqty7 = IntVar()
    LUqty8 = IntVar()
    LUquantity5 = Entry(secondcont_frame, textvariable=LUqty5, font='Arial', width=2)
    LUquantity6 = Entry(secondcont_frame, textvariable=LUqty6, font='Arial', width=2)
    LUquantity7 = Entry(secondcont_frame, textvariable=LUqty7, font='Arial', width=2)
    LUquantity8 = Entry(secondcont_frame, textvariable=LUqty8, font='Arial', width=2)
    LUquantity5.grid(row=17, column=1, columnspan=2, padx=(90, 0))
    LUquantity6.grid(row=17, column=3, columnspan=2, padx=(90, 0))
    LUquantity7.grid(row=17, column=5, columnspan=2, padx=(90, 0))
    LUquantity8.grid(row=17, column=7, columnspan=2, padx=(90, 0))
    LUqty5.set(0)
    LUqty6.set(0)
    LUqty7.set(0)
    LUqty8.set(0)

    # ==========DINNER==========#
    dinnerLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Dinner')
    dinnerLbl.grid(row=18, column=0, columnspan=2, padx=(8, 0), pady=(18, 0))

    # THIS IS FIRST COLUMN IN DINNER
    # ==========IMAGE========== #
    dinner_1 = Image.open(r'Foods\Dinner\dinner-1.png')
    dinner_2 = Image.open(r'Foods\Dinner\dinner-2.png')
    dinner_3 = Image.open(r'Foods\Dinner\dinner-3.png')
    dinner_4 = Image.open(r'Foods\Dinner\dinner-4.png')
    dinner_1.thumbnail((100, 100))
    dinner_2.thumbnail((100, 100))
    dinner_3.thumbnail((100, 100))
    dinner_4.thumbnail((100, 100))
    dinner_1_photo = ImageTk.PhotoImage(dinner_1)
    dinner_2_photo = ImageTk.PhotoImage(dinner_2)
    dinner_3_photo = ImageTk.PhotoImage(dinner_3)
    dinner_4_photo = ImageTk.PhotoImage(dinner_4)
    dinner_1_Lbl = Label(secondcont_frame, image=dinner_1_photo)
    dinner_2_Lbl = Label(secondcont_frame, image=dinner_2_photo)
    dinner_3_Lbl = Label(secondcont_frame, image=dinner_3_photo)
    dinner_4_Lbl = Label(secondcont_frame, image=dinner_4_photo)
    dinner_1_Lbl.grid(row=19, column=1, columnspan=2, pady=(8, 0))
    dinner_2_Lbl.grid(row=19, column=3, columnspan=2, pady=(8, 0))
    dinner_3_Lbl.grid(row=19, column=5, columnspan=2, pady=(8, 0))
    dinner_4_Lbl.grid(row=19, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    dinner_1_name = Label(secondcont_frame, text='Grilled Chicken with\nRoasted Sweet Potatoes', font=('Kristen ITC', 9))
    dinner_2_name = Label(secondcont_frame, text='Spaghetti with\nMarinara Sauce', font=('Kristen ITC', 9))
    dinner_3_name = Label(secondcont_frame, text='Baked Salmon with\nQuinoa Pilaf', font=('Kristen ITC', 9))
    dinner_4_name = Label(secondcont_frame, text='Stir-Fried Tofu\nand Vegetables', font=('Kristen ITC', 9))
    dinner_1_name.grid(row=20, column=1, columnspan=2, pady=(8, 0))
    dinner_2_name.grid(row=20, column=3, columnspan=2, pady=(8, 0))
    dinner_3_name.grid(row=20, column=5, columnspan=2, pady=(8, 0))
    dinner_4_name.grid(row=20, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    dinner_1_price = Label(secondcont_frame, text='₱360.00', font=('Arial', 11, 'bold'))
    dinner_2_price = Label(secondcont_frame, text='₱167.00', font=('Arial', 11, 'bold'))
    dinner_3_price = Label(secondcont_frame, text='₱138.00', font=('Arial', 11, 'bold'))
    dinner_4_price = Label(secondcont_frame, text='₱322.00', font=('Arial', 11, 'bold'))
    dinner_1_price.grid(row=21, column=1, columnspan=2)
    dinner_2_price.grid(row=21, column=3, columnspan=2)
    dinner_3_price.grid(row=21, column=5, columnspan=2)
    dinner_4_price.grid(row=21, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DIorderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn1)
    DIorderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn2)
    DIorderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn3)
    DIorderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn4)
    DIorderBtn1.grid(row=22, column=1, columnspan=2)
    DIorderBtn2.grid(row=22, column=3, columnspan=2)
    DIorderBtn3.grid(row=22, column=5, columnspan=2)
    DIorderBtn4.grid(row=22, column=7, columnspan=2)

    # ==========QUANTITY========== #
    DIqty1 = IntVar()
    DIqty2 = IntVar()
    DIqty3 = IntVar()
    DIqty4 = IntVar()
    DIquantity1 = Entry(secondcont_frame, textvariable=DIqty1, font='Arial', width=2)
    DIquantity2 = Entry(secondcont_frame, textvariable=DIqty2, font='Arial', width=2)
    DIquantity3 = Entry(secondcont_frame, textvariable=DIqty3, font='Arial', width=2)
    DIquantity4 = Entry(secondcont_frame, textvariable=DIqty4, font='Arial', width=2)
    DIquantity1.grid(row=22, column=1, columnspan=2, padx=(90, 0))
    DIquantity2.grid(row=22, column=3, columnspan=2, padx=(90, 0))
    DIquantity3.grid(row=22, column=5, columnspan=2, padx=(90, 0))
    DIquantity4.grid(row=22, column=7, columnspan=2, padx=(90, 0))
    DIqty1.set(0)
    DIqty2.set(0)
    DIqty3.set(0)
    DIqty4.set(0)

    # THIS IS SECOND COLUMN IN DINNER
    # ==========IMAGE========== #
    dinner_5 = Image.open(r'Foods\Dinner\dinner-5.png')
    dinner_6 = Image.open(r'Foods\Dinner\dinner-6.png')
    dinner_7 = Image.open(r'Foods\Dinner\dinner-7.png')
    dinner_8 = Image.open(r'Foods\Dinner\dinner-8.png')
    dinner_5.thumbnail((100, 100))
    dinner_6.thumbnail((100, 100))
    dinner_7.thumbnail((100, 100))
    dinner_8.thumbnail((100, 100))
    dinner_5_photo = ImageTk.PhotoImage(dinner_5)
    dinner_6_photo = ImageTk.PhotoImage(dinner_6)
    dinner_7_photo = ImageTk.PhotoImage(dinner_7)
    dinner_8_photo = ImageTk.PhotoImage(dinner_8)
    dinner_5_Lbl = Label(secondcont_frame, image=dinner_5_photo)
    dinner_6_Lbl = Label(secondcont_frame, image=dinner_6_photo)
    dinner_7_Lbl = Label(secondcont_frame, image=dinner_7_photo)
    dinner_8_Lbl = Label(secondcont_frame, image=dinner_8_photo)
    dinner_5_Lbl.grid(row=23, column=1, columnspan=2, pady=(8, 0))
    dinner_6_Lbl.grid(row=23, column=3, columnspan=2, pady=(8, 0))
    dinner_7_Lbl.grid(row=23, column=5, columnspan=2, pady=(8, 0))
    dinner_8_Lbl.grid(row=23, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    dinner_5_name = Label(secondcont_frame, text='Shrimp and Vegetable\nKebabs', font=('Kristen ITC', 9))
    dinner_6_name = Label(secondcont_frame, text='Stuffed Bell Peppers', font=('Kristen ITC', 9))
    dinner_7_name = Label(secondcont_frame, text='Eggplant Parmesan', font=('Kristen ITC', 9))
    dinner_8_name = Label(secondcont_frame, text='Mexican-Style\nChicken Fajitas', font=('Kristen ITC', 9))
    dinner_5_name.grid(row=24, column=1, columnspan=2, pady=(8, 0))
    dinner_6_name.grid(row=24, column=3, columnspan=2, pady=(8, 0))
    dinner_7_name.grid(row=24, column=5, columnspan=2, pady=(8, 0))
    dinner_8_name.grid(row=24, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    dinner_5_price = Label(secondcont_frame, text='₱449.00', font=('Arial', 11, 'bold'))
    dinner_6_price = Label(secondcont_frame, text='₱389.00', font=('Arial', 11, 'bold'))
    dinner_7_price = Label(secondcont_frame, text='₱325.00', font=('Arial', 11, 'bold'))
    dinner_8_price = Label(secondcont_frame, text='₱299.00', font=('Arial', 11, 'bold'))
    dinner_5_price.grid(row=25, column=1, columnspan=2)
    dinner_6_price.grid(row=25, column=3, columnspan=2)
    dinner_7_price.grid(row=25, column=5, columnspan=2)
    dinner_8_price.grid(row=25, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DIorderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn5)
    DIorderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn6)
    DIorderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn7)
    DIorderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=dinner_orderbtn8)
    DIorderBtn5.grid(row=26, column=1, columnspan=2)
    DIorderBtn6.grid(row=26, column=3, columnspan=2)
    DIorderBtn7.grid(row=26, column=5, columnspan=2)
    DIorderBtn8.grid(row=26, column=7, columnspan=2)

    # ==========QUANTITY========== #
    DIqty5 = IntVar()
    DIqty6 = IntVar()
    DIqty7 = IntVar()
    DIqty8 = IntVar()
    DIquantity5 = Entry(secondcont_frame, textvariable=DIqty5, font='Arial', width=2)
    DIquantity6 = Entry(secondcont_frame, textvariable=DIqty6, font='Arial', width=2)
    DIquantity7 = Entry(secondcont_frame, textvariable=DIqty7, font='Arial', width=2)
    DIquantity8 = Entry(secondcont_frame, textvariable=DIqty8, font='Arial', width=2)
    DIquantity5.grid(row=26, column=1, columnspan=2, padx=(90, 0))
    DIquantity6.grid(row=26, column=3, columnspan=2, padx=(90, 0))
    DIquantity7.grid(row=26, column=5, columnspan=2, padx=(90, 0))
    DIquantity8.grid(row=26, column=7, columnspan=2, padx=(90, 0))
    DIqty5.set(0)
    DIqty6.set(0)
    DIqty7.set(0)
    DIqty8.set(0)

    # ==========DRINKS========== #
    drinkLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Drinks')
    drinkLbl.grid(row=27, column=0, columnspan=2, padx=(8, 0), pady=(18, 0))

    # THIS IS FIRST COLUMN IN DRINKS
    # ==========IMAGE========== #
    drink_1 = Image.open(r'Foods\Drinks\drink-1.png')
    drink_2 = Image.open(r'Foods\Drinks\drink-2.png')
    drink_3 = Image.open(r'Foods\Drinks\drink-3.png')
    drink_4 = Image.open(r'Foods\Drinks\drink-4.png')
    drink_1.thumbnail((100, 100))
    drink_2.thumbnail((100, 100))
    drink_3.thumbnail((100, 100))
    drink_4.thumbnail((100, 100))
    drink_1_photo = ImageTk.PhotoImage(drink_1)
    drink_2_photo = ImageTk.PhotoImage(drink_2)
    drink_3_photo = ImageTk.PhotoImage(drink_3)
    drink_4_photo = ImageTk.PhotoImage(drink_4)
    drink_1_Lbl = Label(secondcont_frame, image=drink_1_photo)
    drink_2_Lbl = Label(secondcont_frame, image=drink_2_photo)
    drink_3_Lbl = Label(secondcont_frame, image=drink_3_photo)
    drink_4_Lbl = Label(secondcont_frame, image=drink_4_photo)
    drink_1_Lbl.grid(row=28, column=1, columnspan=2, pady=(8, 0))
    drink_2_Lbl.grid(row=28, column=3, columnspan=2, pady=(8, 0))
    drink_3_Lbl.grid(row=28, column=5, columnspan=2, pady=(8, 0))
    drink_4_Lbl.grid(row=28, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    drink_1_name = Label(secondcont_frame, text='Coca-Cola', font=('Kristen ITC', 9))
    drink_2_name = Label(secondcont_frame, text='Pineapple Juice', font=('Kristen ITC', 9))
    drink_3_name = Label(secondcont_frame, text='Mango Lassi', font=('Kristen ITC', 9))
    drink_4_name = Label(secondcont_frame, text='Fruit Punch', font=('Kristen ITC', 9))
    drink_1_name.grid(row=29, column=1, columnspan=2, pady=(8, 0))
    drink_2_name.grid(row=29, column=3, columnspan=2, pady=(8, 0))
    drink_3_name.grid(row=29, column=5, columnspan=2, pady=(8, 0))
    drink_4_name.grid(row=29, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    drink_1_price = Label(secondcont_frame, text='₱37.00', font=('Arial', 11, 'bold'))
    drink_2_price = Label(secondcont_frame, text='₱37.00', font=('Arial', 11, 'bold'))
    drink_3_price = Label(secondcont_frame, text='₱45.00', font=('Arial', 11, 'bold'))
    drink_4_price = Label(secondcont_frame, text='₱59.00', font=('Arial', 11, 'bold'))
    drink_1_price.grid(row=30, column=1, columnspan=2)
    drink_2_price.grid(row=30, column=3, columnspan=2)
    drink_3_price.grid(row=30, column=5, columnspan=2)
    drink_4_price.grid(row=30, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DRorderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn1)
    DRorderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn2)
    DRorderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn3)
    DRorderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn4)
    DRorderBtn1.grid(row=31, column=1, columnspan=2)
    DRorderBtn2.grid(row=31, column=3, columnspan=2)
    DRorderBtn3.grid(row=31, column=5, columnspan=2)
    DRorderBtn4.grid(row=31, column=7, columnspan=2)

    # ==========QUANTITY========== #
    DRqty1 = IntVar()
    DRqty2 = IntVar()
    DRqty3 = IntVar()
    DRqty4 = IntVar()
    DRquantity1 = Entry(secondcont_frame, textvariable=DRqty1, font='Arial', width=2)
    DRquantity2 = Entry(secondcont_frame, textvariable=DRqty2, font='Arial', width=2)
    DRquantity3 = Entry(secondcont_frame, textvariable=DRqty3, font='Arial', width=2)
    DRquantity4 = Entry(secondcont_frame, textvariable=DRqty4, font='Arial', width=2)
    DRquantity1.grid(row=31, column=1, columnspan=2, padx=(90, 0))
    DRquantity2.grid(row=31, column=3, columnspan=2, padx=(90, 0))
    DRquantity3.grid(row=31, column=5, columnspan=2, padx=(90, 0))
    DRquantity4.grid(row=31, column=7, columnspan=2, padx=(90, 0))
    DRqty1.set(0)
    DRqty2.set(0)
    DRqty3.set(0)
    DRqty4.set(0)

    # THIS IS SECOND COLUMN IN DRINKS
    # ==========IMAGE========== #
    drink_5 = Image.open(r'Foods\Drinks\drink-5.png')
    drink_6 = Image.open(r'Foods\Drinks\drink-6.png')
    drink_7 = Image.open(r'Foods\Drinks\drink-7.png')
    drink_8 = Image.open(r'Foods\Drinks\drink-8.png')
    drink_5.thumbnail((100, 100))
    drink_6.thumbnail((100, 100))
    drink_7.thumbnail((100, 100))
    drink_8.thumbnail((100, 100))
    drink_5_photo = ImageTk.PhotoImage(drink_5)
    drink_6_photo = ImageTk.PhotoImage(drink_6)
    drink_7_photo = ImageTk.PhotoImage(drink_7)
    drink_8_photo = ImageTk.PhotoImage(drink_8)
    drink_5_Lbl = Label(secondcont_frame, image=drink_5_photo)
    drink_6_Lbl = Label(secondcont_frame, image=drink_6_photo)
    drink_7_Lbl = Label(secondcont_frame, image=drink_7_photo)
    drink_8_Lbl = Label(secondcont_frame, image=drink_8_photo)
    drink_5_Lbl.grid(row=32, column=1, columnspan=2, pady=(8, 0))
    drink_6_Lbl.grid(row=32, column=3, columnspan=2, pady=(8, 0))
    drink_7_Lbl.grid(row=32, column=5, columnspan=2, pady=(8, 0))
    drink_8_Lbl.grid(row=32, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    dinner_5_name = Label(secondcont_frame, text='Sparkling Lemonade', font=('Kristen ITC', 9))
    dinner_6_name = Label(secondcont_frame, text='Pomegranate Spritzer', font=('Kristen ITC', 9))
    dinner_7_name = Label(secondcont_frame, text='Virgin Mojito', font=('Kristen ITC', 9))
    dinner_8_name = Label(secondcont_frame, text='Cucumber Cooler', font=('Kristen ITC', 9))
    dinner_5_name.grid(row=33, column=1, columnspan=2, pady=(8, 0))
    dinner_6_name.grid(row=33, column=3, columnspan=2, pady=(8, 0))
    dinner_7_name.grid(row=33, column=5, columnspan=2, pady=(8, 0))
    dinner_8_name.grid(row=33, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    drink_5_price = Label(secondcont_frame, text='₱44.00', font=('Arial', 11, 'bold'))
    drink_6_price = Label(secondcont_frame, text='₱66.00', font=('Arial', 11, 'bold'))
    drink_7_price = Label(secondcont_frame, text='₱83.00', font=('Arial', 11, 'bold'))
    drink_8_price = Label(secondcont_frame, text='₱77.00', font=('Arial', 11, 'bold'))
    drink_5_price.grid(row=34, column=1, columnspan=2)
    drink_6_price.grid(row=34, column=3, columnspan=2)
    drink_7_price.grid(row=34, column=5, columnspan=2)
    drink_8_price.grid(row=34, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DRorderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn5)
    DRorderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn6)
    DRorderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn7)
    DRorderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn8)
    DRorderBtn5.grid(row=35, column=1, columnspan=2, pady=(0, 15))
    DRorderBtn6.grid(row=35, column=3, columnspan=2, pady=(0, 15))
    DRorderBtn7.grid(row=35, column=5, columnspan=2, pady=(0, 15))
    DRorderBtn8.grid(row=35, column=7, columnspan=2, pady=(0, 15))

    # ==========QUANTITY========== #
    DRqty5 = IntVar()
    DRqty6 = IntVar()
    DRqty7 = IntVar()
    DRqty8 = IntVar()
    DRquantity5 = Entry(secondcont_frame, textvariable=DRqty5, font='Arial', width=2)
    DRquantity6 = Entry(secondcont_frame, textvariable=DRqty6, font='Arial', width=2)
    DRquantity7 = Entry(secondcont_frame, textvariable=DRqty7, font='Arial', width=2)
    DRquantity8 = Entry(secondcont_frame, textvariable=DRqty8, font='Arial', width=2)
    DRquantity5.grid(row=35, column=1, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRquantity6.grid(row=35, column=3, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRquantity7.grid(row=35, column=5, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRquantity8.grid(row=35, column=7, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRqty5.set(0)
    DRqty6.set(0)
    DRqty7.set(0)
    DRqty8.set(0)

    # ==============================DELIVERY-WINDOW-FOOTER============================== #
    # ==========SHOW-ORDERS-WINDOW========== #
    def show_or():
        show_win = Toplevel()
        show_win.title('KUB-KUB')
        width = 600
        height = 500
        x_pos = (show_win.winfo_screenwidth() - width) // 2
        y_pos = (show_win.winfo_screenwidth() - height) // 5
        show_winGeometry = f'{width}x{height}+{x_pos}+{y_pos}'
        show_win.geometry(show_winGeometry)
        show_win.resizable(False, False)
        show_win.iconbitmap('Kub-Kub-Icon.ico')

        # ==========SHOW-ORDER-WINDOW-NAVBAR========== #
        shownav_frame = Frame(show_win)
        shownav_frame.pack(side=TOP, fill=X)
        current_orFrame = Frame(shownav_frame, width=600, height=80, bg='#4b91f1')
        current_orFrame.grid(row=0, column=0, columnspan=5)
        current_orLbl = Label(shownav_frame, text='Current Orders', font=('Kristen ITC', 16), bg='#4b91f1')
        current_orLbl.grid(row=0, column=2)

        # ==========SHOW-ORDERS-WINDOW-SCROLLBAR========== #
        cont_frame = Frame(show_win)
        cont_frame.pack(fill=BOTH, expand=1)
        cont_canvas = Canvas(cont_frame)
        cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
        cont_scrollbar.pack(side=RIGHT, fill=Y)
        cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
        cont_canvas.bind('<Configure>', lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
        secondcont_frame = Frame(cont_canvas)
        cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

        # ==========SHOW-LABELS========== #
        showOrdetails = Frame(secondcont_frame)
        showOrdetails.pack(side=TOP, fill=X)
        showOrFrame = Frame(showOrdetails, width=600)
        showOrFrame.grid(row=0, column=0, columnspan=8)
        foodLbl = Label(showOrdetails, text='Food', font=('Kristen ITC', 12, 'bold'))
        priceLbl = Label(showOrdetails, text='Price', font=('Kristen ITC', 12, 'bold'))
        quantityLbl = Label(showOrdetails, text='Quantity', font=('Kristen ITC', 12, 'bold'))
        foodLbl.grid(row=0, column=0, columnspan=2)
        priceLbl.grid(row=0, column=2, columnspan=2)
        quantityLbl.grid(row=0, column=4, columnspan=2)

        # ==========REMOVE-SPECIFIC-ORDER========== #
        def remove_or(index):
            show_orders.pop(index)
            minus_totalprice = total_price.get() - order_prices[index]
            total_price.set(minus_totalprice)
            order_prices.pop(index)
            dis_or()
            show_win.destroy()
            show_or()

        # ==========SHOW-ORDERS========== #
        def dis_or():
            count = 1
            for index, i in enumerate(show_orders):
                showOr = i.split(',')

                foodDis = Label(showOrdetails, text=showOr[0], font=('Kristen ITC', 12))
                priceDis = Label(showOrdetails, text=showOr[1], font=('Kristen ITC', 12))
                quantDis = Label(showOrdetails, text=showOr[2].strip(), font=('Kristen ITC', 12))
                removeBtn = Button(showOrdetails, text='Remove', font=('Kristen ITC', 10), bg='#4b91f1', command=lambda index=index: remove_or(index))
                foodDis.grid(row=count, column=0, columnspan=2)
                priceDis.grid(row=count, column=2, columnspan=2)
                quantDis.grid(row=count, column=4, columnspan=2)
                removeBtn.grid(row=count, column=6, columnspan=2)

                count += 1

        dis_or()

        # ==========SHOW-ORDERS-WINDOW-FOOTER========== #
        footer_frame = Frame(show_win)
        footer_frame.pack(side=BOTTOM, fill=X)
        footer = Frame(footer_frame, width=600, height=80, bg='#4b91f1')
        footer.grid(row=0, column=0, columnspan=6)
        show_total = Label(footer_frame, text=f'Total: ₱{total_price.get()}', font=('Kristen ITC', 16), bg='#4b91f1')
        show_total.grid(row=0, column=2, columnspan=2)

    # ==========PLACE-ORDER========== #
    def place_order():
        if show_orders == []:
            messagebox.showerror('KUB-KUB', 'You have no order.')
        else:
            placeOr_win = Toplevel()
            placeOr_win.title('KUB-KUB')
            placeOr_win.config(bg='#4b91f1')
            placeOr_width = 600
            placeOr_height = 500
            x_pos = (placeOr_win.winfo_screenwidth() - placeOr_width) // 2
            y_pos = (placeOr_win.winfo_screenwidth() - placeOr_height) // 6
            placeOr_winGeometry = f'{placeOr_width}x{placeOr_height}+{x_pos}+{y_pos}'
            placeOr_win.geometry(placeOr_winGeometry)
            placeOr_win.resizable(False, False)
            placeOr_win.iconbitmap('Kub-Kub-Icon.ico')

            # ==========SUBMIT-ORDER========== #
            def submit_order():
                if cusName.get() == '':
                    messagebox.showerror('KUB-KUB', 'Fill the missing information.')
                elif cusAdd.get() == '':
                    messagebox.showerror('KUB-KUB', 'Fill the missing information.')
                elif cusCont.get() == '':
                    messagebox.showerror('KUB-KUB', 'Fill the missing information.')
                else:
                    placeOr_win.withdraw()
                    confOr_win = Toplevel()
                    confOr_win.title('KUB-KUB')
                    confOr_width = 600
                    confOr_height = 500
                    x_pos = (confOr_win.winfo_screenwidth() - confOr_width) // 2
                    y_pos = (confOr_win.winfo_screenwidth() - confOr_height) // 6
                    confOr_winGeometry = f'{confOr_width}x{confOr_height}+{x_pos}+{y_pos}'
                    confOr_win.geometry(confOr_winGeometry)
                    confOr_win.resizable(False, False)
                    confOr_win.iconbitmap('Kub-Kub-Icon.ico')

                    # ==========TOP-FRAME========== #
                    TconfOr_frame1 = Frame(confOr_win)
                    TconfOr_frame1.pack(side=TOP, fill=X)
                    TconfOr_frame2 = Frame(TconfOr_frame1, width=600, height=80, bg='#4b91f1')
                    TconfOr_frame2.grid(row=0, column=0, columnspan=6)
                    confirmLbl = Label(TconfOr_frame1, text='Confirmation', font=('Kristen ITC', 16, 'bold'), bg='#4b91f1')
                    confirmLbl.grid(row=0, column=2, columnspan=2)

                    # ==========SUBMIT-ORDER-WINDOW-SCROLLBAR========== #
                    cont_frame = Frame(confOr_win)
                    cont_frame.pack(fill=BOTH, expand=1)
                    cont_canvas = Canvas(cont_frame)
                    cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                    cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
                    cont_scrollbar.pack(side=RIGHT, fill=Y)
                    cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
                    cont_canvas.bind('<Configure>', lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
                    secondcont_frame = Frame(cont_canvas)
                    cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

                    # ==========CENTER-FRAME========== #
                    CconfOr_frame1 = Frame(secondcont_frame)
                    CconfOr_frame1.grid(row=0, column=0, columnspan=10)

                    foodLbl = Label(CconfOr_frame1, text='Food', font=('Kristen ITC', 12, 'bold'))
                    priceLbl = Label(CconfOr_frame1, text='Price', font=('Kristen ITC', 12, 'bold'))
                    quantityLbl = Label(CconfOr_frame1, text='Quantity', font=('Kristen ITC', 12, 'bold'))
                    foodLbl.grid(row=0, column=1, columnspan=2, padx=70)
                    priceLbl.grid(row=0, column=3, columnspan=2, padx=70)
                    quantityLbl.grid(row=0, column=5, columnspan=2, padx=70)

                    count = 1
                    for i in show_orders:
                        showOr = i.split(',')

                        foodDis = Label(CconfOr_frame1, text=showOr[0], font=('Kristen ITC', 12))
                        priceDis = Label(CconfOr_frame1, text=showOr[1], font=('Kristen ITC', 12))
                        quantDis = Label(CconfOr_frame1, text=showOr[2].strip(), font=('Kristen ITC', 12))
                        foodDis.grid(row=count, column=1, columnspan=2)
                        priceDis.grid(row=count, column=3, columnspan=2)
                        quantDis.grid(row=count, column=5, columnspan=2)

                        count += 1

                    # ==========BOTTOM-FRAME========== #
                    # ==========CONFIRM-ORDER========== #
                    def confirm_order():
                        personal_infos = 'DELIVERY'+', '+cusName.get()+', '+cusAdd.get()+', '+cusCont.get()+', '+str(total_price.get())+'\n'
                        file_infos = open('personal infos.txt', 'a')
                        file_infos.write(personal_infos)
                        file_infos.close()
                        file_orders = open('orders.txt', 'a')
                        orders = str(show_orders)+'\n'
                        file_orders.write(str(orders))
                        file_orders.close()
                        show_orders.clear()
                        order_prices.clear()
                        total_price.set(0.00)
                        confOr_win.destroy()
                        messagebox.showinfo('KUB-KUB', 'Your order is now processing. Wait for the rider to contact you. Thank you for ordering!')

                    BconfOr_frame1 = Frame(confOr_win)
                    BconfOr_frame1.pack(side=BOTTOM, fill=X)
                    BconfOr_frame2 = Frame(BconfOr_frame1, width=600, height=80, bg='#4b91f1')
                    BconfOr_frame2.grid(row=0, column=0, columnspan=6)
                    confirmBtn = Button(BconfOr_frame1, text='Confirm Order', font=('Kristen ITC', 12, 'bold'), command=confirm_order)
                    confirmtotal = Label(BconfOr_frame1, text=f'Total: ₱{total_price.get()}', font=('Kristen ITC', 14, 'bold'), bg='#4b91f1')
                    confirmBtn.grid(row=0, column=1, columnspan=2)
                    confirmtotal.grid(row=0, column=3, columnspan=2)

            placeOr_frame = Frame(placeOr_win, width=600, height=500, bg='#4b91f1')
            placeOr_frame.pack(fill=Y)

            cusName = StringVar()
            cusAdd = StringVar()
            cusCont = StringVar()
            NameEnt = Entry(placeOr_frame, width=40, textvariable=cusName, justify='center', font=('Kristen ITC', 12))
            NameLbl = Label(placeOr_frame, text='Name', font=('Kristen ITC', 12), bg='#4b91f1')
            AddressEnt = Entry(placeOr_frame, width=40, textvariable=cusAdd, justify='center', font=('Kristen ITC', 12))
            AddressLbl = Label(placeOr_frame, text='Address', font=('Kristen ITC', 12), bg='#4b91f1')
            ContEnt = Entry(placeOr_frame, width=40, textvariable=cusCont, justify='center', font=('Kristen ITC', 12))
            ContLbl = Label(placeOr_frame, text='Contact Number', font=('Kristen ITC', 12), bg='#4b91f1')
            CODLbl = Label(placeOr_frame, text='Mode of Payment: Cash on Delivery', font=('Kristen ITC', 12), bg='#4b91f1')
            submitBtn = Button(placeOr_frame, text='Submit', font=('Kristen ITC', 12, 'bold'), command=submit_order)
            NameEnt.grid(row=0, column=3, columnspan=3, pady=(80, 0))
            NameLbl.grid(row=1, column=4)
            AddressEnt.grid(row=2, column=3, columnspan=3, pady=(40, 0))
            AddressLbl.grid(row=3, column=4)
            ContEnt.grid(row=4, column=3, columnspan=3, pady=(40, 0))
            ContLbl.grid(row=5, column=4)
            CODLbl.grid(row=6, column=4, pady=(40, 0))
            submitBtn.grid(row=7, column=4, pady=(40, 0))

    total_price = DoubleVar()
    current_val = DoubleVar()
    footer_frame = Frame(del_win)
    footer_frame.pack(side=BOTTOM, fill=X)
    footer = Frame(footer_frame, width=800, height=80, bg='#4b91f1')
    footer.grid(row=0, column=0, columnspan=6)
    place_orderBtn = Button(footer_frame, text='Place Order', font=('Kristen ITC', 10, 'bold'), command=place_order)
    place_orderBtn.grid(row=0, column=0, columnspan=2, padx=(8, 0), sticky='w')
    showBtn = Button(footer_frame, text='Show', font=('Kristen ITC', 10, 'bold'), command=show_or)
    showBtn.grid(row=0, column=4, padx=(250, 0))
    totalLbl = Label(footer_frame, text='Total: ₱', font=('Kristen ITC', 16), bg='#4b91f1')
    totalLbl.grid(row=0, column=4, padx=(420, 0))
    total_price.set(0.00)
    totalpriceEnt = Entry(footer_frame, textvariable=total_price, state='readonly', font=('Kristen ITC', 16), readonlybackground='#4b91f1', width=10)
    totalpriceEnt.grid(row=0, column=5, padx=(0, 50))

    # ==============================TERMINATE-PROGRAM============================== #
    def terminate_program():
        main.destroy()
    del_win.protocol('WM_DELETE_WINDOW', terminate_program)

    del_win.mainloop()


# ==============================PICKUP-WINDOW============================== #
def pickup_window():
    main.withdraw()
    pick_win = Toplevel()
    pick_win.title('KUB-KUB')
    pickwin_width = 800
    pickwin_height = 500
    x_pos = (pick_win.winfo_screenwidth() - pickwin_width) // 2
    y_pos = (pick_win.winfo_screenwidth() - pickwin_height) // 6
    pickwinGeometry = f'{pickwin_width}x{pickwin_height}+{x_pos}+{y_pos}'
    pick_win.geometry(pickwinGeometry)
    pick_win.resizable(False, False)
    pick_win.iconbitmap('Kub-Kub-Icon.ico')

    show_orders = []
    order_prices = []

    # ==============================PICKUP-WINDOW-NAVBAR============================== #
    def return_to_main():
        pick_win.destroy()
        main.deiconify()

    nav_frame = Frame(pick_win)
    nav_frame.pack(side=TOP, fill=X)
    navbar = Frame(nav_frame, width=800, height=80, bg='#4b91f1')
    navbar.grid(row=0, column=0, columnspan=6)
    logo_img = Image.open('Kub-Kub Logo.jpg')
    logo_img.thumbnail((100, 70))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo = Label(nav_frame, image=logo_photo)
    logo.grid(row=0, column=0, padx=(8, 0), columnspan=2, sticky='w')
    returnBtn = Button(nav_frame, text='Home', font=('Kristen ITC', 10, 'bold'), command=return_to_main)
    returnBtn.grid(row=0, column=5)

    # ==============================PICKUP-WINDOW-SCROLLBAR============================== #
    cont_frame = Frame(pick_win)
    cont_frame.pack(fill=BOTH, expand=1)
    cont_canvas = Canvas(cont_frame)
    cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
    cont_scrollbar.pack(side=RIGHT, fill=Y)
    cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
    cont_canvas.bind('<Configure>', lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
    secondcont_frame = Frame(cont_canvas)
    cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

    # ==============================PICKUP-WINDOW-CONTENT============================== #
    # ==========BREAKFAST-CALCULATIONS========== #
    def bf_orderbtn1():
        if BFquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty1.set(0)
        elif BFquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty1.set(0)
        elif int(BFquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty1.set(0)
        elif int(BFquantity1.get()) > 0 and int(BFquantity1.get()) <= 50:
            bf_1_total = int(BFquantity1.get()) * 185.00
            current_val.set(bf_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Oatmeal with Berries\nand Nuts'+','+f'185.00'+','+f'{BFquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_1_total
            order_prices.append(food_price)

            BFqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty1.set(0)

    def bf_orderbtn2():
        if BFquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty2.set(0)
        elif BFquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty2.set(0)
        elif int(BFquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty2.set(0)
        elif int(BFquantity2.get()) > 0 and int(BFquantity2.get()) <= 50:
            bf_2_total = int(BFquantity2.get()) * 35.00
            current_val.set(bf_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Avocado Toast'+','+'35.00'+','+f'{BFquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_2_total
            order_prices.append(food_price)

            BFqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty2.set(0)

    def bf_orderbtn3():
        if BFquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty3.set(0)
        elif BFquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty3.set(0)
        elif int(BFquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty3.set(0)
        elif int(BFquantity3.get()) > 0 and int(BFquantity3.get()) <= 50:
            bf_3_total = int(BFquantity3.get()) * 120.00
            current_val.set(bf_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Greek Yogurt with\nGranola with Honey'+','+'120.00'+','+f'{BFquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_3_total
            order_prices.append(food_price)

            BFqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty3.set(0)

    def bf_orderbtn4():
        if BFquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty4.set(0)
        elif BFquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty4.set(0)
        elif int(BFquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty4.set(0)
        elif int(BFquantity4.get()) > 0 and int(BFquantity4.get()) <= 50:
            bf_4_total = int(BFquantity4.get()) * 99.00
            current_val.set(bf_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Veggie Omelet'+','+'99.00'+','+f'{BFquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_4_total
            order_prices.append(food_price)

            BFqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty4.set(0)

    def bf_orderbtn5():
        if BFquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty5.set(0)
        elif BFquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty5.set(0)
        elif int(BFquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty5.set(0)
        elif int(BFquantity5.get()) > 0 and int(BFquantity5.get()) <= 50:
            bf_5_total = int(BFquantity5.get()) * 299.00
            current_val.set(bf_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Smoothie Bowl'+','+'299.00'+','+f'{BFquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_5_total
            order_prices.append(food_price)

            BFqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty5.set(0)

    def bf_orderbtn6():
        if BFquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty6.set(0)
        elif BFquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty6.set(0)
        elif int(BFquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty6.set(0)
        elif int(BFquantity6.get()) > 0 and int(BFquantity6.get()) <= 50:
            bf_6_total = int(BFquantity6.get()) * 150.00
            current_val.set(bf_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Whole Grain Pancakes\nwith Maple Syrup'+','+'150.00'+','+f'{BFquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_6_total
            order_prices.append(food_price)

            BFqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty6.set(0)

    def bf_orderbtn7():
        if BFquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty7.set(0)
        elif BFquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty7.set(0)
        elif int(BFquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty7.set(0)
        elif int(BFquantity7.get()) > 0 and int(BFquantity7.get()) <= 50:
            bf_7_total = int(BFquantity7.get()) * 175.00
            current_val.set(bf_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Breakfast Burrito'+','+'175.00'+','+f'{BFquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_7_total
            order_prices.append(food_price)

            BFqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty7.set(0)

    def bf_orderbtn8():
        if BFquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty8.set(0)
        elif BFquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            BFqty8.set(0)
        elif int(BFquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            BFqty8.set(0)
        elif int(BFquantity8.get()) > 0 and int(BFquantity8.get()) <= 50:
            bf_8_total = int(BFquantity8.get()) * 250.00
            current_val.set(bf_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Quinoa Breakfast Bowl'+','+'250.00'+','+f'{BFquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = bf_8_total
            order_prices.append(food_price)

            BFqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            BFqty8.set(0)

    # ==========LUNCH-CALCULATIONS========== #
    def lunch_orderbtn1():
        if LUquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty1.set(0)
        elif LUquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty1.set(0)
        elif int(LUquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty1.set(0)
        elif int(LUquantity1.get()) > 0 and int(LUquantity1.get()) <= 50:
            lunch_1_total = int(LUquantity1.get()) * 550.00
            current_val.set(lunch_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Grilled Chicken Salad'+','+'550.00'+','+f'{LUquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_1_total
            order_prices.append(food_price)

            LUqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty1.set(0)

    def lunch_orderbtn2():
        if LUquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty2.set(0)
        elif LUquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty2.set(0)
        elif int(LUquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty2.set(0)
        elif int(LUquantity2.get()) > 0 and int(LUquantity2.get()) <= 50:
            lunch_2_total = int(LUquantity2.get()) * 385.00
            current_val.set(lunch_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Quinoa and Roasted\nVegetable Bowl'+','+'385.00'+','+f'{LUquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_2_total
            order_prices.append(food_price)

            LUqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty2.set(0)

    def lunch_orderbtn3():
        if LUquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty3.set(0)
        elif LUquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty3.set(0)
        elif int(LUquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty3.set(0)
        elif int(LUquantity3.get()) > 0 and int(LUquantity3.get()) <= 50:
            lunch_3_total = int(LUquantity3.get()) * 120.00
            current_val.set(lunch_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Turkey and Avocado\nWrap'+','+'120.00'+','+f'{LUquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_3_total
            order_prices.append(food_price)

            LUqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty3.set(0)

    def lunch_orderbtn4():
        if LUquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty4.set(0)
        elif LUquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty4.set(0)
        elif int(LUquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty4.set(0)
        elif int(LUquantity4.get()) > 0 and int(LUquantity4.get()) <= 50:
            lunch_4_total = int(LUquantity4.get()) * 75.00
            current_val.set(lunch_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Caprese Salad'+','+'75.00'+','+f'{LUquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_4_total
            order_prices.append(food_price)

            LUqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty4.set(0)

    def lunch_orderbtn5():
        if LUquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty5.set(0)
        elif LUquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty5.set(0)
        elif int(LUquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty5.set(0)
        elif int(LUquantity5.get()) > 0 and int(LUquantity5.get()) <= 50:
            lunch_5_total = int(LUquantity5.get()) * 110.00
            current_val.set(lunch_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Lentil Soup'+','+'110.00'+','+f'{LUquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_5_total
            order_prices.append(food_price)

            LUqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty5.set(0)

    def lunch_orderbtn6():
        if LUquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty6.set(0)
        elif LUquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty6.set(0)
        elif int(LUquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty6.set(0)
        elif int(LUquantity6.get()) > 0 and int(LUquantity6.get()) <= 50:
            lunch_6_total = int(LUquantity6.get()) * 145.00
            current_val.set(lunch_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Grilled Salmon with\nSteamed Vegetables'+','+'145.00'+','+f'{LUquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_6_total
            order_prices.append(food_price)

            LUqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty6.set(0)

    def lunch_orderbtn7():
        if LUquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty7.set(0)
        elif LUquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty7.set(0)
        elif int(LUquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty7.set(0)
        elif int(LUquantity7.get()) > 0 and int(LUquantity7.get()) <= 50:
            lunch_7_total = int(LUquantity7.get()) * 600.00
            current_val.set(lunch_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Quinoa Salad with\nChickpeas and Feta\nCheese'+','+'600.00'+','+f'{LUquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_7_total
            order_prices.append(food_price)

            LUqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty7.set(0)

    def lunch_orderbtn8():
        if LUquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty8.set(0)
        elif LUquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            LUqty8.set(0)
        elif int(LUquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            LUqty8.set(0)
        elif int(LUquantity8.get()) > 0 and int(LUquantity8.get()) <= 50:
            lunch_8_total = int(LUquantity8.get()) * 125.00
            current_val.set(lunch_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Veggie Wrap with\nHummus'+','+'125.00'+','+f'{LUquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = lunch_8_total
            order_prices.append(food_price)

            LUqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            LUqty8.set(0)

    # ==========DINNER-CALCULATIONS========== #
    def dinner_orderbtn1():
        if DIquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty1.set(0)
        elif DIquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty1.set(0)
        elif int(DIquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty1.set(0)
        elif int(DIquantity1.get()) > 0 and int(DIquantity1.get()) <= 50:
            dinner_1_total = int(DIquantity1.get()) * 360.00
            current_val.set(dinner_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Grilled Chicken with\nRoasted Sweet Potatoes'+','+'360.00'+','+f'{DIquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_1_total
            order_prices.append(food_price)

            DIqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty1.set(0)

    def dinner_orderbtn2():
        if DIquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty2.set(0)
        elif DIquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty2.set(0)
        elif int(DIquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty2.set(0)
        elif int(DIquantity2.get()) > 0 and int(DIquantity2.get()) <= 50:
            dinner_2_total = int(DIquantity2.get()) * 167.00
            current_val.set(dinner_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Spaghetti with Marinara\nSauce'+','+'167.00'+','+f'{DIquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_2_total
            order_prices.append(food_price)

            DIqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty2.set(0)

    def dinner_orderbtn3():
        if DIquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty3.set(0)
        elif DIquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty3.set(0)
        elif int(DIquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty3.set(0)
        elif int(DIquantity3.get()) > 0 and int(DIquantity3.get()) <= 50:
            dinner_3_total = int(DIquantity3.get()) * 138.00
            current_val.set(dinner_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Baked Salmon with\nQuinoa Pilaf'+','+'138.00'+','+f'{DIquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_3_total
            order_prices.append(food_price)

            DIqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty3.set(0)

    def dinner_orderbtn4():
        if DIquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty4.set(0)
        elif DIquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty4.set(0)
        elif int(DIquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty4.set(0)
        elif int(DIquantity4.get()) > 0 and int(DIquantity4.get()) <= 50:
            dinner_4_total = int(DIquantity4.get()) * 322.00
            current_val.set(dinner_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Stir-Fried Tofu\nand Vegetables'+','+'322.00'+','+f'{DIquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_4_total
            order_prices.append(food_price)

            DIqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty4.set(0)

    def dinner_orderbtn5():
        if DIquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty5.set(0)
        elif DIquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty5.set(0)
        elif int(DIquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty5.set(0)
        elif int(DIquantity5.get()) > 0 and int(DIquantity5.get()) <= 50:
            dinner_5_total = int(DIquantity5.get()) * 449.00
            current_val.set(dinner_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Shrimp and Vegetable\nKebabs'+','+'449.00'+','+f'{DIquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_5_total
            order_prices.append(food_price)

            DIqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty5.set(0)

    def dinner_orderbtn6():
        if DIquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty6.set(0)
        elif DIquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty6.set(0)
        elif int(DIquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty6.set(0)
        elif int(DIquantity6.get()) > 0 and int(DIquantity6.get()) <= 50:
            dinner_6_total = int(DIquantity6.get()) * 389.00
            current_val.set(dinner_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Stuffed Bell Peppers'+','+'389.00'+','+f'{DIquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_6_total
            order_prices.append(food_price)

            DIqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty6.set(0)

    def dinner_orderbtn7():
        if DIquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty7.set(0)
        elif DIquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty7.set(0)
        elif int(DIquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty7.set(0)
        elif int(DIquantity7.get()) > 0 and int(DIquantity7.get()) <= 50:
            dinner_7_total = int(DIquantity7.get()) * 325.00
            current_val.set(dinner_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Eggplant Parmesan'+','+'325.00'+','+f'{DIquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_7_total
            order_prices.append(food_price)

            DIqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty7.set(0)

    def dinner_orderbtn8():
        if DIquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty8.set(0)
        elif DIquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DIqty8.set(0)
        elif int(DIquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DIqty8.set(0)
        elif int(DIquantity8.get()) > 0 and int(DIquantity8.get()) <= 50:
            dinner_8_total = int(DIquantity8.get()) * 299.00
            current_val.set(dinner_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Mexican-Style Chicken\nFajitas'+','+'299.00'+','+f'{DIquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = dinner_8_total
            order_prices.append(food_price)

            DIqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DIqty8.set(0)

    # ==========DRINKS-CALCULATIONS========== #
    def drink_orderbtn1():
        if DRquantity1.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty1.set(0)
        elif DRquantity1.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty1.set(0)
        elif int(DRquantity1.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty1.set(0)
        elif int(DRquantity1.get()) > 0 and int(DRquantity1.get()) <= 50:
            drink_1_total = int(DRquantity1.get()) * 37.00
            current_val.set(drink_1_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Coca-Cola'+','+'37.00'+','+f'{DRquantity1.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_1_total
            order_prices.append(food_price)

            DRqty1.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty1.set(0)

    def drink_orderbtn2():
        if DRquantity2.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty2.set(0)
        elif DRquantity2.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty2.set(0)
        elif int(DRquantity2.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty2.set(0)
        elif int(DRquantity2.get()) > 0 and int(DRquantity2.get()) <= 50:
            drink_2_total = int(DRquantity2.get()) * 37.00
            current_val.set(drink_2_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Pineapple Juice'+','+'37.00'+','+f'{DRquantity2.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_2_total
            order_prices.append(food_price)

            DRqty2.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty2.set(0)

    def drink_orderbtn3():
        if DRquantity3.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty3.set(0)
        elif DRquantity3.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty3.set(0)
        elif int(DRquantity3.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty3.set(0)
        elif int(DRquantity3.get()) > 0 and int(DRquantity3.get()) <= 50:
            drink_3_total = int(DRquantity3.get()) * 45.00
            current_val.set(drink_3_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Mango Lassi'+','+'45.00'+','+f'{DRquantity3.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_3_total
            order_prices.append(food_price)

            DRqty3.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty3.set(0)

    def drink_orderbtn4():
        if DRquantity4.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty4.set(0)
        elif DRquantity4.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty4.set(0)
        elif int(DRquantity4.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty4.set(0)
        elif int(DRquantity4.get()) > 0 and int(DRquantity4.get()) <= 50:
            drink_4_total = int(DRquantity4.get()) * 59.00
            current_val.set(drink_4_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Fruit Punch'+','+'59.00'+','+f'{DRquantity4.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_4_total
            order_prices.append(food_price)

            DRqty4.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty4.set(0)

    def drink_orderbtn5():
        if DRquantity5.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty5.set(0)
        elif DRquantity5.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty5.set(0)
        elif int(DRquantity5.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty5.set(0)
        elif int(DRquantity5.get()) > 0 and int(DRquantity5.get()) <= 50:
            drink_5_total = int(DRquantity5.get()) * 44.00
            current_val.set(drink_5_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Sparkling Lemonade'+','+'44.00'+','+f'{DRquantity5.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_5_total
            order_prices.append(food_price)

            DRqty5.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty5.set(0)

    def drink_orderbtn6():
        if DRquantity6.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty6.set(0)
        elif DRquantity6.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty6.set(0)
        elif int(DRquantity6.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty6.set(0)
        elif int(DRquantity6.get()) > 0 and int(DRquantity6.get()) <= 50:
            drink_6_total = int(DRquantity6.get()) * 66.00
            current_val.set(drink_6_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Pomegranate Spritzer'+','+'66.00'+','+f'{DRquantity6.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_6_total
            order_prices.append(food_price)

            DRqty6.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty6.set(0)

    def drink_orderbtn7():
        if DRquantity7.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty7.set(0)
        elif DRquantity7.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty7.set(0)
        elif int(DRquantity7.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty7.set(0)
        elif int(DRquantity7.get()) > 0 and int(DRquantity7.get()) <= 50:
            drink_7_total = int(DRquantity7.get()) * 83.00
            current_val.set(drink_7_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Virgin Mojito'+','+'83.00'+','+f'{DRquantity7.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_7_total
            order_prices.append(food_price)

            DRqty7.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty7.set(0)

    def drink_orderbtn8():
        if DRquantity8.get() == '':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty8.set(0)
        elif DRquantity8.get() == '0':
            messagebox.showerror('KUB-KUB', 'Please input quantity.')
            DRqty8.set(0)
        elif int(DRquantity8.get()) <= 0:
            messagebox.showerror('KUB-KUB', 'Invalid input.')
            DRqty8.set(0)
        elif int(DRquantity8.get()) > 0 and int(DRquantity8.get()) <= 50:
            drink_8_total = int(DRquantity8.get()) * 77.00
            current_val.set(drink_8_total)
            initial_total = current_val.get() + total_price.get()
            total_price.set(initial_total)

            food_details = 'Cucumber Cooler'+','+'77.00'+','+f'{DRquantity8.get()}'+'\n'
            show_orders.append(food_details)

            food_price = drink_8_total
            order_prices.append(food_price)

            DRqty8.set(0)
        else:
            messagebox.showwarning('KUB-KUB', 'Quantity limit is 50.')
            DRqty8.set(0)

    # ==========BREAKFAST========== #
    breakfastLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Breakfast')
    breakfastLbl.grid(row=0, column=0, columnspan=2, padx=(8, 0), pady=(8, 0))

    # THIS IS FIRST COLUMN IN BREAKFAST
    # ==========IMAGE========== #
    bf_1 = Image.open(r'Foods\Breakfast\bf-1.png')
    bf_2 = Image.open(r'Foods\Breakfast\bf-2.png')
    bf_3 = Image.open(r'Foods\Breakfast\bf-3.png')
    bf_4 = Image.open(r'Foods\Breakfast\bf-4.png')
    bf_1.thumbnail((100, 100))
    bf_2.thumbnail((100, 100))
    bf_3.thumbnail((100, 100))
    bf_4.thumbnail((100, 100))
    bf_1_photo = ImageTk.PhotoImage(bf_1)
    bf_2_photo = ImageTk.PhotoImage(bf_2)
    bf_3_photo = ImageTk.PhotoImage(bf_3)
    bf_4_photo = ImageTk.PhotoImage(bf_4)
    bf_1_Lbl = Label(secondcont_frame, image=bf_1_photo)
    bf_2_Lbl = Label(secondcont_frame, image=bf_2_photo)
    bf_3_Lbl = Label(secondcont_frame, image=bf_3_photo)
    bf_4_Lbl = Label(secondcont_frame, image=bf_4_photo)
    bf_1_Lbl.grid(row=1, column=1, columnspan=2, padx=40, pady=(8, 0))
    bf_2_Lbl.grid(row=1, column=3, columnspan=2, padx=40, pady=(8, 0))
    bf_3_Lbl.grid(row=1, column=5, columnspan=2, padx=40, pady=(8, 0))
    bf_4_Lbl.grid(row=1, column=7, columnspan=2, padx=40, pady=(8, 0))

    # ==========NAME========== #
    bf_1_name = Label(secondcont_frame, text='Oatmeal with Berries\nand Nuts', font=('Kristen ITC', 9))
    bf_2_name = Label(secondcont_frame, text='Avocado Toast', font=('Kristen ITC', 9))
    bf_3_name = Label(secondcont_frame, text='Greek Yogurt with\nGranola with Honey', font=('Kristen ITC', 9))
    bf_4_name = Label(secondcont_frame, text='Veggie Omelet', font=('Kristen ITC', 9))
    bf_1_name.grid(row=2, column=1, columnspan=2, padx=40, pady=(8, 0))
    bf_2_name.grid(row=2, column=3, columnspan=2, padx=40, pady=(8, 0))
    bf_3_name.grid(row=2, column=5, columnspan=2, padx=40, pady=(8, 0))
    bf_4_name.grid(row=2, column=7, columnspan=2, padx=40, pady=(8, 0))

    # ==========PRICE========== #
    bf_1_price = Label(secondcont_frame, text='₱185.00', font=('Arial', 11, 'bold'))
    bf_2_price = Label(secondcont_frame, text='₱35.00', font=('Arial', 11, 'bold'))
    bf_3_price = Label(secondcont_frame, text='₱120.00', font=('Arial', 11, 'bold'))
    bf_4_price = Label(secondcont_frame, text='₱99.00', font=('Arial', 11, 'bold'))
    bf_1_price.grid(row=3, column=1, columnspan=2, padx=40)
    bf_2_price.grid(row=3, column=3, columnspan=2, padx=40)
    bf_3_price.grid(row=3, column=5, columnspan=2, padx=40)
    bf_4_price.grid(row=3, column=7, columnspan=2, padx=40)

    # ==========ORDER-BUTTON========== #
    BForderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn1)
    BForderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn2)
    BForderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn3)
    BForderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn4)
    BForderBtn1.grid(row=4, column=1, columnspan=2)
    BForderBtn2.grid(row=4, column=3, columnspan=2)
    BForderBtn3.grid(row=4, column=5, columnspan=2)
    BForderBtn4.grid(row=4, column=7, columnspan=2)

    # ==========QUANTITY========== #
    BFqty1 = IntVar()
    BFqty2 = IntVar()
    BFqty3 = IntVar()
    BFqty4 = IntVar()
    BFquantity1 = Entry(secondcont_frame, textvariable=BFqty1, font='Arial', width=2)
    BFquantity2 = Entry(secondcont_frame, textvariable=BFqty2, font='Arial', width=2)
    BFquantity3 = Entry(secondcont_frame, textvariable=BFqty3, font='Arial', width=2)
    BFquantity4 = Entry(secondcont_frame, textvariable=BFqty4, font='Arial', width=2)
    BFquantity1.grid(row=4, column=1, columnspan=2, padx=(90, 0))
    BFquantity2.grid(row=4, column=3, columnspan=2, padx=(90, 0))
    BFquantity3.grid(row=4, column=5, columnspan=2, padx=(90, 0))
    BFquantity4.grid(row=4, column=7, columnspan=2, padx=(90, 0))
    BFqty1.set(0)
    BFqty2.set(0)
    BFqty3.set(0)
    BFqty4.set(0)

    # THIS IS SECOND COLUMN IN BREAKFAST
    # ==========IMAGE========== #
    bf_5 = Image.open(r'Foods\Breakfast\bf-5.png')
    bf_6 = Image.open(r'Foods\Breakfast\bf-6.png')
    bf_7 = Image.open(r'Foods\Breakfast\bf-7.png')
    bf_8 = Image.open(r'Foods\Breakfast\bf-8.png')
    bf_5.thumbnail((100, 100))
    bf_6.thumbnail((100, 100))
    bf_7.thumbnail((100, 100))
    bf_8.thumbnail((100, 100))
    bf_5_photo = ImageTk.PhotoImage(bf_5)
    bf_6_photo = ImageTk.PhotoImage(bf_6)
    bf_7_photo = ImageTk.PhotoImage(bf_7)
    bf_8_photo = ImageTk.PhotoImage(bf_8)
    bf_5_Lbl = Label(secondcont_frame, image=bf_5_photo)
    bf_6_Lbl = Label(secondcont_frame, image=bf_6_photo)
    bf_7_Lbl = Label(secondcont_frame, image=bf_7_photo)
    bf_8_Lbl = Label(secondcont_frame, image=bf_8_photo)
    bf_5_Lbl.grid(row=5, column=1, columnspan=2, pady=(8, 0))
    bf_6_Lbl.grid(row=5, column=3, columnspan=2, pady=(8, 0))
    bf_7_Lbl.grid(row=5, column=5, columnspan=2, pady=(8, 0))
    bf_8_Lbl.grid(row=5, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    bf_5_name = Label(secondcont_frame, text='Smoothie Bowl', font=('Kristen ITC', 9))
    bf_6_name = Label(secondcont_frame, text='Whole Grain Pancakes\nwith Maple Syrup', font=('Kristen ITC', 9))
    bf_7_name = Label(secondcont_frame, text='Breakfast Burrito', font=('Kristen ITC', 9))
    bf_8_name = Label(secondcont_frame, text='Quinoa Breakfast\nBowl', font=('Kristen ITC', 9))
    bf_5_name.grid(row=6, column=1, columnspan=2, pady=(8, 0))
    bf_6_name.grid(row=6, column=3, columnspan=2, pady=(8, 0))
    bf_7_name.grid(row=6, column=5, columnspan=2, pady=(8, 0))
    bf_8_name.grid(row=6, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    bf_5_price = Label(secondcont_frame, text='₱299.00', font=('Arial', 11, 'bold'))
    bf_6_price = Label(secondcont_frame, text='₱150.00', font=('Arial', 11, 'bold'))
    bf_7_price = Label(secondcont_frame, text='₱175.00', font=('Arial', 11, 'bold'))
    bf_8_price = Label(secondcont_frame, text='₱250.00', font=('Arial', 11, 'bold'))
    bf_5_price.grid(row=7, column=1, columnspan=2)
    bf_6_price.grid(row=7, column=3, columnspan=2)
    bf_7_price.grid(row=7, column=5, columnspan=2)
    bf_8_price.grid(row=7, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    BForderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn5)
    BForderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn6)
    BForderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn7)
    BForderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=bf_orderbtn8)
    BForderBtn5.grid(row=8, column=1, columnspan=2)
    BForderBtn6.grid(row=8, column=3, columnspan=2)
    BForderBtn7.grid(row=8, column=5, columnspan=2)
    BForderBtn8.grid(row=8, column=7, columnspan=2)

    # ==========QUANTITY========== #
    BFqty5 = IntVar()
    BFqty6 = IntVar()
    BFqty7 = IntVar()
    BFqty8 = IntVar()
    BFquantity5 = Entry(secondcont_frame, textvariable=BFqty5, font='Arial', width=2)
    BFquantity6 = Entry(secondcont_frame, textvariable=BFqty6, font='Arial', width=2)
    BFquantity7 = Entry(secondcont_frame, textvariable=BFqty7, font='Arial', width=2)
    BFquantity8 = Entry(secondcont_frame, textvariable=BFqty8, font='Arial', width=2)
    BFquantity5.grid(row=8, column=1, columnspan=2, padx=(90, 0))
    BFquantity6.grid(row=8, column=3, columnspan=2, padx=(90, 0))
    BFquantity7.grid(row=8, column=5, columnspan=2, padx=(90, 0))
    BFquantity8.grid(row=8, column=7, columnspan=2, padx=(90, 0))
    BFqty5.set(0)
    BFqty6.set(0)
    BFqty7.set(0)
    BFqty8.set(0)

    # ==========LUNCH========== #
    lunchLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Lunch')
    lunchLbl.grid(row=9, column=0, columnspan=2, padx=(8, 0), pady=(18, 0))

    # THIS IS FIRST COLUMN IN LUNCH
    # ==========IMAGE========== #
    lunch_1 = Image.open(r'Foods\Lunch\lunch-1.png')
    lunch_2 = Image.open(r'Foods\Lunch\lunch-2.png')
    lunch_3 = Image.open(r'Foods\Lunch\lunch-3.png')
    lunch_4 = Image.open(r'Foods\Lunch\lunch-4.png')
    lunch_1.thumbnail((100, 100))
    lunch_2.thumbnail((100, 100))
    lunch_3.thumbnail((100, 100))
    lunch_4.thumbnail((100, 100))
    lunch_1_photo = ImageTk.PhotoImage(lunch_1)
    lunch_2_photo = ImageTk.PhotoImage(lunch_2)
    lunch_3_photo = ImageTk.PhotoImage(lunch_3)
    lunch_4_photo = ImageTk.PhotoImage(lunch_4)
    lunch_1_Lbl = Label(secondcont_frame, image=lunch_1_photo)
    lunch_2_Lbl = Label(secondcont_frame, image=lunch_2_photo)
    lunch_3_Lbl = Label(secondcont_frame, image=lunch_3_photo)
    lunch_4_Lbl = Label(secondcont_frame, image=lunch_4_photo)
    lunch_1_Lbl.grid(row=10, column=1, columnspan=2, pady=(8, 0))
    lunch_2_Lbl.grid(row=10, column=3, columnspan=2, pady=(8, 0))
    lunch_3_Lbl.grid(row=10, column=5, columnspan=2, pady=(8, 0))
    lunch_4_Lbl.grid(row=10, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    lunch_1_name = Label(secondcont_frame, text='Grilled Chicken Salad', font=('Kristen ITC', 9))
    lunch_2_name = Label(secondcont_frame, text='Quinoa and Roasted\nVegetable Bowl', font=('Kristen ITC', 9))
    lunch_3_name = Label(secondcont_frame, text='Turkey and Avocado\nWrap', font=('Kristen ITC', 9))
    lunch_4_name = Label(secondcont_frame, text='Caprese Salad', font=('Kristen ITC', 9))
    lunch_1_name.grid(row=11, column=1, columnspan=2, pady=(8, 0))
    lunch_2_name.grid(row=11, column=3, columnspan=2, pady=(8, 0))
    lunch_3_name.grid(row=11, column=5, columnspan=2, pady=(8, 0))
    lunch_4_name.grid(row=11, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    lunch_1_price = Label(secondcont_frame, text='₱550.00', font=('Arial', 11, 'bold'))
    lunch_2_price = Label(secondcont_frame, text='₱385.00', font=('Arial', 11, 'bold'))
    lunch_3_price = Label(secondcont_frame, text='₱120.00', font=('Arial', 11, 'bold'))
    lunch_4_price = Label(secondcont_frame, text='₱75.00', font=('Arial', 11, 'bold'))
    lunch_1_price.grid(row=12, column=1, columnspan=2)
    lunch_2_price.grid(row=12, column=3, columnspan=2)
    lunch_3_price.grid(row=12, column=5, columnspan=2)
    lunch_4_price.grid(row=12, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    LUorderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn1)
    LUorderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn2)
    LUorderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn3)
    LUorderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn4)
    LUorderBtn1.grid(row=13, column=1, columnspan=2)
    LUorderBtn2.grid(row=13, column=3, columnspan=2)
    LUorderBtn3.grid(row=13, column=5, columnspan=2)
    LUorderBtn4.grid(row=13, column=7, columnspan=2)

    # ==========QUANTITY========== #
    LUqty1 = IntVar()
    LUqty2 = IntVar()
    LUqty3 = IntVar()
    LUqty4 = IntVar()
    LUquantity1 = Entry(secondcont_frame, textvariable=LUqty1, font='Arial', width=2)
    LUquantity2 = Entry(secondcont_frame, textvariable=LUqty2, font='Arial', width=2)
    LUquantity3 = Entry(secondcont_frame, textvariable=LUqty3, font='Arial', width=2)
    LUquantity4 = Entry(secondcont_frame, textvariable=LUqty4, font='Arial', width=2)
    LUquantity1.grid(row=13, column=1, columnspan=2, padx=(90, 0))
    LUquantity2.grid(row=13, column=3, columnspan=2, padx=(90, 0))
    LUquantity3.grid(row=13, column=5, columnspan=2, padx=(90, 0))
    LUquantity4.grid(row=13, column=7, columnspan=2, padx=(90, 0))
    LUqty1.set(0)
    LUqty2.set(0)
    LUqty3.set(0)
    LUqty4.set(0)

    # THIS IS SECOND COLUMN IN LUNCH
    # ==========IMAGE========== #
    lunch_5 = Image.open(r'Foods\Lunch\lunch-5.png')
    lunch_6 = Image.open(r'Foods\Lunch\lunch-6.png')
    lunch_7 = Image.open(r'Foods\Lunch\lunch-7.png')
    lunch_8 = Image.open(r'Foods\Lunch\lunch-8.png')
    lunch_5.thumbnail((100, 100))
    lunch_6.thumbnail((100, 100))
    lunch_7.thumbnail((100, 100))
    lunch_8.thumbnail((100, 100))
    lunch_5_photo = ImageTk.PhotoImage(lunch_5)
    lunch_6_photo = ImageTk.PhotoImage(lunch_6)
    lunch_7_photo = ImageTk.PhotoImage(lunch_7)
    lunch_8_photo = ImageTk.PhotoImage(lunch_8)
    lunch_5_Lbl = Label(secondcont_frame, image=lunch_5_photo)
    lunch_6_Lbl = Label(secondcont_frame, image=lunch_6_photo)
    lunch_7_Lbl = Label(secondcont_frame, image=lunch_7_photo)
    lunch_8_Lbl = Label(secondcont_frame, image=lunch_8_photo)
    lunch_5_Lbl.grid(row=14, column=1, columnspan=2, pady=(8, 0))
    lunch_6_Lbl.grid(row=14, column=3, columnspan=2, pady=(8, 0))
    lunch_7_Lbl.grid(row=14, column=5, columnspan=2, pady=(8, 0))
    lunch_8_Lbl.grid(row=14, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    lunch_5_name = Label(secondcont_frame, text='Lentil Soup', font=('Kristen ITC', 9))
    lunch_6_name = Label(secondcont_frame, text='Grilled Salmon with\nSteamed Vegetables', font=('Kristen ITC', 9))
    lunch_7_name = Label(secondcont_frame, text='Quinoa Salad with\nChickpeas and Feta\nCheese',
                         font=('Kristen ITC', 9))
    lunch_8_name = Label(secondcont_frame, text='Veggie Wrap with\nHummus', font=('Kristen ITC', 9))
    lunch_5_name.grid(row=15, column=1, columnspan=2, pady=(8, 0))
    lunch_6_name.grid(row=15, column=3, columnspan=2, pady=(8, 0))
    lunch_7_name.grid(row=15, column=5, columnspan=2, pady=(8, 0))
    lunch_8_name.grid(row=15, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    lunch_5_price = Label(secondcont_frame, text='₱110.00', font=('Arial', 11, 'bold'))
    lunch_6_price = Label(secondcont_frame, text='₱145.00', font=('Arial', 11, 'bold'))
    lunch_7_price = Label(secondcont_frame, text='₱600.00', font=('Arial', 11, 'bold'))
    lunch_8_price = Label(secondcont_frame, text='₱125.00', font=('Arial', 11, 'bold'))
    lunch_5_price.grid(row=16, column=1, columnspan=2)
    lunch_6_price.grid(row=16, column=3, columnspan=2)
    lunch_7_price.grid(row=16, column=5, columnspan=2)
    lunch_8_price.grid(row=16, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    LUorderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn5)
    LUorderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn6)
    LUorderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn7)
    LUorderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=lunch_orderbtn8)
    LUorderBtn5.grid(row=17, column=1, columnspan=2)
    LUorderBtn6.grid(row=17, column=3, columnspan=2)
    LUorderBtn7.grid(row=17, column=5, columnspan=2)
    LUorderBtn8.grid(row=17, column=7, columnspan=2)

    # ==========QUANTITY========== #
    LUqty5 = IntVar()
    LUqty6 = IntVar()
    LUqty7 = IntVar()
    LUqty8 = IntVar()
    LUquantity5 = Entry(secondcont_frame, textvariable=LUqty5, font='Arial', width=2)
    LUquantity6 = Entry(secondcont_frame, textvariable=LUqty6, font='Arial', width=2)
    LUquantity7 = Entry(secondcont_frame, textvariable=LUqty7, font='Arial', width=2)
    LUquantity8 = Entry(secondcont_frame, textvariable=LUqty8, font='Arial', width=2)
    LUquantity5.grid(row=17, column=1, columnspan=2, padx=(90, 0))
    LUquantity6.grid(row=17, column=3, columnspan=2, padx=(90, 0))
    LUquantity7.grid(row=17, column=5, columnspan=2, padx=(90, 0))
    LUquantity8.grid(row=17, column=7, columnspan=2, padx=(90, 0))
    LUqty5.set(0)
    LUqty6.set(0)
    LUqty7.set(0)
    LUqty8.set(0)

    # ==========DINNER==========#
    dinnerLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Dinner')
    dinnerLbl.grid(row=18, column=0, columnspan=2, padx=(8, 0), pady=(18, 0))

    # THIS IS FIRST COLUMN IN DINNER
    # ==========IMAGE========== #
    dinner_1 = Image.open(r'Foods\Dinner\dinner-1.png')
    dinner_2 = Image.open(r'Foods\Dinner\dinner-2.png')
    dinner_3 = Image.open(r'Foods\Dinner\dinner-3.png')
    dinner_4 = Image.open(r'Foods\Dinner\dinner-4.png')
    dinner_1.thumbnail((100, 100))
    dinner_2.thumbnail((100, 100))
    dinner_3.thumbnail((100, 100))
    dinner_4.thumbnail((100, 100))
    dinner_1_photo = ImageTk.PhotoImage(dinner_1)
    dinner_2_photo = ImageTk.PhotoImage(dinner_2)
    dinner_3_photo = ImageTk.PhotoImage(dinner_3)
    dinner_4_photo = ImageTk.PhotoImage(dinner_4)
    dinner_1_Lbl = Label(secondcont_frame, image=dinner_1_photo)
    dinner_2_Lbl = Label(secondcont_frame, image=dinner_2_photo)
    dinner_3_Lbl = Label(secondcont_frame, image=dinner_3_photo)
    dinner_4_Lbl = Label(secondcont_frame, image=dinner_4_photo)
    dinner_1_Lbl.grid(row=19, column=1, columnspan=2, pady=(8, 0))
    dinner_2_Lbl.grid(row=19, column=3, columnspan=2, pady=(8, 0))
    dinner_3_Lbl.grid(row=19, column=5, columnspan=2, pady=(8, 0))
    dinner_4_Lbl.grid(row=19, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    dinner_1_name = Label(secondcont_frame, text='Grilled Chicken with\nRoasted Sweet Potatoes',
                          font=('Kristen ITC', 9))
    dinner_2_name = Label(secondcont_frame, text='Spaghetti with\nMarinara Sauce', font=('Kristen ITC', 9))
    dinner_3_name = Label(secondcont_frame, text='Baked Salmon with\nQuinoa Pilaf', font=('Kristen ITC', 9))
    dinner_4_name = Label(secondcont_frame, text='Stir-Fried Tofu\nand Vegetables', font=('Kristen ITC', 9))
    dinner_1_name.grid(row=20, column=1, columnspan=2, pady=(8, 0))
    dinner_2_name.grid(row=20, column=3, columnspan=2, pady=(8, 0))
    dinner_3_name.grid(row=20, column=5, columnspan=2, pady=(8, 0))
    dinner_4_name.grid(row=20, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    dinner_1_price = Label(secondcont_frame, text='₱360.00', font=('Arial', 11, 'bold'))
    dinner_2_price = Label(secondcont_frame, text='₱167.00', font=('Arial', 11, 'bold'))
    dinner_3_price = Label(secondcont_frame, text='₱138.00', font=('Arial', 11, 'bold'))
    dinner_4_price = Label(secondcont_frame, text='₱322.00', font=('Arial', 11, 'bold'))
    dinner_1_price.grid(row=21, column=1, columnspan=2)
    dinner_2_price.grid(row=21, column=3, columnspan=2)
    dinner_3_price.grid(row=21, column=5, columnspan=2)
    dinner_4_price.grid(row=21, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DIorderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn1)
    DIorderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn2)
    DIorderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn3)
    DIorderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn4)
    DIorderBtn1.grid(row=22, column=1, columnspan=2)
    DIorderBtn2.grid(row=22, column=3, columnspan=2)
    DIorderBtn3.grid(row=22, column=5, columnspan=2)
    DIorderBtn4.grid(row=22, column=7, columnspan=2)

    # ==========QUANTITY========== #
    DIqty1 = IntVar()
    DIqty2 = IntVar()
    DIqty3 = IntVar()
    DIqty4 = IntVar()
    DIquantity1 = Entry(secondcont_frame, textvariable=DIqty1, font='Arial', width=2)
    DIquantity2 = Entry(secondcont_frame, textvariable=DIqty2, font='Arial', width=2)
    DIquantity3 = Entry(secondcont_frame, textvariable=DIqty3, font='Arial', width=2)
    DIquantity4 = Entry(secondcont_frame, textvariable=DIqty4, font='Arial', width=2)
    DIquantity1.grid(row=22, column=1, columnspan=2, padx=(90, 0))
    DIquantity2.grid(row=22, column=3, columnspan=2, padx=(90, 0))
    DIquantity3.grid(row=22, column=5, columnspan=2, padx=(90, 0))
    DIquantity4.grid(row=22, column=7, columnspan=2, padx=(90, 0))
    DIqty1.set(0)
    DIqty2.set(0)
    DIqty3.set(0)
    DIqty4.set(0)

    # THIS IS SECOND COLUMN IN DINNER
    # ==========IMAGE========== #
    dinner_5 = Image.open(r'Foods\Dinner\dinner-5.png')
    dinner_6 = Image.open(r'Foods\Dinner\dinner-6.png')
    dinner_7 = Image.open(r'Foods\Dinner\dinner-7.png')
    dinner_8 = Image.open(r'Foods\Dinner\dinner-8.png')
    dinner_5.thumbnail((100, 100))
    dinner_6.thumbnail((100, 100))
    dinner_7.thumbnail((100, 100))
    dinner_8.thumbnail((100, 100))
    dinner_5_photo = ImageTk.PhotoImage(dinner_5)
    dinner_6_photo = ImageTk.PhotoImage(dinner_6)
    dinner_7_photo = ImageTk.PhotoImage(dinner_7)
    dinner_8_photo = ImageTk.PhotoImage(dinner_8)
    dinner_5_Lbl = Label(secondcont_frame, image=dinner_5_photo)
    dinner_6_Lbl = Label(secondcont_frame, image=dinner_6_photo)
    dinner_7_Lbl = Label(secondcont_frame, image=dinner_7_photo)
    dinner_8_Lbl = Label(secondcont_frame, image=dinner_8_photo)
    dinner_5_Lbl.grid(row=23, column=1, columnspan=2, pady=(8, 0))
    dinner_6_Lbl.grid(row=23, column=3, columnspan=2, pady=(8, 0))
    dinner_7_Lbl.grid(row=23, column=5, columnspan=2, pady=(8, 0))
    dinner_8_Lbl.grid(row=23, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    dinner_5_name = Label(secondcont_frame, text='Shrimp and Vegetable\nKebabs', font=('Kristen ITC', 9))
    dinner_6_name = Label(secondcont_frame, text='Stuffed Bell Peppers', font=('Kristen ITC', 9))
    dinner_7_name = Label(secondcont_frame, text='Eggplant Parmesan', font=('Kristen ITC', 9))
    dinner_8_name = Label(secondcont_frame, text='Mexican-Style\nChicken Fajitas', font=('Kristen ITC', 9))
    dinner_5_name.grid(row=24, column=1, columnspan=2, pady=(8, 0))
    dinner_6_name.grid(row=24, column=3, columnspan=2, pady=(8, 0))
    dinner_7_name.grid(row=24, column=5, columnspan=2, pady=(8, 0))
    dinner_8_name.grid(row=24, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    dinner_5_price = Label(secondcont_frame, text='₱449.00', font=('Arial', 11, 'bold'))
    dinner_6_price = Label(secondcont_frame, text='₱389.00', font=('Arial', 11, 'bold'))
    dinner_7_price = Label(secondcont_frame, text='₱325.00', font=('Arial', 11, 'bold'))
    dinner_8_price = Label(secondcont_frame, text='₱299.00', font=('Arial', 11, 'bold'))
    dinner_5_price.grid(row=25, column=1, columnspan=2)
    dinner_6_price.grid(row=25, column=3, columnspan=2)
    dinner_7_price.grid(row=25, column=5, columnspan=2)
    dinner_8_price.grid(row=25, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DIorderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn5)
    DIorderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn6)
    DIorderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn7)
    DIorderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1',
                         command=dinner_orderbtn8)
    DIorderBtn5.grid(row=26, column=1, columnspan=2)
    DIorderBtn6.grid(row=26, column=3, columnspan=2)
    DIorderBtn7.grid(row=26, column=5, columnspan=2)
    DIorderBtn8.grid(row=26, column=7, columnspan=2)

    # ==========QUANTITY========== #
    DIqty5 = IntVar()
    DIqty6 = IntVar()
    DIqty7 = IntVar()
    DIqty8 = IntVar()
    DIquantity5 = Entry(secondcont_frame, textvariable=DIqty5, font='Arial', width=2)
    DIquantity6 = Entry(secondcont_frame, textvariable=DIqty6, font='Arial', width=2)
    DIquantity7 = Entry(secondcont_frame, textvariable=DIqty7, font='Arial', width=2)
    DIquantity8 = Entry(secondcont_frame, textvariable=DIqty8, font='Arial', width=2)
    DIquantity5.grid(row=26, column=1, columnspan=2, padx=(90, 0))
    DIquantity6.grid(row=26, column=3, columnspan=2, padx=(90, 0))
    DIquantity7.grid(row=26, column=5, columnspan=2, padx=(90, 0))
    DIquantity8.grid(row=26, column=7, columnspan=2, padx=(90, 0))
    DIqty5.set(0)
    DIqty6.set(0)
    DIqty7.set(0)
    DIqty8.set(0)

    # ==========DRINKS========== #
    drinkLbl = Label(secondcont_frame, font=('Kristen ITC', 12, 'bold'), text='Drinks')
    drinkLbl.grid(row=27, column=0, columnspan=2, padx=(8, 0), pady=(18, 0))

    # THIS IS FIRST COLUMN IN DRINKS
    # ==========IMAGE========== #
    drink_1 = Image.open(r'Foods\Drinks\drink-1.png')
    drink_2 = Image.open(r'Foods\Drinks\drink-2.png')
    drink_3 = Image.open(r'Foods\Drinks\drink-3.png')
    drink_4 = Image.open(r'Foods\Drinks\drink-4.png')
    drink_1.thumbnail((100, 100))
    drink_2.thumbnail((100, 100))
    drink_3.thumbnail((100, 100))
    drink_4.thumbnail((100, 100))
    drink_1_photo = ImageTk.PhotoImage(drink_1)
    drink_2_photo = ImageTk.PhotoImage(drink_2)
    drink_3_photo = ImageTk.PhotoImage(drink_3)
    drink_4_photo = ImageTk.PhotoImage(drink_4)
    drink_1_Lbl = Label(secondcont_frame, image=drink_1_photo)
    drink_2_Lbl = Label(secondcont_frame, image=drink_2_photo)
    drink_3_Lbl = Label(secondcont_frame, image=drink_3_photo)
    drink_4_Lbl = Label(secondcont_frame, image=drink_4_photo)
    drink_1_Lbl.grid(row=28, column=1, columnspan=2, pady=(8, 0))
    drink_2_Lbl.grid(row=28, column=3, columnspan=2, pady=(8, 0))
    drink_3_Lbl.grid(row=28, column=5, columnspan=2, pady=(8, 0))
    drink_4_Lbl.grid(row=28, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    drink_1_name = Label(secondcont_frame, text='Coca-Cola', font=('Kristen ITC', 9))
    drink_2_name = Label(secondcont_frame, text='Pineapple Juice', font=('Kristen ITC', 9))
    drink_3_name = Label(secondcont_frame, text='Mango Lassi', font=('Kristen ITC', 9))
    drink_4_name = Label(secondcont_frame, text='Fruit Punch', font=('Kristen ITC', 9))
    drink_1_name.grid(row=29, column=1, columnspan=2, pady=(8, 0))
    drink_2_name.grid(row=29, column=3, columnspan=2, pady=(8, 0))
    drink_3_name.grid(row=29, column=5, columnspan=2, pady=(8, 0))
    drink_4_name.grid(row=29, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    drink_1_price = Label(secondcont_frame, text='₱37.00', font=('Arial', 11, 'bold'))
    drink_2_price = Label(secondcont_frame, text='₱37.00', font=('Arial', 11, 'bold'))
    drink_3_price = Label(secondcont_frame, text='₱45.00', font=('Arial', 11, 'bold'))
    drink_4_price = Label(secondcont_frame, text='₱59.00', font=('Arial', 11, 'bold'))
    drink_1_price.grid(row=30, column=1, columnspan=2)
    drink_2_price.grid(row=30, column=3, columnspan=2)
    drink_3_price.grid(row=30, column=5, columnspan=2)
    drink_4_price.grid(row=30, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DRorderBtn1 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn1)
    DRorderBtn2 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn2)
    DRorderBtn3 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn3)
    DRorderBtn4 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn4)
    DRorderBtn1.grid(row=31, column=1, columnspan=2)
    DRorderBtn2.grid(row=31, column=3, columnspan=2)
    DRorderBtn3.grid(row=31, column=5, columnspan=2)
    DRorderBtn4.grid(row=31, column=7, columnspan=2)

    # ==========QUANTITY========== #
    DRqty1 = IntVar()
    DRqty2 = IntVar()
    DRqty3 = IntVar()
    DRqty4 = IntVar()
    DRquantity1 = Entry(secondcont_frame, textvariable=DRqty1, font='Arial', width=2)
    DRquantity2 = Entry(secondcont_frame, textvariable=DRqty2, font='Arial', width=2)
    DRquantity3 = Entry(secondcont_frame, textvariable=DRqty3, font='Arial', width=2)
    DRquantity4 = Entry(secondcont_frame, textvariable=DRqty4, font='Arial', width=2)
    DRquantity1.grid(row=31, column=1, columnspan=2, padx=(90, 0))
    DRquantity2.grid(row=31, column=3, columnspan=2, padx=(90, 0))
    DRquantity3.grid(row=31, column=5, columnspan=2, padx=(90, 0))
    DRquantity4.grid(row=31, column=7, columnspan=2, padx=(90, 0))
    DRqty1.set(0)
    DRqty2.set(0)
    DRqty3.set(0)
    DRqty4.set(0)

    # THIS IS SECOND COLUMN IN DRINKS
    # ==========IMAGE========== #
    drink_5 = Image.open(r'Foods\Drinks\drink-5.png')
    drink_6 = Image.open(r'Foods\Drinks\drink-6.png')
    drink_7 = Image.open(r'Foods\Drinks\drink-7.png')
    drink_8 = Image.open(r'Foods\Drinks\drink-8.png')
    drink_5.thumbnail((100, 100))
    drink_6.thumbnail((100, 100))
    drink_7.thumbnail((100, 100))
    drink_8.thumbnail((100, 100))
    drink_5_photo = ImageTk.PhotoImage(drink_5)
    drink_6_photo = ImageTk.PhotoImage(drink_6)
    drink_7_photo = ImageTk.PhotoImage(drink_7)
    drink_8_photo = ImageTk.PhotoImage(drink_8)
    drink_5_Lbl = Label(secondcont_frame, image=drink_5_photo)
    drink_6_Lbl = Label(secondcont_frame, image=drink_6_photo)
    drink_7_Lbl = Label(secondcont_frame, image=drink_7_photo)
    drink_8_Lbl = Label(secondcont_frame, image=drink_8_photo)
    drink_5_Lbl.grid(row=32, column=1, columnspan=2, pady=(8, 0))
    drink_6_Lbl.grid(row=32, column=3, columnspan=2, pady=(8, 0))
    drink_7_Lbl.grid(row=32, column=5, columnspan=2, pady=(8, 0))
    drink_8_Lbl.grid(row=32, column=7, columnspan=2, pady=(8, 0))

    # ==========NAME========== #
    dinner_5_name = Label(secondcont_frame, text='Sparkling Lemonade', font=('Kristen ITC', 9))
    dinner_6_name = Label(secondcont_frame, text='Pomegranate Spritzer', font=('Kristen ITC', 9))
    dinner_7_name = Label(secondcont_frame, text='Virgin Mojito', font=('Kristen ITC', 9))
    dinner_8_name = Label(secondcont_frame, text='Cucumber Cooler', font=('Kristen ITC', 9))
    dinner_5_name.grid(row=33, column=1, columnspan=2, pady=(8, 0))
    dinner_6_name.grid(row=33, column=3, columnspan=2, pady=(8, 0))
    dinner_7_name.grid(row=33, column=5, columnspan=2, pady=(8, 0))
    dinner_8_name.grid(row=33, column=7, columnspan=2, pady=(8, 0))

    # ==========PRICE========== #
    drink_5_price = Label(secondcont_frame, text='₱44.00', font=('Arial', 11, 'bold'))
    drink_6_price = Label(secondcont_frame, text='₱66.00', font=('Arial', 11, 'bold'))
    drink_7_price = Label(secondcont_frame, text='₱83.00', font=('Arial', 11, 'bold'))
    drink_8_price = Label(secondcont_frame, text='₱77.00', font=('Arial', 11, 'bold'))
    drink_5_price.grid(row=34, column=1, columnspan=2)
    drink_6_price.grid(row=34, column=3, columnspan=2)
    drink_7_price.grid(row=34, column=5, columnspan=2)
    drink_8_price.grid(row=34, column=7, columnspan=2)

    # ==========ORDER-BUTTON========== #
    DRorderBtn5 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn5)
    DRorderBtn6 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn6)
    DRorderBtn7 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn7)
    DRorderBtn8 = Button(secondcont_frame, text='Order', font=('Kristen ITC', 9), bg='#4b91f1', command=drink_orderbtn8)
    DRorderBtn5.grid(row=35, column=1, columnspan=2, pady=(0, 15))
    DRorderBtn6.grid(row=35, column=3, columnspan=2, pady=(0, 15))
    DRorderBtn7.grid(row=35, column=5, columnspan=2, pady=(0, 15))
    DRorderBtn8.grid(row=35, column=7, columnspan=2, pady=(0, 15))

    # ==========QUANTITY========== #
    DRqty5 = IntVar()
    DRqty6 = IntVar()
    DRqty7 = IntVar()
    DRqty8 = IntVar()
    DRquantity5 = Entry(secondcont_frame, textvariable=DRqty5, font='Arial', width=2)
    DRquantity6 = Entry(secondcont_frame, textvariable=DRqty6, font='Arial', width=2)
    DRquantity7 = Entry(secondcont_frame, textvariable=DRqty7, font='Arial', width=2)
    DRquantity8 = Entry(secondcont_frame, textvariable=DRqty8, font='Arial', width=2)
    DRquantity5.grid(row=35, column=1, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRquantity6.grid(row=35, column=3, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRquantity7.grid(row=35, column=5, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRquantity8.grid(row=35, column=7, columnspan=2, padx=(90, 0), pady=(0, 15))
    DRqty5.set(0)
    DRqty6.set(0)
    DRqty7.set(0)
    DRqty8.set(0)

    # ==============================PICKUP-WINDOW-FOOTER============================== #
    # ==========SHOW-ORDERS-WINDOW========== #
    def show_or():
        show_win = Toplevel()
        show_win.title('KUB-KUB')
        width = 600
        height = 500
        x_pos = (show_win.winfo_screenwidth() - width) // 2
        y_pos = (show_win.winfo_screenwidth() - height) // 5
        show_winGeometry = f'{width}x{height}+{x_pos}+{y_pos}'
        show_win.geometry(show_winGeometry)
        show_win.resizable(False, False)
        show_win.iconbitmap('Kub-Kub-Icon.ico')

        # ==========SHOW-ORDER-WINDOW-NAVBAR========== #
        shownav_frame = Frame(show_win)
        shownav_frame.pack(side=TOP, fill=X)
        current_orFrame = Frame(shownav_frame, width=600, height=80, bg='#4b91f1')
        current_orFrame.grid(row=0, column=0, columnspan=5)
        current_orLbl = Label(shownav_frame, text='Current Orders', font=('Kristen ITC', 16), bg='#4b91f1')
        current_orLbl.grid(row=0, column=2)

        # ==========SHOW-ORDERS-WINDOW-SCROLLBAR========== #
        cont_frame = Frame(show_win)
        cont_frame.pack(fill=BOTH, expand=1)
        cont_canvas = Canvas(cont_frame)
        cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
        cont_scrollbar.pack(side=RIGHT, fill=Y)
        cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
        cont_canvas.bind('<Configure>', lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
        secondcont_frame = Frame(cont_canvas)
        cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

        # ==========SHOW-LABELS========== #
        showOrdetails = Frame(secondcont_frame)
        showOrdetails.pack(side=TOP, fill=X)
        showOrFrame = Frame(showOrdetails, width=600)
        showOrFrame.grid(row=0, column=0, columnspan=8)
        foodLbl = Label(showOrdetails, text='Food', font=('Kristen ITC', 12, 'bold'))
        priceLbl = Label(showOrdetails, text='Price', font=('Kristen ITC', 12, 'bold'))
        quantityLbl = Label(showOrdetails, text='Quantity', font=('Kristen ITC', 12, 'bold'))
        foodLbl.grid(row=0, column=0, columnspan=2)
        priceLbl.grid(row=0, column=2, columnspan=2)
        quantityLbl.grid(row=0, column=4, columnspan=2)

        # ==========REMOVE-SPECIFIC-ORDER========== #
        def remove_or(index):
            show_orders.pop(index)
            minus_totalprice = total_price.get() - order_prices[index]
            total_price.set(minus_totalprice)
            order_prices.pop(index)
            dis_or()
            show_win.destroy()
            show_or()

        # ==========SHOW-ORDERS========== #
        def dis_or():
            count = 1
            for index, i in enumerate(show_orders):
                showOr = i.split(',')

                foodDis = Label(showOrdetails, text=showOr[0], font=('Kristen ITC', 12))
                priceDis = Label(showOrdetails, text=showOr[1], font=('Kristen ITC', 12))
                quantDis = Label(showOrdetails, text=showOr[2].strip(), font=('Kristen ITC', 12))
                removeBtn = Button(showOrdetails, text='Remove', font=('Kristen ITC', 10), bg='#4b91f1', command=lambda index=index: remove_or(index))
                foodDis.grid(row=count, column=0, columnspan=2)
                priceDis.grid(row=count, column=2, columnspan=2)
                quantDis.grid(row=count, column=4, columnspan=2)
                removeBtn.grid(row=count, column=6, columnspan=2)

                count += 1

        dis_or()

        # ==========SHOW-ORDERS-WINDOW-FOOTER========== #
        footer_frame = Frame(show_win)
        footer_frame.pack(side=BOTTOM, fill=X)
        footer = Frame(footer_frame, width=600, height=80, bg='#4b91f1')
        footer.grid(row=0, column=0, columnspan=6)
        show_total = Label(footer_frame, text=f'Total: ₱{total_price.get()}', font=('Kristen ITC', 16), bg='#4b91f1')
        show_total.grid(row=0, column=2, columnspan=2)

    # ==========PLACE-ORDER========== #
    def place_order():
        if show_orders == []:
            messagebox.showerror('KUB-KUB', 'You have no order.')
        else:
            placeOr_win = Toplevel()
            placeOr_win.title('KUB-KUB')
            placeOr_win.config(bg='#4b91f1')
            placeOr_width = 600
            placeOr_height = 500
            x_pos = (placeOr_win.winfo_screenwidth() - placeOr_width) // 2
            y_pos = (placeOr_win.winfo_screenwidth() - placeOr_height) // 6
            placeOr_winGeometry = f'{placeOr_width}x{placeOr_height}+{x_pos}+{y_pos}'
            placeOr_win.geometry(placeOr_winGeometry)
            placeOr_win.resizable(False, False)
            placeOr_win.iconbitmap('Kub-Kub-Icon.ico')

            # ==========SUBMIT-ORDER========== #
            def submit_order():
                if cusName.get() == '':
                    messagebox.showerror('KUB-KUB', 'Fill the missing information.')
                elif cusCont.get() == '':
                    messagebox.showerror('KUB-KUB', 'Fill the missing information.')
                else:
                    placeOr_win.withdraw()
                    confOr_win = Toplevel()
                    confOr_win.title('KUB-KUB')
                    confOr_width = 600
                    confOr_height = 500
                    x_pos = (confOr_win.winfo_screenwidth() - confOr_width) // 2
                    y_pos = (confOr_win.winfo_screenwidth() - confOr_height) // 6
                    confOr_winGeometry = f'{confOr_width}x{confOr_height}+{x_pos}+{y_pos}'
                    confOr_win.geometry(confOr_winGeometry)
                    confOr_win.resizable(False, False)
                    confOr_win.iconbitmap('Kub-Kub-Icon.ico')

                    # ==========TOP-FRAME========== #
                    TconfOr_frame1 = Frame(confOr_win)
                    TconfOr_frame1.pack(side=TOP, fill=X)
                    TconfOr_frame2 = Frame(TconfOr_frame1, width=600, height=80, bg='#4b91f1')
                    TconfOr_frame2.grid(row=0, column=0, columnspan=6)
                    confirmLbl = Label(TconfOr_frame1, text='Confirmation', font=('Kristen ITC', 16, 'bold'),
                                       bg='#4b91f1')
                    confirmLbl.grid(row=0, column=2, columnspan=2)

                    # ==========SUBMIT-ORDER-WINDOW-SCROLLBAR========== #
                    cont_frame = Frame(confOr_win)
                    cont_frame.pack(fill=BOTH, expand=1)
                    cont_canvas = Canvas(cont_frame)
                    cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
                    cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
                    cont_scrollbar.pack(side=RIGHT, fill=Y)
                    cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
                    cont_canvas.bind('<Configure>',
                                     lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
                    secondcont_frame = Frame(cont_canvas)
                    cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

                    # ==========CENTER-FRAME========== #
                    CconfOr_frame1 = Frame(secondcont_frame)
                    CconfOr_frame1.grid(row=0, column=0, columnspan=10)

                    foodLbl = Label(CconfOr_frame1, text='Food', font=('Kristen ITC', 12, 'bold'))
                    priceLbl = Label(CconfOr_frame1, text='Price', font=('Kristen ITC', 12, 'bold'))
                    quantityLbl = Label(CconfOr_frame1, text='Quantity', font=('Kristen ITC', 12, 'bold'))
                    foodLbl.grid(row=0, column=1, columnspan=2, padx=70)
                    priceLbl.grid(row=0, column=3, columnspan=2, padx=70)
                    quantityLbl.grid(row=0, column=5, columnspan=2, padx=70)

                    count = 1
                    for i in show_orders:
                        showOr = i.split(',')

                        foodDis = Label(CconfOr_frame1, text=showOr[0], font=('Kristen ITC', 12))
                        priceDis = Label(CconfOr_frame1, text=showOr[1], font=('Kristen ITC', 12))
                        quantDis = Label(CconfOr_frame1, text=showOr[2].strip(), font=('Kristen ITC', 12))
                        foodDis.grid(row=count, column=1, columnspan=2)
                        priceDis.grid(row=count, column=3, columnspan=2)
                        quantDis.grid(row=count, column=5, columnspan=2)

                        count += 1

                    # ==========BOTTOM-FRAME========== #
                    # ==========CONFIRM-ORDER========== #
                    def confirm_order():
                        personal_infos = 'PICK-UP'+', '+cusName.get()+', '+cusCont.get()+', '+str(total_price.get())+'\n'
                        file_infos = open('personal infos.txt', 'a')
                        file_infos.write(personal_infos)
                        file_infos.close()
                        file_orders = open('orders.txt', 'a')
                        orders = str(show_orders) + '\n'
                        file_orders.write(str(orders))
                        file_orders.close()
                        show_orders.clear()
                        order_prices.clear()
                        total_price.set(0.00)
                        confOr_win.destroy()
                        messagebox.showinfo('KUB-KUB', 'Your order is now processing for pick-up. Thank you for ordering!')

                    BconfOr_frame1 = Frame(confOr_win)
                    BconfOr_frame1.pack(side=BOTTOM, fill=X)
                    BconfOr_frame2 = Frame(BconfOr_frame1, width=600, height=80, bg='#4b91f1')
                    BconfOr_frame2.grid(row=0, column=0, columnspan=6)
                    confirmBtn = Button(BconfOr_frame1, text='Confirm Order', font=('Kristen ITC', 12, 'bold'), command=confirm_order)
                    confirmtotal = Label(BconfOr_frame1, text=f'Total: ₱{total_price.get()}', font=('Kristen ITC', 14, 'bold'), bg='#4b91f1')
                    confirmBtn.grid(row=0, column=1, columnspan=2)
                    confirmtotal.grid(row=0, column=3, columnspan=2)

            placeOr_frame = Frame(placeOr_win, width=600, height=500, bg='#4b91f1')
            placeOr_frame.pack(fill=Y)

            cusName = StringVar()
            cusCont = StringVar()
            NameEnt = Entry(placeOr_frame, width=40, textvariable=cusName, justify='center', font=('Kristen ITC', 12))
            NameLbl = Label(placeOr_frame, text='Name', font=('Kristen ITC', 12), bg='#4b91f1')
            ContEnt = Entry(placeOr_frame, width=40, textvariable=cusCont, justify='center', font=('Kristen ITC', 12))
            ContLbl = Label(placeOr_frame, text='Contact Number', font=('Kristen ITC', 12), bg='#4b91f1')
            submitBtn = Button(placeOr_frame, text='Submit', font=('Kristen ITC', 12, 'bold'), command=submit_order)
            NameEnt.grid(row=0, column=3, columnspan=3, pady=(140, 0))
            NameLbl.grid(row=1, column=4)
            ContEnt.grid(row=2, column=3, columnspan=3, pady=(40, 0))
            ContLbl.grid(row=3, column=4)
            submitBtn.grid(row=4, column=4, pady=(40, 0))

    total_price = DoubleVar()
    current_val = DoubleVar()
    footer_frame = Frame(pick_win)
    footer_frame.pack(side=BOTTOM, fill=X)
    footer = Frame(footer_frame, width=800, height=80, bg='#4b91f1')
    footer.grid(row=0, column=0, columnspan=6)
    place_orderBtn = Button(footer_frame, text='Place Order', font=('Kristen ITC', 10, 'bold'), command=place_order)
    place_orderBtn.grid(row=0, column=0, columnspan=2, padx=(8, 0), sticky='w')
    showBtn = Button(footer_frame, text='Show', font=('Kristen ITC', 10, 'bold'), command=show_or)
    showBtn.grid(row=0, column=4, padx=(250, 0))
    totalLbl = Label(footer_frame, text='Total: ₱', font=('Kristen ITC', 16), bg='#4b91f1')
    totalLbl.grid(row=0, column=4, padx=(420, 0))
    total_price.set(0.00)
    totalpriceEnt = Entry(footer_frame, textvariable=total_price, state='readonly', font=('Kristen ITC', 16), readonlybackground='#4b91f1', width=10)
    totalpriceEnt.grid(row=0, column=5, padx=(0, 50))

    # ==============================TERMINATE-PROGRAM============================== #
    def terminate_program():
        main.destroy()
    pick_win.protocol('WM_DELETE_WINDOW', terminate_program)

    pick_win.mainloop()

# ==============================MAIN-WINDOW-NAVBAR============================== #
navbar = Frame(main, width=800, height=80, bg='#4b91f1')
navbar.grid(row=0, column=0, columnspan=5)
logo_img = Image.open('Kub-Kub Logo.jpg')
logo_img.thumbnail((100, 70))
logo_photo = ImageTk.PhotoImage(logo_img)
logo = Label(main, image=logo_photo)
logo.grid(row=0, column=0, padx=(8, 0), columnspan=2, sticky='w')

# ==============================MAIN-WINDOW-CONTENT============================== #
slogan = Label(main, font=('Kristen ITC', 16), text='''KUB-KUB: Your Tastebuds' Personal Courier''')
slogan.grid(row=1, column=0, columnspan=5,pady=(120, 50))
deliveryBtn = Button(main, width=10, height=3, text='Delivery', font=('Kristen ITC', 12, 'bold'), bg='#4b91f1', command=delivery_window)
deliveryBtn.grid(row=2, column=1, padx=(50, 0))
pickupBtn = Button(main, width=10, height=3, text='Pick-up', font=('Kristen ITC', 12, 'bold'), bg='#4b91f1', command=pickup_window)
pickupBtn.grid(row=2, column=3, padx=(0, 50))
orLbl = Label(main, font=('Kristen ITC', 12, 'bold'), text='OR')
orLbl.grid(row=2, column=2)

main.mainloop()