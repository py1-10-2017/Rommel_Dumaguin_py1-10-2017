def odd_even():
    for num in range (1,2001):
        # print num
        if num % 2 == 0:
            print "Number is " + str(num) + ". This is an even number."
        else:
            print "Number is " + str(num) + ". This is an odd number."
odd_even()

def multiplyBy5(numList,x):
    newList = []
    for num in range (0,len(numList)):
        newList.append(numList[num]*x)
    return newList
b = multiplyBy5([2, 4, 10, 16],2)
print b

def hackerChallenge(x):
    newArr = []
    for i in x:
        tempArr = []
        for j in range(0,i):
            tempArr.append(1)
        newArr.append(tempArr)
    return newArr
c = hackerChallenge(multiplyBy5([2, 4, 10, 16],2))
print c
