for i in range (0,9):

    import random
    import math
    random_num = int(random.random()*41)+60
    # print random_num
    if random_num >= 60 and random_num <= 69:
        print "Score: " + str(random_num) + "; Your grade is D"
    elif random_num <= 79:
        print "Score: " + str(random_num) + "; Your grade is C"
    elif random_num <= 89:
        print "Score: " + str(random_num) + "; Your grade is B"
    else:
        print "Score: " + str(random_num) + "; Your grade is A"

# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this:
#
# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!
# Copy
# Hint: Use the python random module to generate a random number
#
# import random
# random_num = random.random()
# # the random function will return a floating point number, that is 0.0 <= random_num < 1.0
# #or use...
# random_num = random.randint()
