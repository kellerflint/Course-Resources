# Table JOINs - JOIN Tables with Many to Many Relationships

Embed Video

## Understanding JOINs in Many to Many Relationships

Given our bookstore database example from the previous lesson:
### Authors Table:
|AuthorID|AuthorName|
|---|---|
|1|Luna Bellatrix|
|2|Orion Stardust|
|3|Celeste Moon |
### Books Table:
|BookID|Title|
|---|---|
|101|Whispers of the Galaxy|
|102|Secrets of the Eclipse|
|103|Shadows in the Cosmos|
|104|Starlight Symphony|
|105|Moonlit Myth|
### BooksAuthors Joining Table:
|BookID|AuthorID|
|---|---|
|101|1|
|102|2|
|103|2|
|103|1|
|104|3|
|105|3|
To retrieve data that spans across these three tables, we use the SQL JOIN operation twice. Let's see how we can use the JOIN command to fetch the list of books along with their authors' names now that we're representing the data with a many to many relationship.
### Understanding the Many to Many Relationship

```sql
SELECT Books.Title, Authors.AuthorName FROM Books
JOIN BooksAuthors ON Books.BookID = BooksAuthors.BookID
JOIN Authors ON BooksAuthors.AuthorID = Authors.AuthorID;
```
##### Expected Output:
|Title|AuthorName|
|---|---|
|Whispers of the Galaxy|Luna Bellatrix|
|Secrets of the Eclipse|Orion Stardust|
|Shadows in the Cosmos|Orion Stardust|
|Shadows in the Cosmos|Luna Bellatrix|
|Starlight Symphony|Celeste Moon |
|Moonlit Myth|Celeste Moon |
#### 1. `SELECT Books.Title, Authors.AuthorName FROM Books`
- This command retrieves the `Title` from the `Books` table and the `AuthorName` from the `Authors` table, aiming to display book titles alongside their authors' names.
- It also sets `Books` as the primary table from which the query starts, establishing the context for the JOIN operations that follow.

#### 2. `JOIN BooksAuthors ON Books.BookID = BooksAuthors.BookID`
- The first JOIN operation. It joins the `Books` table with the `BooksAuthors` joining table, based on the `BookID`. This operation matches each book with its corresponding entries in the `BooksAuthors` table.

#### 3. `JOIN Authors ON BooksAuthors.AuthorID = Authors.AuthorID`
- The second JOIN operation. It joins the intermediate result (which includes information from `Books` and `BooksAuthors`) with the `Authors` table. The joining is based on the `AuthorID`, linking each entry in the BooksAuthors table with its respective author.


Back: [[Table JOINs - Many to Many Relationships]] | Next: [[Table JOINs - Filter and Sort with JOINs]]