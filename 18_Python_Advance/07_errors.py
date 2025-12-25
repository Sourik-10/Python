# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a + b}")
#         break
#     except ValueError as e:
#         print("Invalid input. Please enter valid integers.")
#         print("Error:", e)

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Invalid input! Please enter a number.")

# # Alternative using a tuple:
# try:
#   num = int(input("Enter a number: "))
#   result = 10 / num
# except (ZeroDivisionError, ValueError) as e:
#   print(f"An error occurred: {e}")

#raising exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted."

try:
  print(check_age(20))  # Access granted.
  print(check_age(16))  # Raises ValueError
except ValueError as e:
  print(f"Error: {e}")