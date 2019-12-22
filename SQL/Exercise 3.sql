-- CREATE DATABASE FlightsDB;

USE FlightsDB;

CREATE TABLE Airlines(
	AirlineId INT IDENTITY PRIMARY KEY,
	Name VARCHAR(30) NOT NULL
);

CREATE TABLE Countries(
	CountryId INT IDENTITY PRIMARY KEY,
	CountryName VARCHAR(30) NOT NULL
	);

CREATE TABLE Cities(
	CityId INT IDENTITY PRIMARY KEY,
	CityName VARCHAR(30) NOT NULL,
	CountryId INT FOREIGN KEY REFERENCES Countries(CountryId)
	);

CREATE TABLE Flights(
	FlightNumber VARCHAR(8) PRIMARY KEY,
	AirlineId INT FOREIGN KEY REFERENCES Airlines(AirlineId),
	SourceCityId INT FOREIGN KEY REFERENCES Cities(CityId),
	DestinationCityId INT FOREIGN KEY REFERENCES Cities(CityId),
	DepartureTime TIME NOT NULL,
	ArrivalTime TIME NOT NULL,
	FlightDuration FLOAT(24) CHECK (FlightDuration > 0),
	SeatsNumber SMALLINT CHECK (SeatsNumber > 0 AND SeatsNumber < 500)
);

CREATE TABLE Departures(
	DepartureId INT IDENTITY PRIMARY KEY,
	FlightNumber VARCHAR(8) FOREIGN KEY REFERENCES Flights(FlightNumber),
	DepartureDate DATETIME NOT NULL,
	Price FLOAT(24) NOT NULL CHECK (Price > 0),
	SeatsAvailable SMALLINT NOT NULL CHECK (SeatsAvailable >= 0)
);

CREATE TABLE Passengers(
	PassengerId INT IDENTITY PRIMARY KEY,
	Password VARCHAR(20) NOT NULL,
	FirstName VARCHAR(20) NOT NULL,
	LastName VARCHAR(20) NOT NULL,
	Address VARCHAR(30),
	PhoneNumber CHAR(14),
	Email VARCHAR(30)
);

CREATE TABLE Bookings(
	PassengerId INT FOREIGN KEY REFERENCES Passengers(PassengerId),
	DepartureId INT FOREIGN KEY REFERENCES Departures(DepartureId),
	ReservationDate DATETIME NOT NULL CHECK (ReservationDate < GETDATE()),
	SeatNumber CHAR(4) NOT NULL
	PRIMARY KEY (PassengerId, DepartureId)
);

CREATE TABLE WaitingList(
	PassengerId INT FOREIGN KEY REFERENCES Passengers(PassengerId),
	DepartureId INT FOREIGN KEY REFERENCES Departures(DepartureId),
	NumberInList SMALLINT,
	PRIMARY KEY (PassengerId, DepartureId, NumberInList)
);
