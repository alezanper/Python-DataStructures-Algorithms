class person (object):
        
    def __init__(self, name, age, email_address, phone_number):
        self.name = name
        self.age = age 
        self.email_address = email_address
        self.phone_number = phone_number
    
    def isAdult(self):
        if (self.age > 18):
            return True
        else:
            return False

class foreignPerson (person):
        
    def __init__(self, name, age, email_address, phon_number, country):
        person.__init__(self, name, age, email_address, phon_number)
        self.country = country
    
    def isAdult(self):
        if (self.age > 18):
            return True
        else:
            return False

class client(object):

    def __init__(self, person, creditScore):
        if (person.isAdult()):
            self.creditPerson = person
            self.creditScore =  creditScore
        else:
            print('Client must be an adult')
      
    def describeClient(self):
        print(self.creditPerson.name + ' is our client')
        print('Phone Number: ' + self.creditPerson.phone_number)
        print('Email Address: ' + self.creditPerson.email_address)
        if (self.isGoodScore()):
            print(self.creditPerson.name + ' has a good score')
        else: 
            print(self.creditPerson.name + ' has not a good score')

    def isGoodScore(self):
        if self.creditScore > 100:
            return True
        else:
            return False    
        
my_person = person('Alexander', 32, 'email@email.com', '31122334455')
print(my_person.name)
print(my_person.age)
print(my_person.email_address)

foreign_person = foreignPerson('Juana', 26, 'myemail@otheremail.com', '98980864647', 'Spain')

print(foreign_person.name)
print(foreign_person.email_address)
print(foreign_person.isAdult())

my_client = client(my_person, 200)
my_client.describeClient()
my_client2 = client(foreign_person, 50)
my_client2.describeClient()