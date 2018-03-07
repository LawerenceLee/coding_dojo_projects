import hashlib


class Patient():
    def __init__(self, name, allergies=""):
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.id = hashlib.sha512(name + allergies).hexdigest()[-8:].upper()

    def __str__(self):
        return "PATIENT-ID: {}\nNAME: {}\nALLERGIES: {}\nBED No.: {}".format(
            self.id, self.name, self.allergies, self.bed_number)


class Hospital():
    patients = []

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.beds = range(1, self.capacity+1)

    def admit(self, patient):
        if len(self.patients) == self.capacity:
            print("Hospital is Full, Sorry")
        else:
            patient.bed_number = self.beds.pop()
            self.patients.append(patient)
            print("Patient has been successfully admitted")

    def discharge(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                self.beds.append(patient.bed_number)
                self.patients.remove(patient)
                print("Patient Successfully Discharged")
            else:
                print("Patient Not Found")

    def __str__(self):
        return "Hospital: {}\nCapacity: {}\nNo. of Patients: {}".format(
            self.name, self.capacity, len(self.patients)
        )


joe = Patient("Joe Shmoe")
print(joe)

bates_hospital = Hospital("Bates Hospital", 2)
print(bates_hospital)
print("")

bates_hospital.admit(joe)
print(bates_hospital)
print("")
print(joe)
print("")

betty = Patient("Betty")
print(betty)
print("")

bates_hospital.admit(betty)
print(bates_hospital)
print("")
print(betty)

print("")
bates_hospital.discharge("Joe Shmoe")
print(bates_hospital)
