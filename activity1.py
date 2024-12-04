#Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). 
# Create different objects for each class and pass the parameters.
#  Showcase the concept of polymorphism in this program.

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return "I am {} and my age is {} years ".format(self.name,self.age)
    
    def make_sound(self):
        return "I bark at the strangers"
    
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return "I am {} and my age is {} years ".format(self.name,self.age)
    
    def make_sound(self):
        return "I make sound meow when I am hungry"
    

d=Dog("Coco",2)
print(d.info())
print(d.make_sound())

c=Cat("Kitty",10)
print(c.info())
print(c.make_sound())
