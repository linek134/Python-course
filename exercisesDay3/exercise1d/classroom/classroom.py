class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getfirstname(self):
        return self.firstname
    def getlastname(self):
        return self.lastname
    def getfullname(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject
    def subject(self):
        return self.subject
    def printNameSubject(self):
        print(f"{self.firstname} {self.lastname}, {self.subject}")

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def subject(self):
        return self.course
    def printNameCourse(self):
        print(f"{self.firstname} {self.lastname} teaches on the {self.course}")

