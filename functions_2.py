num = 10

# Define a function

def mod(num):
    num = num * 10
    return num * 10
    
mod(num)

#########################################################################
# A function to take a circle's radius, & return the area
#########################################################################

# define

def calculate_area(radius):
    # A = Pi R^2
    area = 3.14 * radius * radius
    return area
    
# Call..

radius = 5
area = calculate_area(radius)
print("Radius: ", radius, " Area: ", area)

#########################################################################
# A function to take a circle's radius, & return the area 
# - by printing to the screen
#########################################################################

def screen_area(radius):
    print("Given a circle with radius ", radius, " Area: ", (3.14 * radius * radius) )

screen_area(15)

#########################################################################
# A function to take a list of circle's radii, & return the areas 
#########################################################################

def radii(rad_list):
    # define the empty list..
    results = []
    # construct a for-loop to append results
    for rad in rad_list:
        results.append(3.14 * rad * rad)
    return results
    
# Call the function to test
radius_list = [1,2,3,4]
area_list = radii(radius_list)

#########################################################################
# A function to take a list of circle radii, which returns 2 outputs
#    1: list of areas of those circles
#    2: list of circumference of those circles
# How do we do this? Use a dictionary!
#########################################################################

# define the function..
def calculate_ac(rad_list):
    area_list = []
    circ_list = []
    result_hash = {'Areas': area_list,
                    'Circumferences' : circ_list}
    for rad in rad_list:
        area_list.append(3.14 * rad * rad)
        circ_list.append(3.14 * rad * rad)
    
    return result_hash
    
result_map = calculate_ac(radius_list)
print("For circles with radii: ", radius_list, "\nAreas: ", result_map['Areas'], 
      "\nCircumferences: ", result_map['Circumferences'])
