coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50
newlist = list(coordinates)
newlist[0] = 50
coordinates = tuple(newlist)
print(coordinates)