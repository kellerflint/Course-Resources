# Many-to-Many Relationships and Entity Relationship Diagrams

<iframe src="https://share.descript.com/embed/4atZ5UxCvkD" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### [[SQL Analytics M8 - Many-to-Many Relationships|Many-to-Many Relationships]] (~10 min)

### [[SQL Analytics M8 - Table Aliasing|Table Aliasing]] (~3 min)

## Creating Entity Relationship Diagrams

### One-to-Many ER Diagrams 

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=d43d459b-9a76-48bf-bb0d-b11c015d3d30&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

### Many-to-Many ER Diagrams

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=b488333a-81d2-4859-9854-b11c015d3061&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

### [[SQL Analytics M8 - Composite Primary Keys]] (~6 min)


# Creating Entity Relationship Diagrams

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=99ed404e-6872-496d-95da-b11c015d3030&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

### Link to the diagraming tool -> https://drawsql.app


## Practice Questions

Create an entity relationship diagram for the following questions using [drawSQL](https://drawsql.app/). *Please check with your instructor and get permission before using any other tool.*

1. *(4pts)* Create an entity relationship diagram to represent the tables created in the script below.

<img src="https://raw.githubusercontent.com/kellerflint/Class-Intro-SQL/hugo/content/SQL-Files/Images/book_store_script_img.png">

2. (3pts) Create an entity relationship diagram to represent the tables below.

##### Guests

| ID  | FirstName | LastName | Phone          |
| --- | --------- | -------- | -------------- |
| 1   | Nathaniel | Mandrake | (111) 222 3333 |
| 2   | David     | Martinez | (333) 444 5555 |
| 3   | Valentine | Wiggin   | (666) 777 8888 |

##### Reservations

| ID  | GuestID | RestaurantID | ReservationDateTime |
| --- | ------- | ------------ | ------------------- |
| 1   | 3       | 2            | 2024-01-02 19:00:00 |
| 2   | 1       | 1            | 2024-01-03 9:30:00  |
| 3   | 2       | 1            | 2024-01-03 10:00:00 |
| 4   | 3       | 2            | 2024-01-04 17:30:00 |

##### Restaurants

| ID | Name                   |
|----|------------------------|
| 1  | Bob's Gourmet Macaroni |
| 2  | Cheese Louise Dinner   |

3. *(5pts)* Create an entity relationship diagram for a chain of lemonade stands. They need a database to help them track information about their stands, shipments and employees. Requirements:
	- Each lemonade stand has a street address and a target revenue.
	- Lemonade stands can receive many shipments, but a shipment can only go to one lemonade stand. The database should track which shipment is sent to which stand.
	- Shipments must always have the date that they were sent. A shipment may also have the date that they were received but this value might be empty if a shipment has not reached the stand yet.
	- Each shipment can contain many different supply items (such as lemons, water, napkins, etc.) and a supply item can belong to many shipments. The database should also track how many of each supply item was sent in a shipment.
	- Each supply item has a name and a price.
	- Lemonade stands can have many employees but an employee can only work at one stand at a time.
	- Each employee has a first name, a last name and an age. The database should also track which day of the week (M, Tu, W, Th, F, Sat, or Sun) that they work. Employees are only scheduled to work once each week.

***Representing this scenario should require 5 tables. If you find yourself with either more or less, it's likely you need to rethink the design.***

## How to Submit

For each question, take screenshots of your completed entity relationship diagrams from drawSQL.

Upload each of your images to the assignment submission on Canvas. *You should be submitting a total of 3 screenshots for this assignment.*
