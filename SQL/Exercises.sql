/*
SELECT	DISTINCT e.FirstName, e.Address, e.City, e.Region
  FROM  Employees as e
  JOIN  Orders as o
    ON  e.EmployeeID = o.EmployeeID
 WHERE  o.ShipCountry = 'Belgium';


SELECT	DISTINCT e.FirstName, e.LastName, sh.CompanyName, c.City
  FROM  Orders as o
  JOIN  Employees as e
    ON  o.EmployeeID = e.EmployeeID
  JOIN  Customers as c
    ON  o.CustomerID = c.CustomerID
  JOIN  Shippers as sh
    ON  o.ShipVia = sh.ShipperID
 WHERE  c.City = 'Bruxelles'
   AND  sh.CompanyName = 'Speedy Express';


SELECT	c.CustomerID, c.City
  FROM  Customers AS c
  JOIN  Customers AS cb
    ON  c.City = cb.City
 WHERE  cb.CustomerID = 'BOLID';


SELECT  p1.ProductName, p1.UnitPrice
  FROM  Products AS p1
  JOIN  Products AS p2
    ON  p1.UnitPrice > p2.UnitPrice
 WHERE  p2.ProductID = 1;


SELECT  e.FirstName, e.LastName, e.BirthDate
  FROM  Employees AS e
  JOIN  Employees AS el
    ON  e.BirthDate < el.BirthDate
 WHERE  el.City = 'London';


SELECT  e.FirstName, e.LastName, e.BirthDate
  FROM  Employees AS e
  JOIN  Employees AS el
    ON  e.BirthDate < el.BirthDate
 WHERE  el.City = 'London';


--------------------------------------

SELECT  DISTINCT p.ProductName
  FROM  [Order Details] AS od
  JOIN  Products AS p
    ON  od.ProductID = p.ProductID
  JOIN  [Order Details] AS od_sub
    ON  od.ProductID = od_sub.ProductID
  JOIN  Orders as o
    ON  od_sub.OrderID = o.OrderID
 WHERE  o.CustomerID IN ('ALFKI', 'QUEEN');

 
SELECT  DISTINCT p.ProductName, o.CustomerID
  FROM  [Order Details] AS od
  JOIN  Products AS p
    ON  od.ProductID = p.ProductID
  JOIN  Orders as o
    ON  od.OrderID = o.OrderID
 WHERE  o.CustomerID IN ('ALFKI', 'QUEEN');

 --------------------------------------


-- Exercise 13

   SELECT  c.CompanyName
     FROM  Customers AS c
LEFT JOIN  Orders AS o
       ON  c.CustomerID = o.CustomerID
	WHERE  o.OrderID IS NULL;


SELECT  c.CustomerID
  FROM  Customers AS c
EXCEPT
SELECT  o.CustomerID
  FROM  Orders AS o


-- Exercise 14 - Withount Union

SELECT  DISTINCT p.ProductID, p.ProductName

  FROM  Products AS p
  JOIN  [Order Details] AS od
    ON  p.ProductID = od.ProductID
  JOIN  Orders AS o
    ON  od.OrderID = o.OrderID
  JOIN  Employees AS e
    ON  o.EmployeeID = o.EmployeeID
  JOIN  Customers as c
    ON  o.CustomerID = c.CustomerID

 WHERE (c.City = 'London')
    OR (e.City = 'London');


-- Exercise 15

  SELECT  c.CategoryName, AVG(p.UnitPrice) AS AveragePrice
    FROM  Products AS p
	JOIN  Categories AS c
	  ON  p.CategoryID = c.CategoryID
GROUP BY  c.CategoryName;



  SELECT  od. OrderID, ROUND(SUM((od.UnitPrice * od.Quantity) * (1 - od.Discount)), 2) AS Subtotal
    FROM  [Order Details] as od
GROUP BY  od.OrderID;


  SELECT  YEAR(OrderDate) AS Year
		 ,MONTH(OrderDate) AS Month
		 ,COUNT(OrderID) AS NumberOfOrders
    FROM  Orders
GROUP BY  YEAR(OrderDate), MONTH(OrderDate)
ORDER BY  YEAR(OrderDate) DESC, MONTH(OrderDate) DESC;


-- Exercise 18
----------------------------------------------------------------------------------------------

    SELECT  p.ProductID, p.ProductName, SUM(od.Quantity) AS TotalOrdered
	  FROM  Products AS p
	  JOIN  [Order Details] AS od
	    ON  p.ProductID = od.ProductID
  GROUP BY  p.ProductID, p.ProductName
    HAVING  SUM(od.Quantity) >= ALL(SELECT  SUM(Quantity)
								     FROM  [Order Details]
							     GROUP BY  ProductID);

 ----------------------------------------------------------------------------------------------
 
 SELECT  e.FirstName, e.LastName, od.UnitPrice
    FROM  Employees AS e
	JOIN  Orders AS o
	  ON  o.EmployeeID = e.EmployeeID
	JOIN  [Order Details] AS od
	  ON  o.OrderID = od.OrderID
   WHERE  od.UnitPrice > (SELECT  MAX(od2.UnitPrice)
						    FROM  Employees AS e2
							JOIN  Orders AS o2
							  ON  o2.EmployeeID = e2.EmployeeID
							JOIN  [Order Details] AS od2
							  ON  o2.OrderID = od2.OrderID
						   WHERE  e2.FirstName = 'Steven' AND e2.LastName = 'Buchanan')
							
----------------------------------------------------------------------------------------------

SELECT  p.ProductID, p.ProductName
  FROM  Products AS p
 WHERE  p.UnitPrice > (SELECT AVG(UnitPrice)
						 FROM Products
						WHERE CategoryID = p.CategoryID)

----------------------------------------------------------------------------------------------
-- Exercise 19

  SELECT  c.CompanyName, p.ProductName, od.Quantity
    FROM  Orders AS o
	JOIN  [Order Details] AS od
	  ON  o.OrderID = od.OrderID
	JOIN  Customers AS c
	  ON  o.CustomerID = c.CustomerID
	JOIN  Products AS p
	  ON  od.ProductID = p.ProductID
   WHERE  od.Quantity > (SELECT  5 * AVG(Quantity)
						   FROM  [Order Details]
						  WHERE  ProductID = od.ProductID);

----------------------------------------------------------------------------------------------

SELECT  c.CustomerID, c.CompanyName, od.UnitPrice, od.ProductID, p.ProductName
  FROM  Customers AS c
  JOIN  Orders AS o
    ON  o.CustomerID = c.CustomerID
  JOIN  [Order Details] AS od
    ON  o.OrderID = od.OrderID
  JOIN  Products AS p
    ON  od.ProductID = p.ProductID
 WHERE  od.UnitPrice = (SELECT  MAX(od2.UnitPrice)
						  FROM  Orders AS o2
						  JOIN  [Order Details] AS od2
						    ON  o2.OrderID = od2.OrderID
						 WHERE  o2.CustomerID = o.CustomerID);

----------------------------------------------------------------------------------------------

  SELECT  o.EmployeeID, o.OrderID, o.OrderDate
    FROM  Orders AS o
   WHERE  o.OrderDate = (SELECT  MAX(OrderDate)
						   FROM  Orders
					      WHERE  EmployeeID = o.EmployeeID)
ORDER BY  o.EmployeeID;

----------------------------------------------------------------------------------------------
-- Exersice 20
SELECT  main.CustomerID, main.CompanyName
  FROM  Customers AS main
 WHERE  NOT EXISTS (SELECT  DISTINCT ProductID
					  FROM  [Order Details]
					 WHERE  UnitPrice < 5

					EXCEPT

					SELECT  od.ProductID
					  FROM  [Order Details] AS od
					  JOIN  Orders AS o
						ON  o.OrderID = od.OrderID
					 WHERE  o.CustomerID = main.CustomerID
					   AND  od.UnitPrice < 5);


  SELECT  o.CustomerID
    FROM  Orders AS o
    JOIN  [Order Details] AS od
      ON  o.OrderID = od.OrderID
   WHERE  od.UnitPrice < 5
GROUP BY  o.CustomerID
  HAVING  COUNT(DISTINCT(od.ProductID)) = (SELECT  COUNT (DISTINCT ProductID)
											 FROM  [Order Details]
										    WHERE  UnitPrice < 5);

----------------------------------------------------------------------------------------------

SELECT  DISTINCT c_outer.CompanyName
  FROM  Orders AS o_outer
  JOIN  Customers AS c_outer
    ON  o_outer.CustomerID = c_outer.CustomerID
  JOIN  [Order Details] AS od_outer
    ON  o_outer.OrderID = od_outer.OrderID
  JOIN  Products AS p_outer
    ON  od_outer.ProductID = p_outer.ProductID
 WHERE  NOT EXISTS (SELECT  CategoryID
					  FROM  Categories
					EXCEPT
					SELECT  CategoryID
					  FROM  Orders AS o_inner
					  JOIN  Customers AS c_inner
						ON  o_inner.CustomerID = c_inner.CustomerID
					  JOIN  [Order Details] AS od_inner
						ON  o_inner.OrderID = od_inner.OrderID
					  JOIN  Products AS p_inner
						ON  od_inner.ProductID = p_inner.ProductID
					 WHERE  o_inner.CustomerID = o_outer.CustomerID);


	SELECT  c.CustomerID, c.CompanyName
	  FROM  Customers AS c
	  JOIN  Orders AS o
		ON  o.CustomerID = c.CustomerID
	  JOIN  [Order Details] AS od
		ON  o.OrderID = od.OrderID
	  JOIN  Products AS p
		ON  od.ProductID = p.ProductID
  GROUP BY  c.CustomerID, c.CompanyName
    HAVING  COUNT(DISTINCT p.CategoryID) = (SELECT COUNT(*)
											  FROM Categories)

----------------------------------------------------------------------------------------------

SELECT  c_main.CustomerID, c_main.CompanyName
	FROM  Customers AS c_main
	JOIN  Orders AS o_main
	  ON  o_main.CustomerID = c_main.CustomerID
	JOIN  [Order Details] AS od_main
  	  ON  o_main.OrderID = od_main.OrderID
	JOIN  Products AS p
	  ON  od_main.ProductID = p.ProductID

GROUP BY  c_main.CustomerID, c_main.CompanyName

  HAVING  COUNT(DISTINCT od_main.ProductID) >= 3
	 AND  COUNT(p.CategoryID) = COUNT(DISTINCT p.CategoryID);

----------------------------------------------------------------------------------------------
SELECT LeaderBoard.EmployeeID, e.FirstName, e.LastName, LeaderBoard.OrdersPerEmp
  FROM (SELECT  TOP 1 EmployeeID, Count(OrderID) AS OrdersPerEmp
		  FROM  Orders
  	  GROUP BY  EmployeeID
	  ORDER BY  Count(OrderID) DESC) AS LeaderBoard
  JOIN Employees AS e
    ON LeaderBoard.EmployeeID = e.EmployeeID;
*/
----------------------------------------------------------------------------------------------

	SELECT	 OrderCategory.GroupName
			,COUNT(OrderTotals.OrderID) AS NumberOfOrders
			,AVG(OrderTotals.TotalPrice) AS AvergageOrderValue

	FROM	 (	SELECT  o.OrderID, SUM((od.UnitPrice * od.Quantity) * (1 - od.Discount)) AS TotalPrice
					FROM  Orders AS o
					JOIN  [Order Details] AS od
					ON  o.OrderID = od.OrderID
				GROUP BY  o.OrderID) AS OrderTotals

	JOIN	 (  SELECT 'Small'  AS GroupName, 0   AS LowerLimit,    49.99 AS UpperLimit
			UNION SELECT 'Medium' AS GroupName, 50  AS LowerLimit,    99.99 AS UpperLimit
			UNION SELECT 'Heavy'  AS GroupName, 100 AS LowerLimit, 99999.99 AS UpperLimit) AS OrderCategory

		ON	 OrderTotals.TotalPrice BETWEEN OrderCategory.LowerLimit AND OrderCategory.UpperLimit

GROUP BY	 OrderCategory.GroupName;

----------------------------------------------------------------------------------------------
