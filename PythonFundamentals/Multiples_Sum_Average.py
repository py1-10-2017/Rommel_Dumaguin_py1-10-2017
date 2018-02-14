# Multiples
# Print all odd numbers from 1 to 1000
for odd in range (1,1000,2):
    print odd
# Print all multiples of 5 from 5 to 1,000,000
for multiplesOf5 in range (5,1000000+1,5):
    print multiplesOf5

# Sum List
# Print the sum of all list values: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print "sum =", sum(a)

# Average List
# Print average of the values in the list: a = [1, 2, 5, 10, 255, 3]
print "average =", sum(a)/len(a)
