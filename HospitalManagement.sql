create database HospitalManagement;
use HospitalManagement;

--Patient table
create table Patient (
    patientId int primary key,
    firstName varchar(50),
    lastName varchar(50),
    dateOfBirth date,
    gender varchar(15),
    contactNumber varchar(15),
    address varchar(100));

--Doctors table
create table Doctor(
    doctorId int primary key,
    firstName varchar(50),
    lastName varchar(50),
    specialization varchar(100),
    contactNumber varchar(15));

--Appointment table
create table Appointment(
    appointmentId int identity(1,1) primary key, 
    patientId int,
    doctorId int,
    appointmentDate date,
    description varchar(250),
    foreign key(patientId)references Patient(patientId),
    foreign key(doctorId)references Doctor(doctorId));

--inserting values 

insert into Patient(patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address)values
(1, 'Karthik', 'Kumar', '1988-04-12', 'Male', '9001000001', 'Coimbatore, Tamilnadu'),
(2, 'Ananya', 'Singh', '1991-09-21', 'Female', '9001000002', 'Pune, Maharashtra'),
(3, 'Rohit', 'Sharma', '1985-01-03', 'Male', '9001000003', 'Nagpur, Maharashtra'),
(4, 'Divya', 'Shri', '1993-12-19', 'Female', '9001000004', 'Chennai, Tamilnadu'),
(5, 'Amit', 'Khan', '1999-06-07', 'Male', '9001000005', 'Delhi, NCR'),
(6, 'Sumi', 'Balan', '1987-11-15', 'Female', '9001000006', 'Kochin, Kerala'),
(7, 'Rohan', 'Krishna', '1990-02-26', 'Male', '9001000007', 'Hyderabad, Andhra'),
(8, 'Neha', 'James', '1984-07-29', 'Female', '9001000008', 'Trivandrum, Kerala'),
(9, 'Aditya', 'Kumar', '1994-03-10', 'Male', '9001000009', 'Srinagar, Kashmir'),
(10, 'Pooja', 'Singh', '1986-05-22', 'Female', '9001000010', 'Jaipur, Rajasthan');


insert into Doctor (doctorId, firstName, lastName, specialization, contactNumber)values
(101, 'Dr. Amir', 'Nagul', 'Cardiologist', '9022011201'),
(102, 'Dr. Meera', 'William', 'Neurologist', '9022011202'),
(103, 'Dr. Raghav', 'Kumar', 'Orthopedic Surgeon', '9022011203'),
(104, 'Dr. Sneha', 'Sundaram', 'Pediatrician', '9022011204'),
(105, 'Dr. Nikhil', 'Ravi', 'Dermatologist', '9022011205'),
(106, 'Dr. Anika', 'Sundar', 'Physician', '9022011206'),
(107, 'Dr. Tarun', 'Reddy', 'Gynecologist', '9022011207'),
(108, 'Dr. Kavya', 'Shree', 'ENT Specialist', '9022011208'),
(109, 'Dr. Deepak', 'Ragu', 'Gastroenterologist', '9022011209'),
(110, 'Dr. Isha', 'Mahesh', 'Dental Surgeon', '9022011210');


insert into Appointment (patientId, doctorId, appointmentDate, description)values
(1, 101, '2025-05-01', 'Digestive health screening'),
(2, 102, '2025-05-02', 'Child regular checkup'),
(3, 103, '2025-05-03', 'Annual physical exam'),
(4, 104, '2025-05-04', 'General checkup'),
(5, 105, '2025-05-05', 'Sinus evaluation'),
(6, 106, '2025-05-06', 'Dental cavity check'),
(7, 107, '2025-05-07', 'Heart checkup'),
(8, 108, '2025-05-08', 'Kidney Diagnosis'),
(9, 109, '2025-05-09', 'Prenatal checkup'),
(10, 110, '2025-05-10', 'Skin rash analysis');


alter table Appointment drop column appointmentTime;
select * from Patient;
select * from Doctor;
select * from Appointment;