import time
import uuid

class Call(object):
    unique_id = 0
    def __init__(self, name, phone_number, reason_for_call):
        Call.unique_id += 1
        self.unique_id = Call.unique_id
        self.name = name
        self.phone_number = phone_number
        self.time_of_call = time.strftime("%H:%M:%S")
        self.reason_for_call = reason_for_call
        self.display() # Display info after they're set

    def display(self):
        print "unique_id: " + str(self.unique_id)
        print "name: " + str(self.name)
        print "phone_number: " + str(self.phone_number)
        print "time_of_call: " + str(self.time_of_call)
        print "reason_for_call: " + str(self.reason_for_call)
        return self

call1 = Call("Amy", 1234567890, "Help")

print "-"*100

class CallCenter(object):
    def __init__(self):
        self.calls = []
        # self.queue_size = len(self.calls)
            # Can't call this since it only holds the initial value of 'len(self.calls)' which is '0'
        # self.queue_size = self.get_queue_size()
            # This doesn't work either. self.queue_size only gets the initial value of the function.

    # def get_queue_size(self):
    #     return len(self.calls)

    def add(self, call):
        # adds a new call to the end of the call list
        self.calls.append(call)
        return self

    def remove(self):
        # removes the call from the beginning of the list (index 0)
        self.calls.remove(self.calls[0])
        return self

    def info(self):
        # prints the name and phone number for each call in the queue as well as the length of the queue
        for caller in self.calls:
            print caller.name,"-",caller.phone_number
        # print "Queue size: " + str(self.queue_size)
        print "Queue size: " + str(len(self.calls))
        return self

    def drop_caller(self, number):
        # Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
        # idx_matching_number = "False"
        # for idx, caller in enumerate(self.calls):
        #     print idx, caller
        #     if caller.phone_number == number:
        #         idx_matching_number = idx
        #         print "idx_matching_number:",idx_matching_number
        #     else:
        #         print "!= number"
        # if idx_matching_number != "False":
        #     print "Dropping object 'idx' with phone_number", number
        #     self.calls.remove(self.calls[idx_matching_number])
        #     self.queue_size = len(self.calls)
        #     return self
        # else:
        #     print "No matching numbers found"
        #     return self
        self.calls = [caller for caller in self.calls if caller.phone_number != number]
        return self

callcenter1 = CallCenter()
callcenter1.add(call1)
call2 = Call("Sarah", 5552225555, "Help2")
callcenter1.add(call2)
print callcenter1.calls
print "-"*100

print "<<<removing the call from the beginning of the list (index 0)>>>"
print "callcenter1.remove(): "
callcenter1.remove()
print callcenter1.calls
print "-"*100

print "callcenter1.add(call3)"
call3 = Call("Kim", 1112223333, "Help3")
callcenter1.add(call3)
callcenter1.info()
print "-"*100

print callcenter1.calls
print "callcenter1.drop_caller(number)"
callcenter1.drop_caller(5552225555)
callcenter1.info()
print callcenter1.calls
