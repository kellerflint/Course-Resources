
# Lessons and Practice - Basic Querying 
## Estimated Time to Complete: 3 ~ 10 hours


### [[SQL Analytics M2 - Installing MySQL Workbench and MariaDB|Installing MySQL Workbench and MariaDB]] (17 min)

After successfully setting up MySQL Workbench and MariaDB, take a screenshot of your working editor with your name in an open file (see canvas assignment for example) and submit it to the "M2 Practice - Editor Screenshot" assignment in canvas.

### [[SQL Analytics M2 - MySQL Workbench Basics|MySQL Workbench Basics]] (8 min)

### [[SQL Analytics M2 - How to Complete SQL Assignments|How to Complete SQL Assignments]] (3 min)

### [[SQL Analytics - Northwind Database|Northwind Database]] (2 min)

### [[SQL Analytics M2 - SELECT Statements|SELECT Statements]] (8 min)

1. Create a query to display the first name and last name of all employees from the `employees` table.
2. Write a query to display all information in the `shippers` table.
3. The sales team needs a list of all our products with only the details most relevant to making the sale. Write a query to accomplish this. Include a comment above the query that briefly explains why you believe the columns you chose were most relevant.

### [[SQL Analytics M2 - Math on Columns|Math on Columns]] (4 min)

4. Write a query to display the product name, price, and price with a 30% discount from the `products` table.
5. Northwind is analyzing their pricing structure and needs to see how each of our products would be priced if we applied a flat $2 increase and then a 12% markdown (decrease). Write a query to accomplish this.

### [[SQL Analytics M2 - Column Aliasing|Column Aliasing]] (3 min)

6. Re-write your query for question #5 using clear column names. Include the following additional columns as well:
	- `Flat Increase Amount` with a fixed value of "12%"
	- `Markdown Amount` with a fixed value of "$2"

### [[SQL Analytics M2 - WHERE Clause|WHERE Clause]] (30 min)

7. Write a query to retrieve all products from the `products` table where the price is between 15 and 25.
8. Create a query to list all products from the `products` table that have 'chef' in their product name.
9. Write a SELECT statement to display all customers from the `customers` table that are located in either Germany, France, or Spain.
10. The marketing team is planning a promotion and needs to see relevant information on Northwind's affordable seafood and dairy products. Write a query to accomplish this.
### [[SQL Analytics M2 - ORDER BY, LIMIT, and Query Structure|ORDER BY, LIMIT, and Query Structure]] (11 min)

11. Write a query to retrieve all employee names from the `employee` table, ordered from youngest to oldest.
12. Write a query to show all customers from the `customers` table, sorted first by their country in reverse alphabetical order and the customer's name in alphabetical order.
13. Management is conducting a performance review of employees and wants to see a comprehensive breakdown of all orders. They need to see which employees handled each order *(you can use the `EmployeeID` in the `orders` table, it shows who facilitated the order)* and the corresponding order dates. They've emphasized the importance of seeing each employee's sales history chronologically, with their most recent sales appearing first. Write a query that provides this information in a format that allows management to easily review each employee's performance over time.

Submit your answers for the "M2 Practice - Basic Querying" assignment on canvas.

