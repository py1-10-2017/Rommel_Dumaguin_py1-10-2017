class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display(self):
        print "$" + str(self.price)
        print self.max_speed
        print str(self.miles) + " miles"
        return self
    def ride(self):
        print "Riding (+10 miles)"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing (-5 miles)"
        # What would you do to prevent the instance from having negative miles?
        if self.miles >= 5:
            self.miles -= 5
        return self

print "<<<Initializing bike1>>>"
bike1 = Bike(200,"25mph")
bike1.ride().ride().ride().reverse()
bike1.display()

print "<<<Initializing bike2>>>"
bike2 = Bike(250,"30mph")
bike2.ride().ride().reverse().reverse()
bike2.display()

print "<<<Initializing bike3>>>"
bike3 = Bike(250,"30mph")
bike3.reverse().reverse().reverse()
bike3.display()
