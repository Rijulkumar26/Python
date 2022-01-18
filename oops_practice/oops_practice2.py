class Dog:
    
    animal = 'Dog'
    
    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color
    
    def describe(self):
        print(self.name, 'is a', self.animal)
        print('animal: ',self.animal)
        print('breed: ',self.breed)
        print('color: ',self.color)
        print('\n')

Rodger = Dog('Rodger','Pug','grey')
Tommy = Dog('Tommy','labrador','brown')
Rodger.describe()
Tommy.describe()