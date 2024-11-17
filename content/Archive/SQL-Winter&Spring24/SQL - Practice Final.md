
The format and topics covered in this practice final closely mirror what you will encounter on the final exam. To ensure you're fully prepared, these practice questions are designed to be slightly more challenging versions of the types of questions you'll be asked in the final exam.

# SDEV 201 Practice Exam

### Part 1: Querying

Given the following tables, write SQL queries to retrieve the requested information.
##### Employee

| EmployeeID | FirstName | LastName | DepartmentID | Salary |
| ---------- | --------- | -------- | ------------ | ------ |
| 1          | Ahmed     | Khan     | 1            | 65,000 |
| 2          | Samantha  | Davis    | 2            | 80,000 |
| 3          | Ava       | Williams | 3            | 72,000 |
| 4          | Diego     | Gonzalez | 2            | 90,000 |
| 5          | Sam       | Johnson  | 4            | 68,000 |
| 6          | Samir     | Patel    | 3            | 75,000 |

##### Project

| ProjectID | Name               | DepartmentID | Budget |
| --------- | ------------------ | ------------ | ------ |
| 1         | Website Redesign   | 2            | 50,000 |
| 2         | Recruitment Drive  | 1            | 25,000 |
| 3         | Financial Analysis | 3            | 40,000 |
| 4         | Marketing Campaign | 4            | 60,000 |
| 5         | Server Upgrade     | 2            | 35,000 |

##### Department

| DepartmentID | Name      |
| ------------ | --------- |
| 1            | HR        |
| 2            | IT        |
| 3            | Finance   |
| 4            | Marketing |

##### ProjectAssignment

| AssignmentID | EmployeeID | ProjectID | HoursWorked |
| ------------ | ---------- | --------- | ----------- |
| 1            | 1          | 2         | 40          |
| 2            | 2          | 1         | 35          |
| 3            | 2          | 5         | 25          |
| 4            | 3          | 3         | 45          |
| 5            | 4          | 1         | 50          |
| 6            | 4          | 5         | 30          |
| 7            | 5          | 4         | 55          |
| 8            | 6          | 3         | 40          |

1. Write a query to retrieve the ID, first name, and last name of all employees.

<details>
<summary>Show Answer</summary>
SELECT EmployeeID, FirstName, LastName FROM Employee;
</details>

2. Write a query to retrieve the project name and budget for all projects in the 'IT' department.

<details>
<summary>Show Answer</summary>
<p>SELECT Project.Name, Budget FROM Project</p>
<p>JOIN Department ON Project.DepartmentID = Department.DepartmentID</p>
<p>WHERE Department.Name = 'IT';</p>
</details>

3. What data would be returned by the following query? Fill in the table with the correct information. You may leave the extra rows blank.

```sql
SELECT FirstName, Salary, Name AS "DepartmentName" FROM Employee
JOIN Department ON Employee.DepartmentID = Department.DepartmentID
WHERE FirstName LIKE '%Sam%' AND Salary > 70000
ORDER BY Salary DESC;
```

| FirstName | Salary | DepartmentName |
| --------- | ------ | -------------- |
|           |        |                |
|           |        |                |
|           |        |                |
|           |        |                |
|           |        |                |

<details>
<summary>Show Answer</summary>
<p>FirstName | Salary | DepartmentName</p>
<p>Samantha | 80,000 | IT</p>
<p>Samir | 75,000 | Finance</p>
</details>

4. Write a query to retrieve all project assignments. Include the name of the project and the first and last name of the employee. Order the results alphabetically by the project name.

<details>
<summary>Show Answer</summary>
<p>SELECT Name AS ProjectName, FirstName, LastName FROM ProjectAssignment</p>
<p>JOIN Project ON ProjectAssignment.ProjectID = Project.ProjectID</p>
<p>JOIN Employee ON ProjectAssignment.EmployeeID = Employee.EmployeeID</p>
<p>ORDER BY Project.Name ASC;</p>
</details>

5. Write a query to retrieve the employee ID, employee last name and the total hours worked on all projects for each employee. Order the results by the total hours worked (highest to lowest).

<details>
<summary>Show Answer</summary>
<p>SELECT Employee.EmployeeID, LastName, SUM(HoursWorked) AS TotalHours FROM ProjectAssignment</p>
<p>JOIN Employee ON ProjectAssignment.EmployeeID = Employee.EmployeeID</p>
<p>JOIN Project ON ProjectAssignment.ProjectID = Project.ProjectID</p>
<p>GROUP BY Employee.EmployeeID</p>
<p>ORDER BY TotalHours DESC;</p>
</details>

### Part 2: Entity Relationship Diagrams and Creating Tables

6. Draw the Entity Relationship Diagram for the Employee, Project, Department, and ProjectAssignment tables given above. Make sure to include all columns, the data type you think each column should have and any relationships between the tables. Represent relationships between tables with Crow's Foot Notation.

<details>
<summary>Show Answer</summary>
<img src="https://raw.githubusercontent.com/kellerflint/Class-Intro-SQL/hugo/content/SQL-Files/Images/PracticeExamDiagramKey.png">
</details>

7. Write the CREATE statement for only the Project table. Make sure to include all columns, the data type of each column, and any primary or foreign key constraints.

<details>
<summary>Show Answer</summary>
<p>CREATE TABLE Project (</p>
<p>    &emsp;ProjectID INT PRIMARY KEY,</p>
<p>    &emsp;Name VARCHAR(100) NOT NULL,</p>
<p>    &emsp;DepartmentID INT NULL,</p>
<p>    &emsp;Budget INT NOT NULL,</p>
<p>    &emsp;FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)</p>
<p>);</p>
<p>Note: Assign columns to be NULL or NOT NULL according to your best judgement.<p>
</details>

8. Based on the Northwind Traders diagram below, write a query to retrieve all orders. Include the order's ID, the order's date, the name of the customer who placed the order, and the name of shipper delivering the order.

<img src="https://raw.githubusercontent.com/kellerflint/Class-Intro-SQL/hugo/content/SQL-Files/NorthwindERD.png">

<details>
<summary>Show Answer</summary>
<p>SELECT OrderID, OrderDate, CustomerName, ShipperName FROM Orders</p>
<p>JOIN Customers ON Orders.CustomerID = Customers.CustomerID</p>
<p>JOIN Shippers ON Orders.ShipperID = Shipper.ShipperID</p>
</details>

### Part 3: SQL for Data Analytics

*This section is worth only a few points on the final exam. Focus your efforts on parts 1 and 2 before tackling the data analytics section.*

Northwind Traders wants to identify the most promising locations for expansion based on current customer purchasing patterns.

Using the Northwind Traders diagram above, construct a query that gives meaningful insights into customer purchasing behavior across different locations to inform the company's regional expansion decisions. Include at least two calculated or aggregated metrics in your query. Make your the query output is well organized and formatted so it is easy for business stakeholders to understand. Provide a brief explanation of how the query you wrote could inform the expansion strategy.

---

### Part 3 Answer:

*I have no specific answer I have in mind for data analytics questions. I'm looking for functional queries that meet the requirements given in the question and help give meaningful insight into the data. I'm also looking for good reasoning about the kind of conclusions your query can provide and what considerations or assumptions went in to designing your query. Below is one possible solution.*

```sql
SELECT c.Country, COUNT(*) AS TotalOrders, SUM(od.Quantity * p.Price) AS TotalRevenue FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY c.Country
ORDER BY TotalRevenue DESC;
```

This query provides an overview of the total orders and revenue generated from each country that Northwind Traders can use to identify their top performing locations. Looking at both total orders and revenue by region is important because it provides a more comprehensive view of market performance and potential.

Total orders can indicate the size of size customer base in each region, while revenue reflects the monetary value of those orders. A region with many orders but low revenue may have a large but low-spending customer base, while a region with few orders but high revenue may have a smaller but high-value customer base.