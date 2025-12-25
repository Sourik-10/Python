import re  # Import the regular expressions module

# Sample text on which regex operations will be performed
text = "The quick brown fox jumps over the lazy dog & fox."

# ------------------ re.search() ------------------
# Searches for the first occurrence of the pattern in the text
# Returns a match object if found, otherwise returns None

# match = re.search(r"fox", text)
# print(match)

# if match:
#     print("Match found:", match.group())     # Returns the matched substring
#     print("Start index:", match.start())     # Starting index of the match
#     print("End index:", match.end())         # Ending index of the match


# ------------------ re.findall() ------------------
# Finds all occurrences of the pattern and returns them as a list
# re.IGNORECASE makes the search case-insensitive

matches = re.findall("the", text, re.IGNORECASE)
print("Matches:", matches)


# ------------------ re.sub() ------------------
# Replaces all occurrences of the pattern with the given replacement string

new_text = re.sub("fox", "cat", text)
print("New text:", new_text)
# ------------------ re.split() ------------------
# Splits the text at each occurrence of the pattern and returns a list
parts = re.split("&", text)
print("Parts:", parts)