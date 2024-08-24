### See Questions: [[SQL Analytics Final - Practice Questions]]
# Final Practice Solutions

Write a query to show the order ID, order date of orders and the first and last name of the employee who handled the order. Only show orders placed in September, October, November or December. Show recent orders first.

*Remember that you can use MONTH(ColumnName) to get the month.*

```sql
SELECT OrderID, OrderDate, FirstName, LastName FROM orders
JOIN employees ON orders.EmployeeID = employees.EmployeeID
WHERE MONTH(OrderDate) >= 9
ORDER BY LastName;
```

Write a query to display the order ID, customer name, and employee last name for all customers whose names start with 'A'. Sort the results by order ID in descending order.

```sql
SELECT orders.OrderID, customers.CustomerName, employees.LastName FROM orders
JOIN customers ON orders.CustomerID = customers.CustomerID
JOIN employees ON orders.EmployeeID = employees.EmployeeID
WHERE customers.CustomerName LIKE 'A%'
ORDER BY orders.OrderID DESC;
```

Write a query to list all products with a price between `$20` and `$50`, and that belong to category ID 3 or 5. Display the product name, price, and category ID. Sort the results by price in ascending order.

```sql
SELECT ProductName, Price, CategoryID FROM products
WHERE Price BETWEEN 20 AND 50 AND CategoryID IN (3, 5)
ORDER BY Price ASC;
```

Write a query to display the supplier name and the number of products they supply. Only include suppliers who supply more than 3 products. Order the results by the number of products in descending order.

```sql
SELECT 
	suppliers.SupplierName, 
	COUNT(products.ProductID) AS NumberOfProducts 
FROM suppliers
JOIN products ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.SupplierID, suppliers.SupplierName
HAVING COUNT(products.ProductID) > 3
ORDER BY COUNT(products.ProductID) DESC;
```

Write a query to show the category name and the total quantity of products ordered for each category. Only include categories where the total quantity ordered is more than 1000. Sort the results by total quantity in descending order.

```sql
SELECT 
	categories.CategoryName, 
	SUM(orderdetails.Quantity) AS TotalQuantity 
FROM categories
JOIN products ON categories.CategoryID = products.CategoryID
JOIN orderdetails ON products.ProductID = orderdetails.ProductID
GROUP BY categories.CategoryID, categories.CategoryName
HAVING SUM(orderdetails.Quantity) > 1000
ORDER BY SUM(orderdetails.Quantity) DESC;
```

*This last one is more challenging than what may be asked on the final but good for additional practice.*

Write a query to show the top 5 customers by total order value. Display the customer name and their total order value. Only include customers who have placed orders totaling more than $10,000. Order the results by total order value in descending order.

```sql
SELECT 
	customers.CustomerName, 
	SUM(orderdetails.Quantity * products.Price) AS TotalOrderValue
FROM customers
JOIN orders ON customers.CustomerID = orders.CustomerID
JOIN orderdetails ON orders.OrderID = orderdetails.OrderID
JOIN products ON orderdetails.ProductID = products.ProductID
GROUP BY customers.CustomerID, customers.CustomerName
HAVING SUM(orderdetails.Quantity * products.Price) > 10000
ORDER BY SUM(orderdetails.Quantity * products.Price) DESC
LIMIT 5;
```

### See Questions: [[SQL Analytics Final - Practice Questions]]