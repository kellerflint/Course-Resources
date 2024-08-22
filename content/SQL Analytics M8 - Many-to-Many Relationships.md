### Back: [[SQL Analytics M8 - Many-to-Many Relationships and Entity Relationship Diagrams]]

# Many-to-Many Relationships

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=c5b32412-9c53-4db8-a649-b0fb000ed371&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## Introduction to Many-to-Many Relationships

A many-to-many relationship in databases occurs when multiple records in one table are associated with multiple records in another table. This kind of relationship often requires a third table, known as a junction, associative or joining table (depending on who you ask). For this class, I will use the term joining table. The joining table is used to break a many-to-many relationship down into two one-to-many relationships.

Let's explore this concept with a new set of tables for books and authors that represent a many-to-many relationship.

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

### Understanding the many-to-many Relationship

1. **First One-to-Many**: Each record in the `Authors` table can be linked to multiple records in the `BooksAuthors` table. For example, AuthorID 2 is linked to BookID 102 and 103. This is a one-to-many relationship from Authors to BooksAuthors.

2. **Second One-to-Many**: Similarly, each record in the `Books` table can be linked to multiple records in the `BooksAuthors` table. For instance, BookID 103 is linked to AuthorID 1 and 2. This is another one-to-many relationship, but from Books to BooksAuthors.

3. **The Many-to-Many**: These two one-to-many relationships combine to form a many-to-many relationship. An author can write multiple books, and a book can be written by multiple authors. The `BooksAuthors` table serves as a bridge, linking each book to one or more authors and each author to one or more books.

### Back: [[SQL Analytics M8 - Many-to-Many Relationships and Entity Relationship Diagrams]]