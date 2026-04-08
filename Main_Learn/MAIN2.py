class Niggas:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"You name is {self.name} and you are {self.age} old"
    def Greet(self):
        print("your name is " + self.name)

P1 = Niggas("Steve", 30)
P2 = Niggas("Alex", 14)
P3 = Niggas("RDJ", 2)
P4 = Niggas("Jake", 90)

P1.Greet()
P2.Greet()
P3.Greet()
P4.Greet()
