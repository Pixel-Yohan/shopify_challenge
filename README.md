## Shopify Challenge Question 1
**a) Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.**
Answer: Because the average of the orders is being taken the data is skewing tailside towards the big orders. A better way to evaluate this data is by taking the median of all order amounts.

**b) What metric would you report for this dataset?**
Answer: The Median would be a better metric as it's not prone to skewing at really large or really small tailsides. 
**c) What is its value?**
Answer: $284.0/per order amount which sounds a lot more reasonable for a sneaker compared to the AOV of $3145.13

## Shopify Challenge Quesiton 2 (SQL)

**a) How many orders were shipped by Speedy Express in total?** 
**Answer: 54**
SQL Query: 
```SQL
SELECT COUNT(ShipperID) FROM (
	SELECT Shippers.ShipperID, Orders.ShipperID, Orders.OrderID, Shippers.ShipperName
	FROM Orders
	INNER JOIN Shippers ON Shippers.ShipperID=Orders.ShipperID
)
WHERE ShipperID = 1;
```
**b) What is the last name of the employee with the most orders?**
**Answer: Peacock (40 orders)**
```SQL
SELECT LastName, MAX (ordercount)
FROM (SELECT Employees.EmployeeID, Orders.EmployeeID, Employees.LastName , COUNT(Employees.LastName) ordercount
		FROM Orders
		INNER JOIN Employees ON Employees.EmployeeID=Orders.EmployeeID
        GROUP BY Employees.LastName
        );
```
**c) What product was ordered the most by customers in Germany?**
**Answer:**
```SQL
SELECT Customers.CustomerID, Customers.Country, Orders.CustomerID, Orders.OrderID, OrderDetails.OrderID, OrderDetails.ProductID, Products.ProductID, Products.ProductName
FROM (((Customers
	INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID)
    INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID)
    INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID)
WHERE Customers.Country = "Germany"
```
