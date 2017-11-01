class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity # an integer indicating the maximum number of patients the hospital can hold.
    def admit(self, id):
        # add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
        self.bed_num = self.capacity
        return self
    def discharge(self):
        # look up and remove a patient from the list of patients. Change bed number for that patient back to none.

        return self

hospital1 = Hospital("Virginia Mason", 250)
hospital1.admit(1).discharge()

class Patient(object):
    def __init__(self, id, name, allergies, bed_num):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_num = 0 # should be none by default

# import time
# import uuid
#
# class Call(object):
#     def __init__(self, id, name, phone_number, reason_for_call):
#         self.unique_id = id
#         self.name = name
#         self.phone_number = phone_number
#         self.time_of_call = time.strftime("%H:%M:%S")
#         self.reason_for_call = reason_for_call
#     def display(self):
#         print "unique_id: " + str(self.unique_id)
#         print "name: " + str(self.name)
#         print "phone_number: " + str(self.phone_number)
#         print "time_of_call: " + str(self.time_of_call)
#         print "reason_for_call: " + str(self.reason_for_call)
#         return self
#
# call1 = Call(uuid.uuid4(), "Amy", 1234567890, "Help")
# # call1.unique_id = id(call1)
#     # uuid.uuid4() seems to be the popular choice on stackoverflow
#     # If all you want is a unique ID, you should probably call uuid1() or uuid4(). Note that uuid1() may compromise privacy since it creates a UUID containing the computer's network address. uuid4() creates a random UUID.
# call1.display()
#
# print "-"*100
#
# class CallCenter(object):
#     def __init__(self):
#         self.calls = []
#         # self.queue_size = len(self.calls)
#             # doesn't work when called here
#     def add(self, call):
#         # adds a new call to the end of the call list
#         self.calls.append(call)
#         self.queue_size = len(self.calls)
#         return self
#     def remove(self):
#         # removes the call from the beginning of the list (index 0)
#         self.calls.remove(self.calls[0])
#         self.queue_size = len(self.calls)
#         return self
#     def info(self):
#         # prints the name and phone number for each call in the queue as well as the length of the queue
#         for caller in self.calls:
#             print caller.name,"-",caller.phone_number
#         print "Queue size: " + str(callcenter1.queue_size)
#         return self
#     def drop_caller(self, number):
#         # Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
#         # idx_matching_number = "False"
#         # for idx, caller in enumerate(self.calls):
#         #     print idx, caller
#         #     if caller.phone_number == number:
#         #         idx_matching_number = idx
#         #         print "idx_matching_number:",idx_matching_number
#         #     else:
#         #         print "!= number"
#         # if idx_matching_number != "False":
#         #     print "Dropping object 'idx' with phone_number", number
#         #     self.calls.remove(self.calls[idx_matching_number])
#         #     self.queue_size = len(self.calls)
#         #     return self
#         # else:
#         #     print "No matching numbers found"
#         #     return self
#         self.calls = [caller for caller in self.calls if caller.phone_number != number]
#         self.queue_size = len(self.calls)
#         return self
#
# callcenter1 = CallCenter()
# callcenter1.add(call1)
# call2 = Call(uuid.uuid4(), "Sarah", 5552225555, "Help2")
# callcenter1.add(call2)
# print callcenter1.calls
# print "Queue size: " + str(callcenter1.queue_size)
# print "-"*100
#
# print "<<<removing the call from the beginning of the list (index 0)>>>"
# print "callcenter1.remove(): "
# callcenter1.remove()
# print callcenter1.calls
# print "Queue size: " + str(callcenter1.queue_size)
# print "-"*100
#
# print "callcenter1.add(call3)"
# call3 = Call(uuid.uuid4(), "Kim", 1112223333, "Help3")
# callcenter1.add(call3)
# callcenter1.info()
# print "-"*100
#
# print callcenter1.calls
# print "callcenter1.drop_caller(number)"
# callcenter1.drop_caller(5552225555)
# callcenter1.info()
# print callcenter1.calls
