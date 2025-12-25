# 🧠 Sets in Python - Full Example

# 1️⃣ Creating a Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# 2️⃣ Sets automatically remove duplicates
dup_set = {1, 2, 2, 3, 3, 4}
print("Duplicate removed:", dup_set)  # Output: {1, 2, 3, 4}

# 3️⃣ Creating an Empty Set
empty_set = set()   # Use set(), NOT {} because {} creates a dictionary
print("Empty set:", empty_set)

# 4️⃣ Adding Elements
my_set.add(6)
print("After adding 6:", my_set)

# 5️⃣ Adding Multiple Elements
my_set.update([7, 8, 9])
print("After adding multiple elements:", my_set)

# 6️⃣ Removing Elements
my_set.remove(4)     # ❌ Error if element not found
print("After remove(4):", my_set)

my_set.discard(10)   # ✅ No error if element not found
print("After discard(10):", my_set)

# 7️⃣ Popping a Random Element
popped = my_set.pop()
print("Popped element:", popped)
print("After pop:", my_set)

# 8️⃣ Set Operations (Union, Intersection, Difference, Symmetric Difference)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union (A ∪ B)
print("Union:", A | B)

# Intersection (A ∩ B)
print("Intersection:", A & B)

# Difference (A - B)
print("Difference (A - B):", A - B)

# Symmetric Difference (A △ B)
print("Symmetric Difference:", A ^ B)

# 9️⃣ Membership Test
print("Is 2 in A?", 2 in A)
print("Is 10 not in A?", 10 not in A)

# 🔟 Clearing a Set
A.clear()
print("After clearing A:", A)

# 1️⃣1️⃣ Set from a List (removes duplicates automatically)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers from list:", unique_numbers)
