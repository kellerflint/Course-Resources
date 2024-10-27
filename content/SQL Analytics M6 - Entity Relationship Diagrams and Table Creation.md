# Entity Relationship Diagrams and Creating Tables

## Understanding Entity Relationship Diagrams 

Entity Relationship Diagrams (ERDs) are a fundamental part of database design and architecture. They provide a visual representation of the data and how entities within a database relate to each other. Using ERDs can make it much easier to grasp the structure of a database without having to examine each table individually. In this section you will learn to read these diagrams, understand the relationships between tables, and apply this knowledge to create and query tables. 

<iframe src="https://share.descript.com/embed/drOIZX5Yik0" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### Part 1 Lessons and Practice Questions (8 pts)
*Click into each of the lessons below for the practice questions*
### [[SQL Analytics M6 - Entity Relationship Diagram Structure|Entity Relationship Diagram Structure]]

### [[SQL Analytics M6 - Representing Relationships|Representing Relationships]]

### [[SQL Analytics M6 - Data Types and Nullability|Data Types and Nullability]]

### [[SQL Analytics M6 - Querying from Entity Relationship Diagrams|Querying from Entity Relationship Diagrams]]


## Create Tables and Manage Data

### CREATE, ALTER, DROP

<iframe src="https://share.descript.com/embed/zJJWNOvV9nr" width="640" height="360" frameborder="0" allowfullscreen></iframe>

Full List of Data Types - [SQL Data Types for MySQL, SQL Server, and MS Access](https://www.w3schools.com/sql/sql_datatypes.asp)

### INSERT, UPDATE, DELETE

<iframe src="https://share.descript.com/embed/3XaKOxT7zkS" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### Constraints

<iframe src="https://share.descript.com/embed/ZOpC1jZU6tB" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### Part 2 Practice Questions (6 pts)
Create a new database called `Reservations` for part 2. Make sure to `USE` it when writing queries.

Write the CREATE and INSERT statements for the tables below. Use your best judgement to assign appropriate data types and constraints to your columns. After each CREATE statement, write a brief comment to give your reasoning for using (or not using) constraints on each of the columns.

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

### Part 3 Practice Questions (6 pts)
Create a new database called `Cars` for part 3. Make sure to `USE` it when writing queries. Create 2nd SQL file for your part 3 scripts.

```sql
/* Create a new database first. Make sure to USE the right database! */

DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    CustomerId INT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20) UNIQUE,

    PRIMARY KEY (CustomerId)
);

CREATE TABLE cars (
    CarId INT,
    Make VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    Year INT,
    Price DECIMAL(10, 2),
    PurchaserId INT,
    
    PRIMARY KEY (CarId),
    FOREIGN KEY (PurchaserId) REFERENCES customers(CustomerId)
);

INSERT INTO customers (CustomerId, FirstName, LastName, Email, Phone) VALUES
    (1, 'Aisha', 'Patel', 'aisha.patel@email.com', '555-1234'),
    (2, 'John', 'Smith', 'john.smith@email.com', '555-5678'),
    (3, 'Mei', 'Chen', 'mei.chen@email.com', '555-9012'),
    (4, 'Kwame', 'Osei', 'kwame.osei@email.com', '555-3456'),
    (5, 'Sarah', 'Johnson', 'sarah.johnson@email.com', '555-7890');

INSERT INTO cars (CarId, Make, Model, Year, Price, PurchaserId) VALUES
    (1, 'Toyota', 'Camry', 2022, 25000.00, 1),
    (2, 'Honda', 'Civic', 2021, 22000.00, 5),
    (3, 'Ford', 'Mustang', 2023, 35000.00, NULL),
    (4, 'Chevrolet', 'Malibu', 2022, 27000.00, 3),
    (5, 'Tesla', 'Model 3', 2023, 45000.00, 3);
```

**Without** using CREATE or INSERT, write SQL commands to handle the following scenarios for this car dealership database.
1. The dealership has decided to start tracking the color of each car.
2. There was a mistake when processing a recent order. The Honda Civic was actually sold to John Smith.
3. Mei Chen has decided to return her Tesla Model 3. The dealership has agreed to take it back.
4. Aisha Patel has changed her email address. Her new email is aishap@gmail.com.
5. Due to a special promotion, the dealership has decided to reduce the price of the Ford Mustang by $2000.
6. Kwame has decided to close their account. Data privacy laws require the company to permanently remove their information.

## How to Submit

You will have 3 deliverables for this assignment:
1. For part 1, paste in your answers to the text area or upload a PDF/Word document or a .txt or .sql file.
2. For part 2, submit a SQL script with your CREATE and INSERT statements.
3. For part 3, submit a SQL script with the table CREATEs and INSERTs provided as well as your queries for questions 1-6.

Upload / submit these files for the "M6 Practice - Entity Relationship Diagrams and Table Creation" assignment.

