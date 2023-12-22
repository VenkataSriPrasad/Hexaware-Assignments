class Doctor:
    def __init__(self, doctorId=None, firstName=None, lastName=None, specialization=None, contactNumber=None):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

# #Sample Data
#     def print_details(self):
#         print("Doctor ID:", self.doctorId)
#         print("First Name:", self.firstName)
#         print("Last Name:", self.lastName)
#         print("Specialization:", self.specialization)
#         print("Contact Number:", self.contactNumber)

# doctor = Doctor(doctorId=1, firstName='Rajesh', lastName='Kumar', specialization='Cardiologist', contactNumber='9876543210')
# doctor.print_details()
