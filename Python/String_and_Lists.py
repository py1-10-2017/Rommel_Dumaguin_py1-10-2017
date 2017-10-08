# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
getLoc = words.find("day")
print "day is at location", getLoc
newString = words.replace("day", "month")
print newString

#Min and Max
x = [2,54,-2,7,12,98]
print "min =",min(x)
print "max =",max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print "First =",x[0]
print "Last =",x[len(x)-1]

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print "x.sort() =", x
print len(x)
halfOfLength = len(x) / 2
print halfOfLength
secondHalfLength = len(x)-halfOfLength
print secondHalfLength
y = []
for count in range (0, halfOfLength+1):
    y.append(x.pop(halfOfLength))
print x
print y
y.insert(0,x)
print y

# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
#
# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
#
# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
#
# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
