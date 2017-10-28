class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.retail_price = price
        self.total_price = price
        self.item_name = str(item_name)
        self.weight = weight
        self.brand = str(brand)
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.total_price += (self.total_price * float(tax))
        return self

    def return_item(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.total_price = 0
        elif reason == "new":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.total_price -= (self.total_price * .2)
        return self

    def display_all(self):
        print "Retail price: $" + str(self.retail_price)
        print "Total price: $" + str(int(self.total_price))
        print "Item name: " + str(self.item_name)
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)
        print "-" * 100
        return self

print "<<<Initializing product1>>>"
product1 = Product(100,"Xbox","25lb","Microsoft")
product1.add_tax(.12).return_item("opened").display_all()
print "<<<Initializing product2>>>"
product2 = Product(200,"Playstation","35lb","Sony")
product2.add_tax(.12).return_item("defective").display_all()
print "<<<Initializing product3>>>"
product3 = Product(1500,"Laptop","15lb","Alienware")
product3.add_tax(.12).sell().display_all()
print "<<<Initializing product1>>>"
product1 = Product(150,"Wii","15lb","Nintendo")
product1.add_tax(.12).return_item("new").display_all()
