
class PatientNumberNotFoundException(Exception):
    def __init__(self, patient_id):
        super().__init__(f"Patient with ID {patient_id} not found in the database.")
