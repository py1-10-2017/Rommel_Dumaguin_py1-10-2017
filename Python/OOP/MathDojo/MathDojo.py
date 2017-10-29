class MathDojo(object):
    def __init__(self):
        self.current_number = 0

    def add(self, *args):
        if args:
            for num in args:
                    if isinstance(num, int) or isinstance(num, float):
                        self.current_number += num
                    elif isinstance(num, list):
                        for idx in num:
                            self.current_number += idx
                    elif isinstance(num, tuple):
                        for idx in num:
                            self.current_number += idx
                    else:
                        print "Arguments must be an number or a list"
        return self

    def subtract(self, *args):
        if args:
            for num in args:
                    if isinstance(num, int) or isinstance(num, float):
                        self.current_number -= num
                    elif isinstance(num, list):
                        for idx in num:
                            self.current_number -= idx
                    elif isinstance(num, tuple):
                        for idx in num:
                            self.current_number -= idx
                    else:
                        print "Arguments must be an number or a list"
        return self

    def result(self):
        print self.current_number
        return self

md = MathDojo()
print "md.add(2).add(2,5).subtract(3,2).result():"
md.add(2).add(2,5).subtract(3,2).result()
print "-"*100
print "md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result():"
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
print "-"*100
md.add(1).add([1,2,3]).subtract((10,25)).add((1,.4)).result()
