import requests

# Send a GET request to an API
response = requests.get("https://api.github.com/users/sourik")

print(response.text)
with open("response.txt", "w") as file:
    file.write(response.text)
# # Print status code (200 means success)
# print(response.status_code)

# # Print response data in JSON format
# print(response.json())
