# M8 Database Design

## Intro


<iframe src="https://share.descript.com/embed/PNTeC55FGFW" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Database Design Example

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=f7aec8fd-4eb1-4e02-a23f-b12401592fb7&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

*Note: I'm using a different diagraming tool in this video but for your assignment use drawSQL (https://drawsql.app) like in previous weeks.*

## Database Design Assignment

For this assignment, you’ll be going through the entire process of designing, creating and querying a database for a local property management company. This company manages rental properties for landlords in the greater Seattle area for a percentage of the rental income. In order to handle these properties effectively the company needs to organize and track information about their properties and tenants in a database.

**Part 1 (10 pts): Create an Entity Relationship Diagram**. Create an entity relationship diagram that represents the following:

1. Owners have names, phone numbers and a date that they joined the management service.
2. An owner can have multiple properties managed by the company and a property can have one or more owners.
3. Properties have a street address and an estimated market value.
4. Properties have one or more units and a unit can only belong to one property. 
5. Each unit has a unit number and a monthly cost. 
6. A unit can have many tenants, but a tenant can only be in one unit.
7. Tenants have a first name, last name and email.
8. A payment has a date and an amount paid. It also must track the user who made the payment and the unit that the payment was made on.
9. Tenants can make maintenance requests on units. A maintenance request has a description, a severity (1-10) and a completion status (done or not done). It also must track the tenant who made the request and the unit the request was made on.

**Part 2 (10 pts): Create and populate tables**. Write CREATE statements for each table in your diagram. Then insert at least 2 rows of data into every table (although you may want to add more to some of the joining tables). Be sure that the relationships you establish between your tables match the design outlined in your diagram, I'm looking for consistency between your code and your ERD.

After your `CREATE` and `INSERT` statements, write a `SELECT * FROM TableName` for each table in your database. Like so:
```sql
-- CREATE statements...

-- INSERT statements...

SELECT * FROM Tenants;
SELECT * FROM Units;
SELECT * FROM Owners;
-- and so on for each table ...
```

# Submission Instructions

For part 1 of this assignment, take a screenshot of your completed entity relationship diagram(s) from drawSQL.

For part 2 of this assignment, please put your `CREATE`, `INSERT` and `SELECT` SQL queries into a single SQL file.

Upload the .sql file and ER diagram image to the assignment on Canvas.
