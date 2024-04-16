
# JOIN Tables with One-to-Many Relationships


<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=851a0a62-1d48-4d30-9bff-b0fb000eb927&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## Understanding JOINs in One-to-Many Relationships

Given our bookstore database example from the previous lesson:
### Authors Table:
| AuthorID | AuthorName |
| ---- | ---- |
| 1 | J.K. Rowling |
| 2 | George Orwell |
| 3 | Leo Tolstoy |
### Books Table:
|BookID|Title|AuthorID|
|---|---|---|
|101|Harry Potter|1|
|102|1984|2|
|103|Animal Farm|2|
|104|War and Peace|3|
|105|Anna Karenina|3|

In order to retrieve data that spans across these two tables, we use the SQL JOIN operation. Let's see how we can use the JOIN command to fetch the list of books along with their authors' names.

```sql
SELECT Books.Title, Authors.AuthorName FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID; 
```
##### Expected Output:
| Title | AuthorName |
| ---- | ---- |
| Harry Potter | J.K. Rowling |
| 1984 | George Orwell |
| Animal Farm | George Orwell |
| War and Peace | Leo Tolstoy |
| Anna Karenina | Leo Tolstoy |

This query effectively combines data from the `Books` and `Authors` tables by linking books to their respective authors by the AuthorID. The `JOIN` operation, facilitated by the `ON` clause, ensures that each book is matched with its author. The selected columns `Books.Title` and `Authors.AuthorName` are displayed in the resulting output.

To understand exactly how the SQL JOIN command works in our Authors and Books example, let's break down the query piece by piece.
#### 1. `SELECT Books.Title, Authors.AuthorName`
- **Purpose**: This part of the query specifies what data we want to retrieve. Here, we are asking for the `Title` from the `Books` table and the `AuthorName` from the `Authors` table.
- **Action**: It tells the database to look at these two columns and prepare to output data from them.
#### 2. `FROM Books`
- **Purpose**: This clause specifies the table from which to retrieve data, which in this case is the `Books` table.
- **Action**: It sets the context for the SQL query, indicating that the data will be selected from the `Books` table.
#### 3. `JOIN Authors`
- **Purpose**: Indicates that we want to combine rows from our existing table(s) (e.g., the `Books` table in this case) with rows from the `Authors` table.
- **Action**: It initiates the action to combine data from the two tables based on a related column.
#### 4. `ON Books.AuthorID = Authors.AuthorID`
- **Purpose**: This is the condition on which the JOIN will be performed. To function, the JOIN needs to know what column it should use to match records between the two tables. `ON` is used to map this relationship. In this case, we are joining the tables based on the `AuthorID` column, which is common to both tables.
- **Action**: It matches each row in the `Books` table with the corresponding row in the `Authors` table where the `AuthorID` is the same.

# Practice Questions

1. Write a query to list all orders, including the order ID, the date the order was placed, and the first and last name of the client who placed the order.

2. Write a query to display a list of all products, including their name, price, and the name and address of their supplier.



# Lessons
- [[SQL - W3 Table JOINs - Introduction]]
- [[SQL - W3 Table JOINs - DROP Tables]]
- [[SQL - Magic Store Database Overview]]
- [[SQL - W3 Table JOINs - One-to-Many Relationships]]
- SQL - W3 Table JOINs - JOIN Tables with One-to-Many Relationships
- Next: [[SQL - W3 Table JOINs - Filter and Sort with JOINs]]
- [[SQL - W3 One-to-Many JOINs - Practice Assignment]]