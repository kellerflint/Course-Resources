# Introduction to One-to-Many Relationships


<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=b1546239-e7ce-4a5d-9068-b0fb000eabca&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=b8901214-6404-4e52-9e50-b0fb000ee542&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## What is a One-to-Many Relationship?

In relational databases, a one-to-many relationship is the most fundamental type of relationship. This relationship exists when a record in one table can be associated with multiple records in another table.

For example, consider a database of a bookstore. Here, we have two tables: `Authors` and `Books`. An author can write multiple books, but each book is written by only one author. This is a classic one-to-many relationship.

### Authors Table:
|AuthorID|AuthorName|
|---|---|
|1|J.K. Rowling|
|2|George Orwell|
|3|Leo Tolstoy|
### Books Table:
|BookID|Title|AuthorID|
|---|---|---|
|101|Harry Potter|1|
|102|1984|2|
|103|Animal Farm|2|
|104|War and Peace|3|
|105|Anna Karenina|3|
### Understanding the Direction of the Relationship

It's important to understand exactly why this is a one-to-many relationship. Why can we can have many books per author but only one author per book? The structure of the table tells us this is how the relationship must work. Here's how:

- **Single Author, Multiple Books**: Each author in the `Authors` table can write multiple books. An author's ID can appear in many rows in the `Books` table. For instance, if "George Orwell" writes two books, his ID appears next to each of those books in the `Books` table. Therefore an author can have many books.

- **Single Book, Single Author**: Conversely, each book in the `Books` table is associated with only one author. For each row in the `Books` table, there is only a place for one AuthorID. For example, "1984" can only be associated with one author, George Orwell.

### Terminology: Primary Keys and Foreign Keys

#### Primary Key
- A primary key is a unique identifier assigned to each record in a table. It ensures that each record can be distinctly identified, meaning no two records can have the same primary key value. This key is essential for maintaining the uniqueness and integrity of the data within the table.
- In the `Authors` table, `AuthorID` serves as the primary key. Each author has a unique `AuthorID` that distinguishes it from others.
- In the `Books` table, the `BookID` serves as the primary key. Each book has a unique `BookID` that distinguishes it from others.
#### Foreign Key
- A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table. Put simply, a foreign key is a reference to the primary key of another table. It establishes a link between tables, showing how records in one table relate to records in another.
- In the `Books` table, `AuthorID` serves as a foreign key. It references the `AuthorID` from the `Authors` table.
- This foreign key creates the link between each book and its author, establishing the one-to-many relationship.

Back: [[Table JOINs - Magic Store Database]] | Next: [[Table JOINs - JOIN Tables with One-to-Many Relationships]]