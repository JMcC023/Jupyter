someNum = 5
someString = "abc"
someList = ["Saturday", "Sun"]
someDictionary = {"Pi": 3.14}

def function_that_reassigns(someNum, someString, someList, someDictionary):
    # someNum = 10
    # someString = "xyz"
    # Strings & numbers are immutable, however there is slightly more flexibility in doing..
    someNum = someNum + 10
    someString = someString + "xyz"
    
    #someList = ["Monday", "Tuesday"]
    #someDictionary = {"Pi": 3.1415}
    
    someList.append("Monday")
    someDictionary["Pi"] = 3.1415
    return

print("Before: " , someNum, someString, someList, someDictionary)

function_that_reassigns(someNum, someString, someList, someDictionary)
print("After: " , someNum, someString, someList, someDictionary)
