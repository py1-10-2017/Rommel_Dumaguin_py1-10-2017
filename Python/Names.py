print "Part I:"
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printStudents():
    for i in students:
        print i["first_name"], i["last_name"]
printStudents()

print " "

print "Part II:"
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printStudentsCharCount():
    for key in users:
        print key
        print users[key]
        group_of_users=users[key]
        for i in range(0, len(group_of_users)):
            # print i
            full_name = group_of_users[i]['first_name'] + group_of_users[i]['last_name']
            print "{} - {} {} - {}".format(i+1, group_of_users[i]['first_name'], group_of_users[i]['last_name'], len(full_name))
    # print "Students"
    # # countStudents = 0
    # for i in users["Students"]:
    #     # countStudents += 1
    #     print i+1, i["first_name"], i["last_name"], len(i["first_name"]) + len(i["last_name"])
    # print "Instructors"
    # # countInstructors = 0
    # for i in users["Instructors"]:
    #     # countInstructors += 1
    #     print i+1, i["first_name"], i["last_name"], len(i["first_name"]) + len(i["last_name"])
printStudentsCharCount()

# Write the following function.
#
# Part I
# Given the following list:
#
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# Copy
# Create a program that outputs:
#
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
# Copy
# Part II
# Now, given the following dictionary:
#
# users = {
#  'Students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }
# Copy
# Create a program that prints the following format (including number of characters in each combined name):
#
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13
# Copy
# Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.
