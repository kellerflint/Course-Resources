# Lesson
## Database Basics

Databases exist to help us store and manage large amounts of information in an organized way. In SQL this data is organized into tables consisting of rows and columns. Each table in a database represents a different entity, such as customers, products, or orders. The rows in the table represent individual records, and the columns represent the attributes of these entities.
##### Example Table: Customers
| CustomerID | FirstName | LastName | Email               |
|------------|-----------|----------|---------------------|
| 1          | John      | Doe      | johndoe@email.com   |
| 2          | Jane      | Smith    | janesmith@email.com |
| 3          | Alex      | Johnson  | alexj@email.com     |

## Introduction to the SELECT Statement
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

Will result in the following output:

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

# Practice



Back: [[Select and Filter Data - Running Database Scripts]] | Next: 