# Dictionaries are enclosed in braces, {}
# e.g.
my_dict = {}

# Can assign a key & a value like this..

my_dict[25] = "Square of 5"
my_dict[3.14] = "Pi"

# Print..
my_dict

type(my_dict)

# Printing out values..
print("The value corresponding to the key: " , str(3.14) , " is: " , my_dict[3.14])

# Can view keys..
my_dict.keys()

# Can view values..
my_dict.values()

len(my_dict.values())

# Taking input to remove from a dictionary

delete = input("What do you want to remove?")

if delete in my_dict:
    my_dict.pop(delete)
    print("Removed ", delete)

print(my_dict)
