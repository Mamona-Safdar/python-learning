#HOSPITAL PATIENT MANAGEMENT SYSTEM
class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def show_info(self):
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def show_info(self):
        print(f"ID: {self.doctor_id}")
        print(f"Doctor: {self.name}")
        print(f"Specialization: {self.specialization}")


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def show_patients(self):
        if not self.patients:
            print("No patients found.")
            return

        for patient in self.patients:
            patient.show_info()
            print("----------------")

    def show_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return

        for doctor in self.doctors:
            doctor.show_info()
            print("----------------")


# Create hospital
hospital = Hospital()

# Create patients
patient1 = Patient(1, "Alia", 18, "Fever")
patient2 = Patient(2, "Ira", 20, "Flu")

# Create doctors
doctor1 = Doctor(101, "Dr. Izza", "Cardiology")
doctor2 = Doctor(102, "Dr. Milha", "Neurology")

# Add them to hospital
hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

# Display information
print("PATIENTS")
hospital.show_patients()

print("\nDOCTORS")
hospital.show_doctors()