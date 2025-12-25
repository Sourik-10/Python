def sum(a,b):
  print("the sum is")
  c =a + b
  global z # please modify globalz
  z= 10 # this will refer to global z & not create a local variable
  return c

z = 5 
print(sum(1,2))
print(z)
