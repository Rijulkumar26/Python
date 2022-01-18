class Dog:
     
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


class Person:
    
    #init method or constructor
    def __init__(self, name):
        self.name = name
    
    #sample method
    def say_hi(self):
        print('Hello my name is',self.name)

#Driver code
Tommy = Dog()
#Accessing class attributes and method through objects
Tommy.fun()

H = Person('Harry')
H.say_hi()