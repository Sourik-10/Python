class Employee:
  company ="asus" # this is class attribute
  def __init__(self, salary ,name ,bond,company): #init constructor
      self.salary = salary # create an instance atrribute of name salary and assign it with salary
      self.name= name
      self.bond = bond
      self.company  = company
  
  def get_salary(self):
    return self.salary
  
  def get_info(self):
    print(f"The Name Of The Employee is {self.name}. salary is {self.salary} & bond is for {self.bond} years")
    
e1 = Employee(40000 ,"sohom",2,"hcl")    
print(e1.company)   # always print instance attribute if present
print(Employee.company) #This will always printn class attribute.

#object introspection
print(dir(e1))