-- Create Database
CREATE DATABASE hospital_db;
USE hospital_db;

-- Create Patients Table
CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('M', 'F') NOT NULL,
    diagnosis VARCHAR(255)
);

-- Create Doctors Table
CREATE TABLE doctors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    contact VARCHAR(15)
);

-- Create Appointments Table
CREATE TABLE appointments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
);

-- Insert Sample Data for Testing
INSERT INTO patients (name, age, gender, diagnosis) 
VALUES 
    ('John Doe', 35, 'M', 'Flu'),
    ('Jane Smith', 29, 'F', 'Allergy');

INSERT INTO doctors (name, specialization, contact) 
VALUES 
    ('Dr. Adams', 'Cardiology', '1234567890'),
    ('Dr. Brown', 'Dermatology', '0987654321');

INSERT INTO appointments (patient_id, doctor_id, date) 
VALUES 
    (1, 1, '2024-12-25'),
    (2, 2, '2024-12-26');
