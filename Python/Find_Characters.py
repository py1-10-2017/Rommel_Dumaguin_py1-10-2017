def findCharacters(list,char):
    newArr = []
    print list,char
    for item in list:
        # print item
        if item.find(char) != -1:
            newArr.append(item)
    print newArr
findCharacters(['hello','world','my','name','is','Anna'],'o')

# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
#
# Here's an example:
#
# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
# Copy
# Hint: how many loops will you need to complete this task?
