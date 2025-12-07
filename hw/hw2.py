class Animal:
    def __init__(self, name: str, age: int, health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self) -> str:
        return f"{self.name}, {self.age} лет, здоровье {self.health}"
    def use_ability(self) -> str:
        return f"{self.name} использует базовую способность."
class Flyable:
    def use_ability(self):
        ability = super().use_ability()
        return f"{ability} летает."

class Swimmable:
    def use_ability(self):
        ability = super().use_ability()
        return f'{ability} плавает.'
class Invisible:
    def use_ability(self):
        ability = super().use_ability()
        return f'{ability} становится невидимым.'
class Duck(Flyable, Swimmable, Animal):
    pass

class Bat(Flyable, Invisible, Animal):
    pass
class Frog(Swimmable, Animal):
    pass
class Phoenix(Flyable, Invisible, Animal):
    def reborn(self):
        return 'имеет способность возрождаться'
class Zoo():
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        return self.animals
    def show_all(self):
        for i in self.animals:
            print(i.info())

    def perform_show(self):
        for j in self.animals:
            print(j.use_ability())


a = Duck('Donald', 2, 90)
b = Phoenix('Dimond', 100, 100)
c = Frog('Betty', 5, 60)
d = Bat('Kermit', 2, 50)
zoo = Zoo()
zoo.add_animal(a)
zoo.add_animal(b)
zoo.add_animal(c)
zoo.add_animal(d)
zoo.show_all()
zoo.perform_show()
print(Duck.__mro__)
print(Phoenix.__mro__)
print(Frog.__mro__)
print(Bat.__mro__)
