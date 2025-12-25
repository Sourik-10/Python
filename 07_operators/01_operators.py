
# --------------------------
# 1️⃣ Arithmetic Operators
# --------------------------
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation
print()

# --------------------------
# 2️⃣ Comparison Operators
# --------------------------
x = 5
y = 8
print("Comparison Operators:")
print("x == y:", x == y)   # Equal to
print("x != y:", x != y)   # Not equal to
print("x > y:", x > y)     # Greater than
print("x < y:", x < y)     # Less than
print("x >= 5:", x >= 5)   # Greater than or equal
print("y <= 10:", y <= 10) # Less than or equal
print()

# --------------------------
# 3️⃣ Logical Operators
# --------------------------
a = 5
b = 10
print("Logical Operators:")
print("(a > 2 and b > 5):", a > 2 and b > 5)   # AND
print("(a > 8 or b == 10):", a > 8 or b == 10) # OR
print("not(a > 8):", not(a > 8))               # NOT
print()

# --------------------------
# 4️⃣ Assignment Operators
# --------------------------
x = 5
print("Assignment Operators:")
x += 2    # x = x + 2
print("x += 2 →", x)
x *= 3    # x = x * 3
print("x *= 3 →", x)
x //= 4   # x = x // 4
print("x //= 4 →", x)
x **= 2   # x = x ** 2
print("x **= 2 →", x)
print()

# --------------------------
# 5️⃣ Bitwise Operators
# --------------------------
a = 5   # 0101
b = 3   # 0011
print("Bitwise Operators:")
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 1 =", a << 1) # Left Shift
print("a >> 1 =", a >> 1) # Right Shift
print()

# --------------------------
# 6️⃣ Membership Operators
# --------------------------
nums = [1, 2, 3, 4]
print("Membership Operators:")
print("3 in nums:", 3 in nums)         # True
print("5 not in nums:", 5 not in nums) # True
print()

# --------------------------
# 7️⃣ Identity Operators
# --------------------------
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("Identity Operators:")
print("x is y:", x is y)         # True
print("x is z:", x is z)         # False
print("x is not z:", x is not z) # True
print()

print("✅ All operator demonstrations completed successfully!")
