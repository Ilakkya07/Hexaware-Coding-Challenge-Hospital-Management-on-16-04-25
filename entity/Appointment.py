class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None, description=None):
        self.appointmentId=appointmentId
        self.patientId=patientId
        self.doctorId=doctorId
        self.appointmentDate=appointmentDate
        self.description=description

    # Getter methods
    def get_appointmentId(self):
        return self.appointmentId

    def get_patientId(self):
        return self.patientId

    def get_doctorId(self):
        return self.doctorId

    def get_appointmentDate(self):
        return self.appointmentDate  

    def get_description(self):
        return self.description

    # Setter methods
    def set_appointmentId(self, appointmentId):
        self.appointmentId=appointmentId

    def set_patientId(self, patientId):
        self.patientId=patientId

    def set_doctorId(self, doctorId):
        self.doctorId=doctorId

    def set_appointmentDate(self, appointmentDate):
        self.appointmentDate=appointmentDate

    def set_description(self, description):
        self.description=description

    # String representation
    def __str__(self):
        return f"Appointment({self.appointmentId}, {self.patientId}, {self.doctorId}, {self.appointmentDate}, {self.description})"
