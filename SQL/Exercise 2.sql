USE CollegeDb;

DROP TABLE Products;

CREATE TABLE Products(
	ProductId INT PRIMARY KEY IDENTITY,
	Name VARCHAR(20) NOT NULL,
	Price SMALLMONEY NOT NULL CHECK (Price > 0),
	WeightKgs FLOAT(24) NOT NULL CHECK (WeightKgs >= 0 AND WeightKgs <= 100),
	UnitsInStock SMALLINT NOT NULL CHECK (UnitsInStock >= 0) DEFAULT 0
);

INSERT INTO Products
  	 VALUES ('Apple', 12.5, 0.2, 200),
			('Banana', 32.8, 0.7, 120),
			('Carrot', 5.1, 0.12, 1300),
			('Watermelon', 42, 1.2, 15),
			('Orange', 38, 1.8, 20),
			('Potato', 11.8, 1.8, 250);

UPDATE Products
   SET Price = Price * 0.9;

DELETE FROM Products
 WHERE Price > 30;