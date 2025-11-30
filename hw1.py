class Dog:
    def __init__(self,name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def bark(self):
        return f'{self.name} says Woof! Woof!'
    def eat(self, food_weight):
        self.weight += food_weight
        return f'{self.name} ate {food_weight}kg. So now its weight is {self.weight}'
rex = Dog('Rex','gray',5)
max = Dog('Max', 'white', 7)
coco = Dog('Coco', 'black', 4)
print(rex.bark())
print(rex.eat(1))
print(max.bark())
print(max.eat(2))
print(coco.bark())
print(coco.eat(1.5))