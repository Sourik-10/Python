# match value:
#     case pattern1:
#          Code to execute if value matches pattern1
#     case pattern2:
#          Code to execute if value matches pattern2
#     case _:
#          Default case (if no patterns match)

a = int(input("Enter a lucky number:"))

match(a):
  case 1:
    print("you won charger")
  case 3:
      print("you won 100k")
  case 6:
      print("you won camera") 
  case _:
      print("Better luck next time")
          
        
      