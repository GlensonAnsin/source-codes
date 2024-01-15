import Employee
import Customer
import Product

employee_list = []
customer_list = []
product_list = []

while True:
    print("=" * 50)
    print("Welcome to XYZ System, what would you like to do?")
    print("1. Add Employee\n2. View Employees\n3. Add Customer\n4. View Customers\n5. Add Product\n6. View Products\n7. Exit")
    print("=" * 50)
    choose_num = int(input("Input Here: "))
    print("=" * 50)
    print()

    if choose_num == 1:
        employee_id = int(input("Enter ID: "))
        employee_fname = input("Enter first name: ")
        employee_lname = input("Enter last name: ")
        employee_position = input("Enter position: ")
        employee_rate_per_hour = float(input("Enter rate per hour: "))
        Employee.Employee(employee_id, employee_fname, employee_lname, employee_position, employee_rate_per_hour)
        employee_infos = f"Employee ID: {employee_id}\nName: {employee_fname} {employee_lname}\nPosition: {employee_position}\nHourly Rate: PHP {employee_rate_per_hour}"
        employee_list.append(employee_infos)
        print()

    elif choose_num == 2:
        print(f"EMPLOYEE INFORMATION:\n")
        print(f"Total Employees: {len(employee_list)}\n")
        for i in employee_list:
            print(i)
            print()
        print()

    elif choose_num == 3:
        customer_id = int(input("Enter ID: "))
        customer_fname = input("Enter first name: ")
        customer_lname = input("Enter last name: ")
        date_register = input("Enter registration date: ")
        points = float(input("Enter points: "))
        Customer.Customer(customer_id, customer_fname, customer_lname, date_register, points)
        customer_infos = f"Customer ID: {customer_id}\nName: {customer_fname} {customer_lname}\nRegistration Date: {date_register}\nPoints: {points}"
        customer_list.append(customer_infos)
        print()

    elif choose_num == 4:
        print(f"CUSTOMER INFORMATION:\n")
        print(f"Total Customers: {len(customer_list)}\n")
        for i in customer_list:
            print(i)
            print()
        print()

    elif choose_num == 5:
        product_id = int(input("Enter ID: "))
        product_name = input("Enter product name: ")
        product_price = float(input("Enter price: "))
        Product.Product(product_id, product_name, product_price)
        product_infos = f"Product ID: {product_id}\nProduct Name: {product_name}\nPrice: PHP {product_price}"
        product_list.append(product_infos)
        print()

    elif choose_num == 6:
        print(f"PRODUCT INFORMATION:\n")
        print(f"Total Products: {len(product_list)}\n")
        for i in product_list:
            print(i)
            print()
        print()

    elif choose_num == 7:
        print("Thank You!")
        break

    else:
        print(f"Invalid input! Please try again.\n")