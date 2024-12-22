import mysql.connector # To work with MySQL
import datetime  # To work with datetime functions


# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",  # Database host
    user="root",  # MySQL username
    password="password",  # MySQL password
    database="hospital_db"  # Database name
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to add a new patient to the database
def add_patient():
    # Take user input for patient details
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (M/F): ")
    diagnosis = input("Enter Diagnosis: ")

    # Prepare the SQL query to insert the new patient
    query = "INSERT INTO patients (name, age, gender, diagnosis) VALUES (%s, %s, %s, %s)"
    values = (name, age, gender, diagnosis)

    # Execute the query and commit the changes to the database
    cursor.execute(query, values)
    db.commit()
    print("Patient added successfully!")

# Function to add a new doctor to the database
def add_doctor():
    # Take user input for doctor details
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    contact = input("Enter Contact Number: ")

    # Prepare the SQL query to insert the new doctor
    query = "INSERT INTO doctors (name, specialization, contact) VALUES (%s, %s, %s)"
    values = (name, specialization, contact)

    # Execute the query and commit the changes to the database
    cursor.execute(query, values)
    db.commit()
    print("Doctor added successfully!")

# Function to schedule an appointment between a patient and a doctor
def schedule_appointment():
    # Take user input for appointment details
    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    date = input("Enter Appointment Date (YYYY-MM-DD): ")

    # Prepare the SQL query to schedule the appointment
    query = "INSERT INTO appointments (patient_id, doctor_id, date) VALUES (%s, %s, %s)"
    values = (patient_id, doctor_id, date)

    # Execute the query and commit the changes to the database
    cursor.execute(query, values)
    db.commit()
    print("Appointment scheduled successfully!")

# Function to view all patients in the system
def view_patients():
    # Execute the SQL query to fetch all patients
    cursor.execute("SELECT * FROM patients")
    records = cursor.fetchall()
    print("Patients:")
    
    # Loop through the records and print them
    for row in records:
        print(row)

# Function to view all doctors in the system
def view_doctors():
    # Execute the SQL query to fetch all doctors
    cursor.execute("SELECT * FROM doctors")
    records = cursor.fetchall()
    print("Doctors:")
    
    # Loop through the records and print them
    for row in records:
        print(row)

# Function to view all appointments scheduled in the system
def view_appointments():
    # Execute the SQL query to join appointments with patients and doctors
    cursor.execute("""
        SELECT appointments.id, patients.name, doctors.name, appointments.date
        FROM appointments
        JOIN patients ON appointments.patient_id = patients.id
        JOIN doctors ON appointments.doctor_id = doctors.id
    """)
    records = cursor.fetchall()
    print("Appointments:")
    
    # Loop through the records and print them
    for row in records:
        print(row)

# Menu-driven interface for interacting with the system
def main_menu():
    while True:
        # Display options to the user
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")
        
        # Take user input for the chosen option
        choice = int(input("Enter your choice: "))
        
        # Perform actions based on user input
        if choice == 1:
            add_patient()
        elif choice == 2:
            add_doctor()
        elif choice == 3:
            schedule_appointment()
        elif choice == 4:
            view_patients()
        elif choice == 5:
            view_doctors()
        elif choice == 6:
            view_appointments()
        elif choice == 7:
            print("Exiting...")
            break  # Exit the loop
        else:
            print("Invalid choice! Please try again.")

# Run the program by calling the main menu function
main_menu()

# Close database connection after the program finishes
cursor.close()
db.close()
