# Allows a class to inherit attributes and methods from another class

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Purr")


class Mouse(Animal):
    def speak(self):
        print("Squeak")


dog = Dog("Bosco")
cat = Cat("Luna")
mouse = Mouse("Panya")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
