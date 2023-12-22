class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None, description=None):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

# # Sample data
#     def print_details(self):
#         print("Appointment ID:", self.appointmentId)
#         print("Patient ID:", self.patientId)
#         print("Doctor ID:", self.doctorId)
#         print("Appointment Date:", self.appointmentDate)
#         print("Description:", self.description)
           
# appointment = Appointment(appointmentId=1001, patientId=101, doctorId=1, appointmentDate='2023-01-10', description='Routine checkup')
# appointment.print_details()  