
In addition to the practice problems from the lesson pages, create an entity relationship diagram for the following business scenario using [drawSQL](https://drawsql.app/). *Please check with your instructor and get permission before using any other tool.*

4. *(5pts)* Create an ERD for a chain of lemonade stands needs software to help them track their supplies and employees. Design requirements:
	- Each lemonade stand has a street address and a target revenue.
	- Lemonade stands can receive many shipments, but a shipment can only go to one lemonade stand. The database should track which shipment is sent to which stand.
	- Shipments must always have the date that they were sent. A shipment may also have the date that they were received but this value might be empty if the shipment has not reached a stand yet.
	- Each shipment can contain many different supply items (such as lemons, water, napkins, etc.) and a supply item can belong to many shipments. The database should also track how many of each supply item was sent in a shipment.
	- Each supply item has a name and a price.
	- Lemonade stands can have many employees but an employee can only work at one stand at a time. The database should also track which days of the week an employee works.
	- Each employee has a first name, a last name and an age.

***Representing this should require 5 tables. If you find yourself with either more or less, it's likely you need to rethink the design.***

# Submission Instructions

For questions #1 and #2, please put your SQL queries into a single SQL file. Use comments to label each query with its respective question number.

For questions #3 and #4, take screenshots of your completed entity relationship diagrams from drawSQL.

Upload the .sql file and each image to the assignment submission on Canvas. *You should be uploading/submitting a total of 3 files for this assignment (the .sql file and the two ERD images).*

# Lessons
- [[Creating Entity Relationship Diagrams - Introduction]]
- [[Creating Entity Relationship Diagrams - CREATE One to Many Tables]]
- [[Creating Entity Relationship Diagrams - CREATE Many to Many Tables]]
- [[Creating Entity Relationship Diagrams - Using Composite Primary Keys]]
- [[Creating Entity Relationship Diagrams - Create Entity Relationship Diagrams]]
- Creating Entity Relationship Diagrams - Practice Assignment