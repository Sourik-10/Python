# # List of numbers
# num = [2, 4, 8, 9, 5]

# # Function to return the square of a number
# def square(x):
#     return x * x

# # Using map() to apply the square function to each element in the list
# new = list(map(square, num))

# # Printing the new list containing squared values
# print(new)


num = [2, 4, 8, 9, 5]
# Using lambda function to calculate the square of each number
new = list(map(lambda x: x * x, num))
print(new)
