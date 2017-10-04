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
