#OOP

#Objects are defined as class
#Each obj has attributes & methods (i.e. attribute: color/name, method: fetch)

class Dog():

    # Attribute (color/about itself)
    def __init__(self, color: str = None):
        self.color = color

    # Method
    def fetch(self, toy:str = 'ball') -> str:
        return toy
    
Max = Dog('black')
print(Max.color)
Shortie = Dog('black and white')
returned_toy = Shortie.fetch('mouse')
print(Shortie.color)
print(returned_toy)



#####DATA METHODS
from dataclasses import dataclass
@dataclass
class squeakyToy:
    """Data class to hold the attributes for a given squeaky toy. 
        Yes, I love my dogs. 
    """

    def __init__(self, name:str, texture:str, size:float, quantity:int):
        self.name = name
        self.texture = texture
        self.size = size
        self.quantity = quantity


pumpkin = squeakyToy('Pumpkin', 'soft and fluffy', 6.32, 1)
steggo = squeakyToy(name='Steggo', texture='Canvas', size=11.2, quantity=2)

print(f'Steggo is the pups favorite, and we only have {steggo.quantity} left!')

steggo.quantity -= 1
print(f'Steggo is the pups favorite, and we only have {steggo.quantity} left!')