# Example of Class and Class inheritance

# Base Class
# Class Person inherits from Object
class Person(object):
    def __init__(self, name):
        self.name = name # Initlize parmaeters
    
    # Method
    def reveal_identity(self):
        print("My name is {}".format(self.name))
        

# Inherits for Base Class
# Class SuperHero inherits from Class Person
class SuperHero(Person):
    def __init__(self, name, hero_name): 
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name # Initlize parmaeters
        
    def reveal_identity(self): # Override
        super(SuperHero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))
        

# Instances of Classes
doug = Person('Doug')
doug.reveal_identity()

#jessica = SuperHero('Jessica Wulf', 'The SheWolf')
#jessica.reveal_identity()
