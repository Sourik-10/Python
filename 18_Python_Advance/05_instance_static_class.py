class Employee:
    # Class variable shared by all instances of the class
    company = "Google"

    # Constructor method to initialize instance variables
    def __init__(self, name, salary):
        self.name = name        # Instance variable
        self.salary = salary    # Instance variable

    # Instance method to print employee information
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static method: does not depend on instance or class variables
    @staticmethod
    def sum(a, b):
        return a + b

    # class methods
    @classmethod
    def print_company(cls):
      print(cls.company)
      
    @classmethod
    def change_company(cls,new_company):
      cls.company = new_company

# Creating objects (instances) of the Employee class
e1 = Employee("Alice", 70000)
e2 = Employee("Bob", 80000)

# Accessing class variable using the class name
# print(Employee.company)

# Accessing instance variable using class name will throw an error
# print(Employee.name)  # This will raise an AttributeError

# Calling instance methods
e1.print_info()
e2.print_info()

# Calling static method using an object (can also be called using the class name)
print(e1.sum(4, 6))

e1.print_company()
e1.change_company("Acer")
e1.print_company()
