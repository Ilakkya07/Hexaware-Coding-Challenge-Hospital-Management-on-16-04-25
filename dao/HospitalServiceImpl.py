import sys
import os
import pyodbc
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.IHospitalService import IHospitalService
from entity.Appointment import Appointment
from exceptions.PatientNotFoundException import PatientNumberNotFoundException
from util.DBConnection import DBConnUtil

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.conn=DBConnUtil.getConnection()

    def getAppointmentById(self, appointmentId):
        cursor=self.conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE appointmentId=?", (appointmentId,))
        row=cursor.fetchone()
        if row:
            return Appointment(*row)
        else:
            return None

    def getAppointmentsForPatient(self, patientId):
        cursor=self.conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE patientId=?", (patientId,))
        rows=cursor.fetchall()
        if not rows:
            raise PatientNumberNotFoundException("Patient ID not found in DB.")
        return [Appointment(*row) for row in rows]

    def getAppointmentsForDoctor(self, doctorId):
        cursor=self.conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE doctorId=?", (doctorId,))
        rows=cursor.fetchall()
        return [Appointment(*row) for row in rows]

    def scheduleAppointment(self, appointment):
        cursor=self.conn.cursor()

        # Check if the doctorId exists in the Doctor table
        cursor.execute("SELECT COUNT(1) FROM Doctor WHERE doctorId=?", (appointment.doctorId,))
        if cursor.fetchone()[0] == 0:
            print(f"Error: Doctor ID {appointment.doctorId} does not exist.")
            return False

        try:
            if isinstance(appointment.appointmentDate, str):
                appointment.appointmentDate = datetime.strptime(appointment.appointmentDate, "%Y-%m-%d").date()

            cursor.execute("""
                INSERT INTO Appointment (doctorId, patientId, appointmentDate, description)
                VALUES (?, ?, ?, ?)
            """, (appointment.doctorId,
                  appointment.patientId,
                  appointment.appointmentDate,
                  appointment.description))
            self.conn.commit()
            print("Appointment scheduled successfully.")
            return True
        except pyodbc.Error as e:
            print(f"Error scheduling appointment: {e}")
            return False

    def updateAppointment(self, appointment):
        cursor=self.conn.cursor()
        query= """
        UPDATE Appointment
        SET patientId=?, doctorId=?, appointmentDate=?, description=?
        WHERE appointmentId=?
        """
        try:
            if isinstance(appointment.get_appointmentDate(), str):
                appointment.set_appointmentDate(datetime.strptime(appointment.get_appointmentDate(), "%Y-%m-%d").date())

            new_patientId=input("Enter New Patient ID: ")
            new_doctorId=input("Enter New Doctor ID: ")
            new_appointmentDate=input("Enter New Appointment Date (YYYY-MM-DD): ")
            new_description=input("Enter New Appointment Description: ")

            cursor.execute("SELECT COUNT(1) FROM Patient WHERE patientId=?", (new_patientId,))
            if cursor.fetchone()[0] == 0:
                print(f"Error: Patient ID {new_patientId} does not exist.")
                return False
            cursor.execute("SELECT COUNT(1) FROM Doctor WHERE doctorId=?", (new_doctorId,))
            if cursor.fetchone()[0] == 0:
                print(f"Error: Doctor ID {new_doctorId} does not exist.")
                return False

            appointment.set_patientId(new_patientId)
            appointment.set_doctorId(new_doctorId)
            appointment.set_appointmentDate(datetime.strptime(new_appointmentDate, "%Y-%m-%d").date())
            appointment.set_description(new_description)

            cursor.execute(query, (
                appointment.get_patientId(),
                appointment.get_doctorId(),
                appointment.get_appointmentDate(),
                appointment.get_description(),
                appointment.get_appointmentId()
            ))
            self.conn.commit()
            print("Appointment updated successfully.")
            return True
        except Exception as e:
            print(f"Error updating appointment: {e}")
            return False

    def cancelAppointment(self, appointmentId):
        cursor=self.conn.cursor()
        query="DELETE FROM Appointment WHERE appointmentId=?"
        try:
            cursor.execute(query, (appointmentId,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error canceling appointment: {e}")
            return False
