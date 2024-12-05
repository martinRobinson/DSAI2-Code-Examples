from patient_management import InPatient, OutPatient


patient1 = InPatient("albert", "einstein", "male")
patient2 = OutPatient("marie", "curie", "female")

patient1.medical_history = {1: "flu", 2: "mumps"}
patient1.get_medical_history()
