# Below shows a basic for-loop in Python

alphabet = ["A", "B", "C", "D"]
# For every letter in array alphabet..
for letter in alphabet:
    print(letter)
    
    
# Printing out dictionary values..
my_dict = {}

# Can assign a key & a value like this..

my_dict[25] = "Square of 5"
my_dict[3.14] = "Pi"

for key in my_dict.keys():
    print(key)
    
for value in my_dict.values():
    print(value)
    
string = "Random string"
# Strings are comprised of characters - can use the len() function to get its length

# Print the len of a string, in string format..
print(str(len(string)))

print(string[6:])

# Can count how many times a substring appears in a string
string.count("Random")

# Can find what position a substring is found at..
string.index("Random")

# Change cases..
string.upper()

string.lower()

# Can split the string with a delimiter
string.split(' ')


# Can check whether a string starts with or ends with a particular letter
string.startswith("Random")

string.endswith("Random")

print(string[:-1])
# This gives everything but the last char

print(string[-3:])
# This gives the last 3

print(string[-3:-1])
