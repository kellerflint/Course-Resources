### Back: [[SQL Analytics M7 - Many-to-Many Relationships and Entity Relationship Diagrams]]
# Table Aliasing

## What is Table Aliasing?

Table aliasing involves giving a table in your SQL query a temporary name. This temporary name (aka alias) is often an abbreviation of the full table name. This is particularly useful in queries involving multiple tables because it simplifies the query syntax and makes it easier to read and write.

### Example Using Authors and Books

Let's look at the Authors and Books tables to see how table aliasing can be applied.
### Authors Table
|AuthorID|AuthorName|
|---|---|
|1|J.K. Rowling|
|2|George Orwell|
|3|Leo Tolstoy|
### Books Table
|BookID|Title|AuthorID|
|---|---|---|
|101|Harry Potter|1|
|102|1984|2|
|103|Animal Farm|2|
|104|War and Peace|3|
|105|Anna Karenina|3|

Here's how we might perform a join to get the Titles and Authors using aliasing:

```sql
SELECT b.Title, a.AuthorName FROM Books b
JOIN Authors a ON b.AuthorID = a.AuthorID;
```
### Explanation:

1. **`Books b`**: Here, `Books` is aliased as `b`. This means that in the rest of the query, we can refer to the `Books` table as `b`.
2. **`Authors a`**: Similarly, `Authors` is aliased as `a`. Any reference to the `Authors` table can now be made using `a`.
3. **`b.Title, a.AuthorName`**: Instead of writing `Books.Title` and `Authors.AuthorName`, we use the aliases, making the query more concise.
4. **`b.AuthorID = a.AuthorID`**: The JOIN condition uses the aliases as a stand in for the full table names as well.

### Back: [[SQL Analytics M7 - Many-to-Many Relationships and Entity Relationship Diagrams]]