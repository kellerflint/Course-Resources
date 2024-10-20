
# Midterm Practice Solutions
## Back: [[SQL Analytics - Midterm Practice Questions|Midterm Practice Questions]]

### Without Grouping / Aggregation

```sql
/* #1 Display all products with a price between $10 and $20. */
SELECT ProductName, Price FROM Products
WHERE Price BETWEEN 10 and 20;
```

```sql
/* #2 List all employees born after 1960. */
SELECT FirstName, LastName, BirthDate
FROM Employees
WHERE BirthDate > '1960-12-31';
```

```sql
/* #3 Show the names of the first 5 customers and their country in alphabetical order. */
SELECT CustomerName, Country FROM Customers
ORDER BY CustomerName
LIMIT 5;
```

```sql
/* #4 List all orders placed in the year 1997. Display the most recent orders first. */
SELECT OrderID, OrderDate FROM Orders
WHERE OrderDate >= '1997-01-01' AND OrderDate < '1998-01-01'
ORDER BY OrderDate DESC;
```

```sql
/* #5 Show all product names that start with ethier the letter 'A' or the letter 'B'. */
SELECT ProductName FROM Products
WHERE ProductName LIKE 'A%' OR ProductName LIKE 'B%';
```
### With Grouping / Aggregation

```sql
/* #6 What is the average price of products in each category? */
SELECT CategoryID, AVG(Price) AS AveragePrice FROM Products
GROUP BY CategoryID;
```

```sql
/* #7 What are the earliest and latest dates that orders were placed in the Northwind database? */
SELECT 
    MIN(OrderDate) AS EarliestOrder,
    MAX(OrderDate) AS LatestOrder
FROM Orders;
```

```sql
/* #8 List the countries that have more than 5 customers. */
SELECT Country, COUNT(*) AS CustomerCount FROM Customers
GROUP BY Country
HAVING CustomerCount > 5;
```

```sql
/* #9 Show the suppliers that provide more than 3 products. */
SELECT SupplierID, COUNT(*) AS ProductCount FROM Products
GROUP BY SupplierID
HAVING ProductCount > 3;
```

```sql
/* #10 List the 3 countries that have the most customers. */
SELECT Country, COUNT(*) AS CustomerCount FROM Customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 3;
```

```sql
/* #11 Challenge: List the months in 1996 where 25 or more orders were placed. */
SELECT 
	MONTH(OrderDate) AS OrderMonth, 
    COUNT(*) AS OrderCount 
FROM Orders
WHERE YEAR(OrderDate) = '1996'
GROUP BY OrderMonth
HAVING OrderCount >= 25;
```