class Animal:                           #superclass
    def __init__(self,colour,legs):
        self.colour = colour
        self.legs = legs

class Cat(Animal):                      #subclass
    def purr(self):
        print("purrrrrrrrrrrrrr")
        return 0

felix = Cat("ginger", 4)

print(felix.colour)
print(felix.legs)
felix.purr()
print(felix.purr())
print("lsdhfjdkslhfsd")
#dslidksfjsdlkdsflkj