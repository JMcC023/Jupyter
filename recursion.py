# A function to reverse a string

def reverse_string(string):
    # Base Case 1: if there is no input, just return
    if string is None:
        return string
    
    # Base Case 2: if it is a string, but is 0 or 1, return
    if(len(string)) <= 1:
        return string
    
    # Recursive case
    return reverse_string(string[1:]) + string[0]
    # What happens here is we take the character at the beginning of the string, & attatch it to the end of the string
    
# Test
s = "Hello World"
print("The reverse of ", s, " is :", reverse_string(s))

# There is also a built in way to do this..
print("The reverse of ", s, " is :", s[::-1])
