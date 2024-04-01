# Select and Filter Data - WHERE Clause and Comparison Operators

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=10ae282e-3ce2-4f40-81b7-b0f201779467&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

The WHERE clause in SQL is used to filter records from a table, returning only those that meet a specific condition. 
### Basics of the WHERE Clause 

The WHERE clause follows the syntax: 

```sql
SELECT column1, column2, ... FROM table_name 
WHERE condition;
```

### Comparison Operators

There are many different types of operators that can be used in our condition to filter what rows we get back based on the data they contain.

The first type are the comparison operators. These are used to compare values in a column with other values or expressions. These include:
- `=` : Equal to
- `<` `>` or `!` `=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>` `=` : Greater than or equal to
- `<` `=` : Less than or equal to

For example, assume we have a table `Employees` with the following data:

|EmployeeID|Name|Age|Department|
|---|---|---|---|
|1|John Doe|28|Marketing|
|2|Jane Doe|32|HR|
|3|Alex Ray|45|IT|
|4|Sara Ali|30|Finance|

To get details of employees from the 'Marketing' department we could write:

```sql
SELECT * FROM Employees
WHERE Department = 'Marketing';
```
##### Expected Output:
|EmployeeID|Name|Age|Department|
|---|---|---|---|
|1|John Doe|28|Marketing|

If we wanted to find all employees who are not in the 'HR' department we could write:

```sql
SELECT * FROM Employees
WHERE Department <> 'HR';
```
##### Expected Output:
|EmployeeID|Name|Age|Department|
|---|---|---|---|
|1|John Doe|28|Marketing|
|3|Alex Ray|45|IT|
|4|Sara Ali|30|Finance|

If we wanted to see information for employees over the age of 30 we could write:

```sql
SELECT * FROM Employees 
WHERE Age > 30;
```
##### Expected Output:
| EmployeeID | Name | Age | Department |
| ---- | ---- | ---- | ---- |
| 2 | Jane Doe | 32 | HR |
| 3 | Alex Ray | 45 | IT |
# Practice Questions

2. Write a query to select all customers who are from 'Germany'.

3. Write a query to select all customers whose contact age is less than or equal to 20.

Back: [[SQL - Select and Filter Data - SELECT Statement]] | Next: [[SQL - Select and Filter Data - Logical Operators]]