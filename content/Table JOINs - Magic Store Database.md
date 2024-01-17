
# Table JOINs - Magic Store Database

Video Embedding - need to tell them how to drop old stuff first. Then add new tables.

## Add the Magic Store Database

- DROP the tables from your previous assignment(s)
- Run the following script to populate your database <a href="https://github.com/kellerflint/Class-Intro-SQL/blob/hugo/content/Files/MagicStoreScript.sql" target="_blank">MagicStoreScript (github.com)</a>

## Magic Store Database Overview

**You may not understand all the details of these tables yet. Don't worry!** We're about to go through it all in detail in the next few lessons. For now, here's a quick overview you can reference back to as needed when working on the practice questions for this section.

The Magic Store Database contains the records of a store that sells potions, ingredients and enchanted items to witches and wizards across the world. These tables are structured to handle a typical e-commerce scenario, where clients place orders for products, and each order can contain multiple products. The `OrderProduct` table is a joining table that manages the many-to-many relationship between orders and products.

##### 1. `Product` Table:
- `ID`: Unique identifier for each product.
- `Name`: Name of the product.
- `Price`: Price of the product.
##### 2. `Client` Table:
- `ID`: Unique identifier for each client.
- `FirstName`: First name of the client.
- `LastName`: Last name of the client.
- `AccountCreated`: The date when the client's account was created.
##### 3. `Order` Table:
- `ID`: Unique identifier for each order.
- `OrderedOn`: The date when the order was placed.
- `ClientID`: Identifies the client who placed the order.
##### 4. `OrderProduct` Table:
- `OrderID`: Identifies the order. It is linked to the `Order` table.
- `ProductID`: Identifies the product. It is linked to the `Product` table.
- `Quantity`: How many of each product are included in an order.



Back: [[Table JOINs - DROP Tables]] | Next: [[Table JOINs - One-to-Many Relationships]]
