# Table JOINs - Many to Many Relationships

Embed Video

## Introduction to Many to Many Relationships

A many to many relationship in databases occurs when multiple records in one table are associated with multiple records in another table. This kind of relationship often requires a third table, known as a junction, associative or joining table. This table is used to break a many to many relationship down into two one to many relationships.

Let's explore this concept with a new set of tables for books and authors that represent a many to many relationship.

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
In the `BooksAuthors` table, both `BookID` and `AuthorID` are used together to create unique combinations, allowing for the representation of multiple authors per book and vice versa.

### Understanding the Many to Many Relationship

1. **First One to Many**: Each record in the `Authors` table can be linked to multiple records in the `BooksAuthors` table. For example, AuthorID 2 is linked to BookID 102 and 103. This is a one to many relationship from Authors to BooksAuthors.

2. **Second One to Many**: Similarly, each record in the `Books` table can be linked to multiple records in the `BooksAuthors` table. For instance, BookID 103 is linked to AuthorID 1 and 2. This is another one to many relationship, but from Books to BooksAuthors.

3. **The Many to Many**: These two one to many relationships combine to form a many to many relationship. An author can write multiple books, and a book can be written by multiple authors. The `BooksAuthors` table serves as a bridge, linking each book to one or more authors and each author to one or more books.



Back: [[Table JOINs - JOIN Tables with One to Many Relationships]] | Next: [[Table JOINs - JOIN Tables with Many to Many Relationships]]