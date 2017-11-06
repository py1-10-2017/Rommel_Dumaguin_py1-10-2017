# OPTIONAL ASSIGNMENT - WIP

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
