class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = "$" + str(price)
        self.speed = str(speed) + "mph"
        self.fuel = str(fuel)
        self.mileage = str(mileage) + "mpg"
        if price > 10000:
            self.tax = str(0.15)
        else:
            self.tax = str(0.12)
    def display_all(self):
        print "Price: " + self.price
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + self.tax

print "<<<Initializing car1>>>"
car1 = Car(2000,35,"Full",15)
car1.display_all()

print "<<<Initializing car2>>>"
car2 = Car(2000,5,"Not Full",105)
car2.display_all()

print "<<<Initializing car3>>>"
car3 = Car(2000,15,"Kind of Full",95)
car3.display_all()

print "<<<Initializing car4>>>"
car4 = Car(2000,25,"Full",25)
car4.display_all()

print "<<<Initializing car5>>>"
car5 = Car(2000,45,"Empty",25)
car5.display_all()

print "<<<Initializing car6>>>"
car6 = Car(20000000,35,"Empty",15)
car6.display_all()
