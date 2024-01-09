<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=1304790b-0894-4c02-90b6-b0f2017793fc&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>
# ORDER BY

The `ORDER BY` clause is used to sort the result set of a query by one or more columns. It can sort the data in ascending or descending order. By default, it sorts in ascending order. 

`ORDER BY` must come after the WHERE clause. This makes sense if we think about it, we do not want to sort the rows until we've already filtered out the ones we don't want.

Using the `Employees` table from the previous example:

|EmployeeID|Name|Age|Department|
|---|---|---|---|
|1|John Doe|28|Marketing|
|2|Jane Doe|32|HR|
|3|Alex Ray|45|IT|
|4|Sara Ali|30|Finance|
|5|Mia Chen|26|Marketing|

We can sort the results by columns such as age with:

```sql
SELECT * FROM Employees
ORDER BY Age;
```
##### Expected Output
| EmployeeID | Name | Age | Department |
| ---- | ---- | ---- | ---- |
| 5 | Mia Chen | 26 | Marketing |
| 1 | John Doe | 28 | Marketing |
| 4 | Sara Ali | 30 | Finance |
| 2 | Jane Doe | 32 | HR |
| 3 | Alex Ray | 45 | IT |

If we instead wrote:

```sql
SELECT * FROM Employees
ORDER BY Age DESC;
```

We would get the same list but sorted from the highest to lowest age.

It is also possible to `ORDER BY` multiple columns:

```sql
SELECT * FROM Employees
ORDER BY Department, Age;
```
##### Expected Output:
| EmployeeID | Name | Age | Department |
| ---- | ---- | ---- | ---- |
| 4 | Sara Ali | 30 | Finance |
| 2 | Jane Doe | 32 | HR |
| 3 | Alex Ray | 45 | IT |
| 5 | Mia Chen | 26 | Marketing |
| 1 | John Doe | 28 | Marketing |

In this ordered list, employees are sorted by their departments ('Finance', 'HR', 'IT', and 'Marketing'), and within each department, they are sorted by their age from youngest to oldest.

# Practice Questions

7. Write a query to select all customers and order them alphabetically by the customer name.

8. Write a query to select all customers and order them by their Ids from highest to lowest.

Back: [[Select and Filter Data - Logical Operators]] | Next: [[Select and Filter Data - SQL Comments]]