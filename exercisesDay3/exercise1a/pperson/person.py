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
