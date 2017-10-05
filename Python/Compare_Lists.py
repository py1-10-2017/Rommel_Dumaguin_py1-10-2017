def compareLists(x,y):
    print x, y
    notSame = False
    if len(x) != len(y):
        print "The lists are not the same."
    else:
        for num in range (len(list_one)):
            if list_one[num] == list_two[num]:
                continue
            else:
                print "The lists are not the same."
                notSame = True
                break
            if notSame == True:
                print "The lists are not the same."
        if notSame == False:
            print "The lists are the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareLists(list_one,list_two)
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compareLists(list_one,list_two)
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compareLists(list_one,list_two)
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compareLists(list_one,list_two)

# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
#
# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:
#
# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
# Copy
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
# Copy
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# Copy
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']
