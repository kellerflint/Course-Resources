# Representing Relationships

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=b9a748d1-1060-4e42-85a0-b1160003d89b&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

Entity Relationship Diagrams (ERDs) not only show us the entities and their attributes but also how these entities interact with each other. The lines connecting the tables represent these relationships and are necessary to understand the database's structure. Let's break down how to read these relationships using the HR database ERD from our previous lessons.

### HR Entity Relationship Diagram
<img src="https://raw.githubusercontent.com/kellerflint/Class-Intro-SQL/hugo/content/SQL-Files/Images/hr_db_erd.png">

*Source:* https://www.sqltutorial.org/sql-sample-database/
## Interpreting Relationships

The lines between the tables indicate how the entities relate to each other. You will notice different endings on these lines, such as a single straight line or a forked line. These symbols tell us about the type and direction of the relationship.
### One-to-Many Relationship

Consider the relationship between the `employees` and `jobs` tables in the HR Entity Relationship Diagram:
- **Single Line**: This represents the "one" side of the relationship.
- **Forked Line**: This symbolizes the "many" side of the relationship.

This is known as "Crow's Foot Notation" and is widely used in database diagraming.

When we read the diagram:
- **From Jobs to Employees**: Each job can have many employees. This is because the line ends with a forked symbol at the `employees` table.
- **From Employees to Jobs**: Each employee has only one job, indicated by the single line ending at the `jobs` table.

This visualization helps us understand that each employee is associated with one job and each job title can be held by multiple employees.

### Employees-Dependents Example

Now, let's look at the relationship between `employees` and `dependents`. Based on the HR Entity Relationship Diagram, what is the relationship between these two table? Try to find out for yourself before continuing.

To understand the relationship, do the following:
1. Look at the `employees` table. The line connecting it to `dependents` ends with a pronged line at the `dependents` table. This indicates that an employee can have many dependents.
2. Now, examine the `dependents` table. The line connecting it to `employees` ends with a single straight line. This indicates that a dependent can only have one employee.

This relationships is also suggested by the structure of the table itself. We can see that `dependents` has a column for `employee_id`, suggesting that each dependent can be linked to a single employee.

# Practice Questions

3. What is the relationship between `regions` and `countries`? What steps did you take to determine this from the diagram?
4. What is the relationship between `departments` and `employees`? What steps did you take to determine this from the diagram?
# Lessons
- [[SQL - W5 Introduction to Entity Relationship Diagrams]]
- [[SQL - W5 Entity Relationship Diagram Structure]]
- SQL W5 Representing Relationships
- **Next**: [[SQL - W5 Data Types and Nullability]]
- [[SQL - W5 Querying from ERDs]]
- [[SQL - W5 Creating Tables in ERDs]]
- [[SQL - W5 Entity Relationship Diagrams Practice Assignment]]

