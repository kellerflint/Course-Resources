# Entity Relationship Diagrams - Basic Structure

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=e3fcaaa2-10b5-48b3-8e8e-b1160003d8d1&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

Entity Relationship Diagrams come in various formats, but they share common elements that help us understand the architecture of a database. As we progress through this course, we will explore different ways to represent ERDs. For now, let's focus on a simple example using an HR database.

### HR Entity Relationship Diagram
<img src="https://raw.githubusercontent.com/kellerflint/Class-Intro-SQL/hugo/content/Images/hr_db_erd.png">

*Source:* https://www.sqltutorial.org/sql-sample-database/

The data here should look familiar, it's the diagram we used for the HR database in the Querying and Analysis assignment.

## Table Structure

The following properties are universal for all ERDs:
- **Tables as Boxes**: Each table in the database is represented as a box.
- **Rows and Columns**: Inside each box, the rows represent the columns of the table. When diagraming, we don't care about what specific rows of data (e.g. the actual information for each employees). Instead we care about the structure of the tables themselves and how they relate to each other.
- **Primary Key Notation**: In this ERD, the primary key for each table is indicated with an asterisk (`*`). Not every diagram uses an `*`, but they will always denote the primary key in some way.

Take the `countries` table for example. It is represented as a box in the HR Entity Relationship Diagram.
- **Columns**: Inside the box, you will find `country_id`, `country_name`, and `region_id`. While they are represented as rows in the diagram, these are actually the columns of the table in the database.
- **Primary Key**: The `country_id` is the primary key, as denoted by the `*` before it.

# Practice Questions 

1. According to the HR Entity Relationship Diagram, what will the columns be for the `countries` table?
2. Which column is the primary key for the `countries` table? How is the primary key shown in this diagram?
# Lessons
- [[SQL - Entity Relationship Diagrams - Introduction]]
- Entity Relationship Diagrams - Basic Structure
- **Next**: [[SQL - Entity Relationship Diagrams - Representing Relationships]]
- [[SQL - Entity Relationship Diagrams - Data Types and Nullability]]
- [[SQL - Entity Relationship Diagrams - Querying]]
- [[SQL - Entity Relationship Diagrams - Creating Tables]]
- [[SQL - Entity Relationship Diagrams - Practice Assignment]]