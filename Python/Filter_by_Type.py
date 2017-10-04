
# class x(object):
#     print object
def valueTypeOf(x):
    input_type = type(x)
    # print input_type
    # if input_type == str:
    if isinstance(x,int):
        if x >= 100:
            print "That's a big number!"
        elif x < 100:
            print "That's a small number"
    if isinstance(x,str):
        if len(x) >= 50:
            print "Long sentence."
        elif len(x) < 50:
            print "Short sentence."
    if isinstance(x,list):
        if len(x) >= 10:
            print "Big list!"
        elif len(x) < 10:
            print "Short list."
# x = 1
# valueTypeOf(x)
# x = "1"
# valueTypeOf(x)
# x = [1]
# valueTypeOf(x)
sI = 45
valueTypeOf(sI)
mI = 100
valueTypeOf(mI)
bI = 455
valueTypeOf(bI)
eI = 0
valueTypeOf(eI)
spI = -23
valueTypeOf(spI)
sS = "Rubber baby buggy bumpers"
valueTypeOf(sS)
mS = "Experience is simply the name we give our mistakes"
valueTypeOf(mS)
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
valueTypeOf(bS)
eS = ""
valueTypeOf(eS)
aL = [1,7,4,21]
valueTypeOf(aL)
mL = [3,5,7,34,3,2,113,65,8,89]
valueTypeOf(mL)
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
valueTypeOf(lL)
eL = []
valueTypeOf(eL)
spL = ['name','address','phone number','social security number']
valueTypeOf(spL)

# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#
# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
#
# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
#
# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
#
# Test your program using these examples:
#
# sI = 45
# mI = 100
# bI = 455
# eI = 0
# spI = -23
# sS = "Rubber baby buggy bumpers"
# mS = "Experience is simply the name we give our mistakes"
# bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# eS = ""
# aL = [1,7,4,21]
# mL = [3,5,7,34,3,2,113,65,8,89]
# lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# eL = []
# spL = ['name','address','phone number','social security number']
