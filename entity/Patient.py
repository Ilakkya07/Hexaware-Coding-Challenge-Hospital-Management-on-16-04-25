class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.patientId=patientId
        self.firstName=firstName
        self.lastName=lastName
        self.dateOfBirth=dateOfBirth
        self.gender=gender
        self.contactNumber=contactNumber
        self.address=address

    # Getter methods
    def get_patientId(self):
        return self.patientId

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_dateOfBirth(self):
        return self.dateOfBirth

    def get_gender(self):
        return self.gender

    def get_contactNumber(self):
        return self.contactNumber

    def get_address(self):
        return self.address

    # Setter methods
    def set_patientId(self, patientId):
        self.patientId=patientId

    def set_firstName(self, firstName):
        self.firstName=firstName

    def set_lastName(self, lastName):
        self.lastName=lastName

    def set_dateOfBirth(self, dateOfBirth):
        self.dateOfBirth=dateOfBirth

    def set_gender(self, gender):
        self.gender=gender

    def set_contactNumber(self, contactNumber):
        self.contactNumber=contactNumber

    def set_address(self, address):
        self.address=address

    # String representation
    def __str__(self):
        return f"Patient({self.patientId}, {self.firstName}, {self.lastName}, {self.dateOfBirth}, {self.gender}, {self.contactNumber}, {self.address})"
