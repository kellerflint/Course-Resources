# Introduction to One to Many Relationships

Video Embedding

## What is a One to Many Relationship?

In relational databases, a One to Many relationship is the most fundamental type of relationship. This relationship exists when a record in one table can be associated with multiple records in another table.

For example, consider a database of a bookstore. Here, we have two tables: `Authors` and `Books`. An author can write multiple books, but each book is written by only one author. This is a classic One to Many relationship.

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

It's important to understand exactly why this is a one to many relationship. Why can we can have many books per author but only one author per book? The structure of the table tells us this is how the relationship must work. Here's how:

- **Single Author, Multiple Books**: Each author in the `Authors` table can write multiple books. An author's ID can appear in many rows in the `Books` table. For instance, if "George Orwell" writes two books, his ID appears next to each of those books in the `Books` table. Therefore an author can have many books.

- **Single Book, Single Author**: Conversely, each book in the `Books` table is associated with only one author. For each row in the `Books` table, there is only a place for one AuthorID. For example, "1984" can only be associated with one author, George Orwell.


Back: [[Table JOINs - DROP Tables and Run Script]] | Next: [[Table JOINs - JOIN Tables with One to Many Relationships]]