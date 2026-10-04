from abc import ABC, abstractmethod

class Animal:
    def eat(self):
        print("eating")


class Dog(Animal):
    def speak(self):
        print("woof")
        
class Cat(Animal):
    def speak(self):
        print("meow")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2

if __name__ == "__main__":
    animals = [Dog(), Cat()]
    for a in animals:
        print(a.speak())
        print(a.eat())
    
    c = Circle(5)
    print(c.area())
        