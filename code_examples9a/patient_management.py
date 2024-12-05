class Patient:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.medical_history = Medical_History({})

    def get_patient_details(self):
        self.patient_details = (
            f"{self.firstname.title()} {self.lastname.title(): {self.gender}}"
        )
        return self.patient_details


class Inpatient(Patient):
    def __init__(self, firstname, lastname, gender, room_number):
        super.__init__(firstname, lastname, gender)
        self.room_number = room_number

    def get_patient_details(self):
        self.patient_details = f"Name: {self.firstname.title()} {self.lastname.title()}\nGender: {self.gender}\nRoom Number: {self.room_number} "
        return self.patient_details


class OutPatient(Patient):
    def __init__(self, firstname, lastname, gender, appointment_date):
        super.__init__(firstname, lastname, gender)
        self.appointment_date = appointment_date

    def get_patient_details(self):
        self.patient_details = f"Name: {self.firstname.title()} {self.lastname.title()}\nGender: {self.gender}\nAppointment Date: {self.appointment_date} "
        return self.patient_details


class Medical_History:
    def __init__(self, medical_history):
        self.medical_history = medical_history

    def get_medical_history(self):
        return repr(self.medical_history)
