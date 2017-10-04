sumNum = 0
newStr = ""
passingList = ['magical unicorns',19,'hello',98.98,'world']
def valueTypeOf(x):
    hasNum = False
    hasStr = False
    print "Given:",passingList
    for item in passingList:
        # print item
        if isinstance(item,float):
            # print "num"
            global sumNum
            sumNum += item
            hasNum = True
        elif isinstance(item,int):
            # print "num"
            global sumNum
            sumNum += item
            hasNum = True
        elif isinstance(item,str):
            # print "str"
            global newStr
            newStr += " " + item
            hasStr = True
    print "sumNum =", sumNum
    print "newStr =", newStr
    if hasNum == True and hasStr == True:
        print "List data types are Mixed"
    elif hasNum == True:
        print "List data types are Numbers"
    elif hasStr == True:
        print "List data types are Strings"

valueTypeOf(['magical unicorns',19,'hello',98.98,'world'])

# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
#
# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
#
# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
# Copy
# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"
# Copy
# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"
