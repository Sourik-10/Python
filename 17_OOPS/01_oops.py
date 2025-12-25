#Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects — which combine data (attributes) and behavior (methods).It helps make code more modular, reusable, and easier to maintain.


# Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

# Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.


#  Class: Think of a class as a blueprint or a template. Eg. from for an exam that contains name ,age, fathers name etc.

# object is a specific instance created from the class .Eg. form which contains data for sohom.

class Employee:
  company="TCS"
  
  def get_salary(self): #self refers to the object of the class which is being created
    return 35000
  
e = Employee() #an object of class employee is created here
print(e.get_salary()) #Employee e get salary method is called 
print(e.company)
