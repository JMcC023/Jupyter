import sys

try: 
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# Can have multiple excepts
except IOError as e:
    print("I/O erorr ({0}): {1}".format(e.errno, estrerror))
except ValueError:
    print("Could not convert value to integer")
except:
    # This prints the description of the last error
    print("Unexpected error: " , sys.exc_info()[0])
    raise
# Raise is a way to throw an exception if the exception was of 2 types we knew how to handle
# We did this, but if it's a generic type we weren't expecting, we used raise to signal that we tried to
# handle the error, but failed

finally:
    print("Goodbye world")
# Finally is a keyword to state code that absolutely must be executed regardless of whether or not an exception was thrown
