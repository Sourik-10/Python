# A constructor is a special method in a class that automatically runs when you create an object.It’s mainly used to initialize (set up) the object’s attributes.

class Employee:
  
  def __init__(self, salary ,name ,bond): #init constructor
      self.salary = salary # create an instance atrribute of name salary and assign it with salary
      self.name= name
      self.bond = bond
  
  def get_salary(self):
    return self.salary
  
  def get_info(self):
    print(f"The Name Of The Employee is {self.name}. salary is {self.salary} & bond is for {self.bond} years")
  
e1 = Employee(40000 ,"sohom",2) 
e1.get_info()
 
 
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name      # Initialize instance variable
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating Objects (constructor called automatically)
s1 = Student("Suman", 18)
s2 = Student("Arjun", 20)

s1.show()
s2.show()
