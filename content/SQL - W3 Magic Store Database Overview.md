
# Magic Store Database Overview


<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=ff2760b3-299f-459d-853e-b0fb000eac4a&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## Initialize the Magic Store Database

- DROP the tables from your previous assignment(s), if necessary
- Run the following script to populate your database -> <a href="https://github.com/kellerflint/Course-Resources/blob/hugo/content/SQL-Files/MagicStoreScript.sql" target="_blank">MagicStoreScript (github.com)</a>

## Magic Store Database Overview

**You may not understand all the details of these tables yet. Don't worry!** We're about to go through it all in detail in the next few lessons. For now, here's a quick overview you can reference back to as needed when working on the practice questions for this section.

The Magic Store Database contains the records of a store that sells potions, ingredients and enchanted items to witches and wizards across the world. These tables are structured to handle a typical e-commerce scenario, where clients place orders for products, and each order can contain multiple products. The `OrderProduct` table is a joining table that manages the many-to-many relationship between orders and products.

##### 1. `Supplier` Table:
- `ID`: Unique identifier for each supplier.
- `Name`: Name of the supplier.
- `Address`: Physical address of the supplier.
- `PhoneNumber`: Contact phone number of the supplier.
##### 2. `Product` Table:
- `ID`: Unique identifier for each product.
- `Name`: Name of the product.
- `Price`: Price of the product.
##### 3. `Client` Table:
- `ID`: Unique identifier for each client.
- `FirstName`: First name of the client.
- `LastName`: Last name of the client.
- `AccountCreated`: The date when the client's account was created.
##### 4. `Order` Table:
- `ID`: Unique identifier for each order.
- `OrderedOn`: The date when the order was placed.
- `ClientID`: Identifies the client who placed the order.
##### 5. `OrderProduct` Table:
- `OrderID`: Identifies the order. It is linked to the `Order` table.
- `ProductID`: Identifies the product. It is linked to the `Product` table.
- `Quantity`: How many of each product are included in an order.




# Lessons
- [[SQL - W3 Table JOINs - Introduction]]
- [[SQL - W3 Table JOINs - DROP Tables]]
- SQL - W3 Magic Store Database Overview
- Next: [[SQL - W3 Table JOINs - One-to-Many Relationships]]
- [[SQL - W3 Table JOINs - JOIN Tables with One-to-Many Relationships]]
- [[SQL - W3 Table JOINs - Filter and Sort with JOINs]]
- [[SQL - W3 One-to-Many JOINs - Practice Assignment]]