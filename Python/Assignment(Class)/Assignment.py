class Student:
    def __init__(self, idno, fname, lname, age, gender, address, yr_level, course):
        self.idno = idno
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.address = address
        self.yr_level = yr_level
        self.course = course
    def introduce(self):
        return "I am {} {}. My ID number is {}, and I am a {} {} student.".format(self.fname, self.lname, self.idno, self.yr_level, self.course)
    def enroll(self, section):
        self.section = section
        return
    def add_major(self, major):
        self.major = major
        return "I am {} {}, and I am a {} {} major in {}.".format(self.fname, self.lname, self.yr_level, self.course, self.major)

Glenson = Student("2022300315", "Glenson", "Ansin", "19", "male", "Balongis, Balulang, Cagayan de Oro City", "1st year", "BS in Information Technology")
