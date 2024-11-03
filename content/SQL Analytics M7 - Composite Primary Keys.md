### Back: [[SQL Analytics M7 - Many-to-Many Relationships and Entity Relationship Diagrams]]
# Composite Primary Keys

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=2cde06fb-34b8-4dcc-83f6-b11c015d2fc9&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

# Using Composite Primary Keys

How do you know when to use a composite primary key vs create a new unique identifier?

When you're creating a joining table there are times where it is appropriate to use a composite primary key and times when you'll want to create a new ID that serves as the primary key. Making this decision is based on what information is required to uniquely identify the relationship. For example, the combination of a Student and a Class will always be unique (i.e. a student cannot have multiple enrollments in the same class). When combined, those two separate keys are sufficient to uniquely identify a record in the StudentClass (or you could call it the enrollment) joining table.

This is what your CREATE statement would look like. You don't add a new ID for the StudentClass. Instead, you declare both the ClassID and StudentID as primary keys (and foreign keys).

```sql
CREATE TABLE StudentClass(
    id INT
    ClassID INT,
    StudentID INT,
    
    PRIMARY KEY(id),
    FOREIGN KEY(ClassID) REFERENCES Class(ID),
    FOREIGN KEY(StudentID) REFERENCES Student(ID)
);
```

However there are times when the combination of two keys in a table are not enough to create a unique identifier. For example, imagine we had a shopping application where users could make multiple payments on an order to pay it off over time. In that situation, the combination of the UserID and the OrderID would not be enough to establish a unique identifier because we could have multiple payments with the same combination of an order and user made on different dates. Here we would either need to add more fields to our composite primary key to make it unique or instead create a new primary key column rather than use a composite primary key. In the latter case, the OrderID and UserID would remain in the Payments table but only as foreign keys, not primary keys.  

In that example the code would look like this. We create the new ID field since the OrderID and UserID together still aren't sufficient to uniquely identify the record:

```sql
CREATE TABLE Payments(
    ID INT,
    OrderID INT,
    UserID INT,
    AmountPaid DECIMAL(10,2),
    
    PRIMARY KEY(ID),
    FOREIGN KEY(OrderID) REFERENCES Order(ID),
    FOREIGN KEY(User) REFERENCES User(ID)
);
```

### Back: [[SQL Analytics M7 - Many-to-Many Relationships and Entity Relationship Diagrams]]