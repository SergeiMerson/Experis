-- CREATE DATABASE CollegeDb;


DROP TABLE Students;

CREATE TABLE Students(
	StudentId CHAR(9) PRIMARY KEY,
	FirstName VARCHAR(20) NOT NULL,
	LastName VARCHAR(20) NOT NULL,
	Gender CHAR(1) CHECK (Gender IN ('M', 'F')) DEFAULT 'M',
	BirthDate DATE CHECK (BirthDate < GETDATE()),
	Email VARCHAR(30) NOT NULL UNIQUE
);


INSERT INTO Students (StudentId, FirstName, LastName, Email)
	 VALUES ('333203302', 'Roi', 'Yehoshua', 'roiyeh@yahoo.com');

INSERT INTO Students
	 VALUES ('321234321', 'John', 'Shith', 'M', '1985/10/30', 'john.smith@gmail.com'),
	        ('123456789', 'Mark', 'Israeli', 'M', NULL, 'israeli302@outlook.com');