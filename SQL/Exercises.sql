/*
SELECT	DISTINCT e.FirstName, e.Address, e.City, e.Region
  FROM  Employees as e
  JOIN  Orders as o
    ON  e.EmployeeID = o.EmployeeID
 WHERE  o.ShipCountry = 'Belgium';
 */

/*
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
*/

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

-- With Union
SELECT  ProductID, ProductName
  FROM  Products

INTERSECT

( SELECT  