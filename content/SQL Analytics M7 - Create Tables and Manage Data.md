# Create Tables and Manage Data

## CREATE, ALTER, DROP

<iframe src="https://share.descript.com/embed/zJJWNOvV9nr" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## INSERT, UPDATE, DELETE

<iframe src="https://share.descript.com/embed/3XaKOxT7zkS" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Constraints

<iframe src="https://share.descript.com/embed/ZOpC1jZU6tB" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Practice Questions

### Part 1 (6 pts)

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

### Part 2 (6 pts)

Create a new database and run the following script:

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
    
	PRIMARY KEY (CarId)
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

Submit your SQL script for the "M7 Practice - Create Tables and Manage Data" assignment on canvas.
