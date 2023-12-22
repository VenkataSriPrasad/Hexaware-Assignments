import mysql.connector
from Appointment import Appointment
from Patient import Patient
from Doctor import Doctor
from datetime import date
from myexceptions import PatientNumberNotFoundException

class HospitalService:
    def __init__(self, user, password, database):
        try:
            # Connect to the MySQL server
            self.connection = mysql.connector.connect(
                user='root',
                password='venkat',
                database='Hospital_Management_System',
                port=3305
            )
            print("Database Connection Succesfull")
            # Create a cursor to execute SQL queries
            self.cursor = self.connection.cursor()

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Access denied. Check your username and password.")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exist.")
            else:
                print("Error:", err)
            


    def get_appointment_by_id(self, appointment_id: int):
        query = "SELECT * FROM appointment WHERE appointmentId = %s"
        self.cursor.execute(query, (appointment_id,))
        result = self.cursor.fetchone()

        if result:
            print(result[0], result[1], result[2], result[3], result[4])

    def get_appointments_for_patient(self, patient_id: int):
        query = "SELECT * FROM appointment WHERE patientId = %s"
        self.cursor.execute(query, (patient_id,))
        results = self.cursor.fetchall()
        
        if not results:
            raise PatientNumberNotFoundException(f"No appointments found for Patient with ID {patient_id}")

        appointments = []
        for result in results:
            print(result[0], result[1], result[2], result[3], result[4])
            appointments.append(result)

        return appointments

    def get_appointments_for_doctor(self, doctor_id: int):
        query = "SELECT * FROM appointment WHERE doctorId = %s"
        self.cursor.execute(query, (doctor_id,))
        results = self.cursor.fetchall()

        appointments = []
        for result in results:
            print(result[0], result[1], result[2], result[3], result[4])
            appointments.append(result)

        return appointments

    def schedule_appointment(self, appointment: Appointment):
        query = "INSERT INTO appointment (appointmentId,patientId, doctorId, appointmentDate, description) VALUES (%s, %s, %s, %s, %s)"
        print("Appointment is  scheduled" )
        values = (appointment[0], appointment[1], appointment[2], appointment[3],appointment[4])
        # self.cursor.execute(query, values)
        # self.connection.commit()
        return True

    def update_appointment(self, appointment: Appointment):
        query = "UPDATE appointment SET appointmentDate = %s, description = %s WHERE appointmentId = %s"
        values = (appointment.appointmentDate, appointment.description, appointment.appointmentId)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Appointment is Updated")
        return True

    def cancel_appointment(self, appointment_id: int):
        query = "DELETE FROM appointment WHERE appointmentId = %s"
        self.cursor.execute(query, (appointment_id,))
        self.connection.commit()
        print("Delection Successfull")
        return True
    
    









