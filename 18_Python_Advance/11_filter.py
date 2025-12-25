# # Function to check whether a number is greater than 10
# def is_greater_than_10(x):
#     if x > 10:
#         return True
#     else:
#         return False

# # List of numbers
# num = [1, 3, 56, 89, 6, 90, 6, 34, 12, 9]

# # Using filter() to keep only numbers greater than 10
# new = list(filter(is_greater_than_10, num))

# # Printing the filtered list
# print(new)


num = [1, 3, 56, 89, 6, 90, 6, 34, 12, 9]

# Using lambda function to filter numbers greater than 10
new = list(filter(lambda x: x > 10, num))
print(new)
