class Dog():
    ''' A dog class '''

    # Class attribute
    species = 'mammal'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)
        
