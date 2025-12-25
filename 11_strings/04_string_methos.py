#name ="sourik" # sreting are immutable

# name[0]='e' # this is wrong

# a =len(name)
# print(a)

# text = "hello world"
# print(text.upper())  # Output: "HELLO WORLD"
# print(text.lower())  # Output: "hello world"
# print(text.title())  # Output: "Hello World"
# print(text.capitalize())  # Output: "Hello world"

#Removing Whitespace
# text = "  hello world  "
# print(text.strip())  # Output: "hello world"
# print(text.lstrip()) # Output: "hello world  "
# print(text.rstrip()) # Output: "  hello world"


#Finding and Replacing
# text = "Gaming is fun"
# print(text.find("is"))   # inex of first occurence Output: 7
# print(text.replace("fun", "awesome"))  # Output: "Gaming is awesome"

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # list - Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"

#Checking String Properti
text1 = "code123"
print(text1.isalpha())  # Output: False
print(text1.isdigit())  # Output: False
print(text1.isalnum())  # Output: True
print(text1.isspace())  # Output: False