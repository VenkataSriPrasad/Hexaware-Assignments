from IHospitalService import HospitalService
from Appointment import Appointment
from datetime import date
from myexceptions import PatientNumberNotFoundException

class main:
    
    def get_appointment_by_id(self):
        print(hospital_service.get_appointment_by_id(1003), "\n")
        
    def get_appointments_for_patient(self):
        print(hospital_service.get_appointments_for_patient(102), "\n")
        
    def get_appointments_for_doctor(self):
        print(hospital_service.get_appointments_for_doctor(4), "\n")
        
    def schedule_appointment(self):
        new_appointment = Appointment(patientId=1, doctorId=1, appointmentDate=date(2023, 12, 31), description='New Appointment')
        print("Appointment Scheduled")
        
    def update_appointment(self):
        updated_appointment = Appointment(appointmentId=1, patientId=1, doctorId=1, appointmentDate=date(2023, 12, 31), description='Updated Appointment')
        print(hospital_service.update_appointment(updated_appointment))
    
    def cancel_appointment(self):
        print(hospital_service.cancel_appointment(1001))
        

if __name__ == "__main__":
    hospital_service = HospitalService( user='root', password='venkat', database='Hospital_Management_System')
    
    
    Execute = main()
    
    # Execute.get_appointment_by_id()
    
    # Execute.get_appointments_for_patient()
    
    # Execute.get_appointments_for_doctor()
    
    # Execute.schedule_appointment()
    
    # Execute.update_appointment()
    
    Execute.cancel_appointment()