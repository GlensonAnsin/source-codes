class Customer:
    def __init__(self, customer_id, customer_fname, customer_lname, date_register, points=0):
        self.customer_id = customer_id
        self.customer_fname = customer_fname
        self.customer_lname = customer_lname
        self.date_register = date_register
        self.points = points

    def show(self):
        return print("CUSTOMER INFORMATION:\nCustomer ID: {}\nName: {} {}\nDate Registered: {}\nPoints: {}".format(self.customer_id, self.customer_fname, self.customer_lname, self.date_register, self.points))

Glenson = Customer("2022300315", "Glenson", "Ansin", "November 8, 2022")