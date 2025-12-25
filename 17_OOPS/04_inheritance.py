# Inheritance is an OOP concept that allows one class (called the child or derived class) to inherit the properties and methods of another class (called the parent or base class).

class Animal:  # Parent class (superclass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Child class (inherits from Animal)
    def speak(self): 
        super().speak()     # Call parent method
        print("Bhou!")      # Dog's specific behavior

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name)  # Output: Rover
print(my_cat.name)  # Output: Fluffy

# They both have a 'speak' method, but it behaves differently:
my_dog.speak()  # Output: bhou!
my_cat.speak()  # Output: Meow!