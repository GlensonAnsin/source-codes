class Employee:
    def __init__(self, employee_id, employee_fname, employee_lname, employee_position, employee_rate_per_hour):
        self.employee_id = employee_id
        self.employee_fname = employee_fname
        self.employee_lname = employee_lname
        self.employee_position = employee_position
        self.employee_rate_per_hour = employee_rate_per_hour

    def show(self):
        return print("EMPLOYEE INFORMATION:\nEmployee ID: {}\nName: {} {}\nPosition: {}".format(self.employee_id, self.employee_fname, self.employee_lname, self.employee_position))

    def calculate_salary(self, days_present):
        self.days_present = days_present
        return print("Salary: PHP", self.employee_rate_per_hour * (days_present * 8))

Glenson = Employee(2022300315, "Glenson", "Ansin", "Software Engineer", 168)