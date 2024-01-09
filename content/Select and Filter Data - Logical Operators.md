<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=1d1412b2-7cca-43cf-af61-b0f20177942c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>
# Logical Operators

Logical operators are essential in SQL for combining multiple conditions in the WHERE clause and adding flexibility to your queries. With the right operators, you can filter for rows based on any combination of attributes and conditions.

Some of the most commonly used logical operators used in SQL are:
- `AND`: Returns true if both conditions are true.
- `OR`: Returns true if at least one of the conditions is true.
- `NOT`: Negates the condition, returning true if the condition is false.
- `BETWEEN`: Returns true if a value lies within a specified range.
- `IN`: Returns true if a value matches any value in a list.
- `LIKE`: Returns true if a value matches a specified pattern.

Expanding on the `Employees` table from our previous examples:

| EmployeeID | Name | Age | Department |
| ---- | ---- | ---- | ---- |
| 1 | John Doe | 28 | Marketing |
| 2 | Jane Doe | 32 | HR |
| 3 | Alex Ray | 45 | IT |
| 4 | Sara Ali | 30 | Finance |
| 5 | Mia Chen | 26 | Marketing |

To find employees over 30 years old in the IT department we could write:

```sql
SELECT * FROM Employees
WHERE Age > 30 AND Department = 'IT';
```
##### Expected Output:
|EmployeeID|Name|Age|Department|
|---|---|---|---|
|3|Alex Ray|45|IT|

As 'Alex Ray' is the only employee who matches both criteria.

Alternatively if we wanted to find employees who are either in the 'HR' departments OR over 30 years old we could write:

```sql
SELECT * FROM Employees
WHERE Age > 30 OR Department = 'IT';
```
##### Expected Output:
|EmployeeID|Name|Age|Department|
|---|---|---|---|
|2|Jane Doe|32|HR|
|3|Alex Ray|45|IT|

Because while 'Jane Doe' is not in the 'IT' department, she is older than 30 and only one condition needs to be met.

To find all employees who are between the ages of 20 and 30 we could write:

```sql
SELECT * FROM Employees
WHERE Age BETWEEN 20 AND 30;
```
##### Expected Output: 
| EmployeeID | Name | Age | Department |
| ---- | ---- | ---- | ---- |
| 1 | John Doe | 28 | Marketing |
| 4 | Sara Ali | 30 | Finance |
| 5 | Mia Chen | 26 | Marketing |

This time the expected output includes Sara Ali because `BETWEEN` is inclusive meaning we'll also get employees who are equal to the thresholds.

To find employees who work in either 'Marketing', 'Finance', or 'IT' departments we could write:

```sql
SELECT * FROM Employees
WHERE Department IN ('Marketing', 'Finance', 'IT');
```
##### Expected Output:
|EmployeeID|Name|Age|Department|
|---|---|---|---|
|1|John Doe|28|Marketing|
|3|Alex Ray|45|IT|
|4|Sara Ali|30|Finance|
|5|Mia Chen|26|Marketing|

The `LIKE` command is slightly more complicated. It can be used to find values that match a particular pattern a pattern. For example if we wanted to find employees whose names started the letter 'J' we could write:

```sql
SELECT * FROM Employees
WHERE Name LIKE 'J%';
```
##### Expected Output:
| EmployeeID | Name | Age | Department |
| ---- | ---- | ---- | ---- |
| 1 | John Doe | 28 | Marketing |
| 2 | Jane Doe | 32 | HR |

The `%` symbol after the 'J' is a wildcard that represents zero, one, or multiple characters. So this pattern is looking for Names that start with a 'J' followed by any number of any characters (or none at all).

`Like` can allow you to match any pattern with the right wildcards. See <a href="https://www.w3schools.com/sql/sql_wildcards.asp" target="_blank">SQL Wildcard Characters (w3schools.com)</a> for more information on Wildcards.

# Practice Questions

4. Write a query to select all customers who are from 'Berlin', 'London', 'Vancouver', 'São Paulo' or 'Madrid'.

5. Write a query to select all customers who are not from 'Germany' and whose contact ages are under 60 years old.

6. Write a query to select all customers whose contact ages are between 25 and 35 and whose contact name starts with an 'Al'.

Back: [[Select and Filter Data - WHERE Clause and Comparison Operators]] | Next: [[Select and Filter Data - ORDER BY]]
