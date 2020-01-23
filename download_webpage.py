import urllib.request
import sys

# Assign a dummy value else the while loop won't even execute
url = 'http://www.google.com'

# Create a blank links dictionary in which KVPs will correspond to (name, url)
links = {}

while url != '':
    # Try blocks are used for risky code which is prone to failing - fundamental in error handling
    try:
        urlToRead = input("Please enter a URL ")
        if urlToRead == "":
            print("Stopped searching ")
            break
        name = input("Please enter an associate name for the URL: " + urlToRead + " ")
        # Below is where we're downloading the actual URL contents in HTML, & returns them in a var called webFile
        webFile = urllib.request.urlopen(urlToRead).read()
        links[name] = webFile
    # If the try-block fails, the exception commands are ran
    except:
        # Error handling at runtime
        print("*****************\nUnexepcted Error ", sys.exc_info()[0])
        # Above returns information about the exception that has occurred (thru sys library)
        print("Invalid URL")
        response = input("An error occurred.. press Y to continue, N to stop ")
        if response == "N":
            print("Quitting.. ")
            break
            # n.b. break breaks out of the innermost loop
        else:
            continue
            # Continues to the next iteration of the while-loop

print(links.keys())

