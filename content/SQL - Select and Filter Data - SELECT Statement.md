# Select and Filter Data - SELECT Statement

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=aa477a38-2f05-4bf1-9aaf-b0f201779f3c&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## Database Basics Refresher

Databases exist to help us store and manage large amounts of information in an organized way. In SQL this data is organized into tables consisting of rows and columns. Each table in a database represents a different entity, such as customers, products, or orders. The rows in the table represent individual records, and the columns represent the attributes of these entities.
##### Example Table: Customers
| CustomerID | FirstName | LastName | Email               |
|------------|-----------|----------|---------------------|
| 1          | John      | Doe      | johndoe@email.com   |
| 2          | Jane      | Smith    | janesmith@email.com |
| 3          | Alex      | Johnson  | alexj@email.com     |

## SELECT Statements

The `SELECT` statement is used to retrieve data from a database. It allows you to specify exactly which data you want to fetch from a table.

##### Basic SELECT Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

##### Selecting Specific Columns

To retrieve specific columns from a table, list the column names separated by commas. For example the query:

```sql
SELECT FirstName, LastName
FROM Customers;
```
##### Expected Output:
| FirstName | LastName |
| ---- | ---- |
| John | Doe |
| Jane | Smith |
| Alex | Johnson |
##### Selecting All Columns

To select all columns from a table, use the asterisk `*` symbol:

```sql
SELECT *
FROM Customers;
```

This query will result in the entire Customers table being displayed.

# Practice Questions

1. Select only the contact's name and age columns from the Customer table.

Back: [[SQL - Select and Filter Data - Running Scripts]] | Next: [[SQL - Select and Filter Data - WHERE Clause and Comparison Operators]]