# Database Design Assignment

For this assignment, you’ll be going through the entire process of designing, creating and querying a database for a local property management company. This company manages rental properties for landlords in the greater Seattle area for a percentage of the rental income. In order to handle these properties effectively the company needs to organize and track information about their properties and tenants in a database.

**Part 1 (40 pts): Create an Entity Relationship Diagram**. Create an entity relationship diagram that represents the following:

1. Owners have names, phone numbers and a date that they joined the management service.
2. An owner can have multiple properties managed by the company and a property can have one or more owners.
3. Properties have a street address and an estimated market value.
4. Properties have one or more units and a unit can only belong to one property. 
5. Each unit has a unit number and a monthly cost. 
6. A unit can have many tenants, but a tenant can only be in one unit.
7. Tenants have a first name, last name and email.
8. A payment has a date and an amount paid. It also must track the user who made the payment and the unit that the payment was made on.
9. Tenants can make maintenance requests on units. A maintenance request has a description, a severity (1-10) and a completion status (done or not done). It also must track the tenant who made the request and the unit the request was made on.

**Part 2 (20 pts): Create and populate tables**. Write CREATE statements for each table in your diagram. Then insert at least 2 rows of data into every table (although you may want to add more to some of the joining tables). Be sure that the relationships you establish between your tables match the design outlined in your diagram, I'm looking for consistency between your code and your ERD.

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

For part 1 of this assignment (and for the [[SQL - Database Design Assignment - Challenge (5 pts Extra Credit)|challenge]], should you choose to attempt it), take a screenshot of your completed entity relationship diagram(s) from drawSQL.

For part 2 of this assignment, please put your `CREATE`, `INSERT` and `SELECT` SQL queries into a single SQL file.

Upload the .sql file and each ERD image to the assignment submission on Canvas.
# Lessons
- [[SQL - ERD & DB Design Assignment - Introduction]]
- [[SQL - Database Design Assignment - Database Design Example]]
- Database Design Assignment
- Next: [[SQL - Database Design Assignment - Challenge (5 pts Extra Credit)]]