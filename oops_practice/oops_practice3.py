# Class for Dog
class Dog():
    
    # Class Variable
    animal = 'dog'
    
     # The init method or constructor
    def __init__(self,breed):
        # Instance Variable
        self.breed = breed
    
    # Adds an instance variable
    def setcolor(self,color):
        self.color=color
    
    # Retrieves instance variable
    def getcolor(self):
        return self.color

# Driver Code    
tommy = Dog('Pug')
tommy.setcolor('grey')
print(tommy.getcolor())