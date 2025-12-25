a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

try:
    c = a / b
    print(c)

except Exception as e:
    print("Error:", e)
#this is always executed no matter what ..
finally:
    print("always executed")

    