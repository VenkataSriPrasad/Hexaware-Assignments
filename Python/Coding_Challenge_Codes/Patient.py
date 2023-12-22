class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.patientId = patientId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address


# #Sample data
#     def print_details(self):
#         print("Patient ID:", self.patientId)
#         print("First Name:", self.firstName)
#         print("Last Name:", self.lastName)
#         print("Date of Birth:", self.dateOfBirth)
#         print("Gender:", self.gender)
#         print("Contact Number:", self.contactNumber)
#         print("Address:", self.address)
        
# patient = Patient(patientId=101, firstName='Aishwarya', lastName='Suresh', dateOfBirth='1990-05-15', gender='F', contactNumber='8765432101', address='123, MG Road, Bangalore')
# patient.print_details()