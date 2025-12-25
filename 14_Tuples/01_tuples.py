# A Tuple in Python is an ordered, immutable (unchangeable) collection of elements.

# Ordered → items have a fixed position.

# Immutable → you can’t change or modify items once created. defined -> ()

# 1️⃣ Creating a Tuple
my_tuple = (10, 20, 30, 40)
print("Tuple:", my_tuple)

# Using Tuple Concatenation
t = (1, 2, 3)
t = t + (4,)   # Note the comma after 4 → makes it a tuple
print(t)


# 2️⃣ Tuples can contain different data types
mixed_tuple = (1, "Hello", 3.5, True)
print("Mixed Tuple:", mixed_tuple)

# 3️⃣ Accessing Tuple Elements (using index)
print("First element:", my_tuple[0])      # 10
print("Last element:", my_tuple[-1])      # 40

# 4️⃣ Slicing a Tuple
print("Slice [1:3]:", my_tuple[1:3])      # (20, 30)

# 5️⃣ Tuples are immutable (this will cause an error)
# my_tuple[0] = 100   ❌ Not allowed

# 6️⃣ Length of Tuple
print("Length:", len(my_tuple))            # 4

# 7️⃣ Tuple with one element must have a comma
single_element = (5,)
print("Single element tuple:", single_element)

# 8️⃣ Tuple Packing and Unpacking
person = ("Alice", 25, "Engineer")         # Packing
name, age, profession = person             # Unpacking
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# 9️⃣ Loop through a Tuple
for item in my_tuple:
    print("Item:", item)

# 🔟 Nested Tuple
nested_tuple = ((1, 2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)
print("Second inner tuple element:", nested_tuple[1][1])  # 5

# 1️⃣1️⃣ Tuple Concatenation
t1 = (1, 2, 3)
t2 = (4, 5)
combined = t1 + t2
print("Concatenated Tuple:", combined)

# 1️⃣2️⃣ Tuple Repetition
repeated = t1 * 2
print("Repeated Tuple:", repeated)

# 1️⃣3️⃣ Using 'in' keyword
print(2 in t1)      # True
print(10 in t1)     # False

# 1️⃣4️⃣ Tuple Functions
nums = (3, 1, 4, 2)
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

