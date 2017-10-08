x = [4, 6, 1, 3, 5, 7, 25]
def draw_Stars(x):
    # print x
    for i in x:
        print "*" * i
draw_Stars(x)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_Stars(x):
    # print x
    for i in x:
        if isinstance(i,int):
            print "*" * i
        elif isinstance(i,str):
            print i[0].lower() * len(i)
draw_Stars(x)

# Write the following functions.
#
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
#
# For example:
#
# x = [4, 6, 1, 3, 5, 7, 25]
# Copy
# draw_stars(x) should print the following when invoked:
#
# ****
# ******
# *
# ***
# *****
# *******
# *************************
# Copy
# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
#
# For example:
#
# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# Copy
# draw_stars(x) should print the following in the terminal:
#
# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj
