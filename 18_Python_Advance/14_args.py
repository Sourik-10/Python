#args: Allows you to pass a variable number of positional arguments.

#1
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3, 4))

#2
def show_details(name, *scores):
    print("Name:", name)
    print("Scores:", scores)

show_details("Sayak", 80, 85, 90)

