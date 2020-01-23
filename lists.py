# Create a list of names..
names = ["Jason", "Dean", "Michael"]

# Create a list of ages..
ages = [21, 40, 29]

# Say we want to add to a list at the start..
# Use the 'insert' function, specify the position, specify the value
names.insert(0, "Joseph")

names

# Add age to the end..
ages.append(22)

ages

# Putting the first element to the end of the list
# Create a temporary variable to store the popped value
temp = names.pop(0)
temp

names.append(temp)
names
