# Lessons and Practice - Basic Querying 
## Estimated Time to Complete: 3 ~ 10 hours

*Use the Northwind database for all questions.*
### [[SQL Analytics M3 - NULL Values|Null Values]]

### [[SQL Analytics M3 - Aggregate Functions|Aggregate Functions]]

1. Write a single query to display the minimum, average and maximum price of products and the total number of products.
2. Write a single query to display the total number of customers that are in North America (Canada, Mexico or the USA).
3. Marketing wants to know how many products we have in the produce category (Category ID 7). Write a query to display this information
### [[SQL Analytics M3 - GROUP BY|GROUPY BY]]

4. Write a single query to display the number of products in each category.
5. Write a single query to display how many orders each employee has processed.
6. The Supplier Procurement team would like to better understand how the pricing of our products differ between Northwind's many suppliers. Write a single query to display the minimum, average price and maximum prices of products from each supplier and the total number of products they supply.

### [[SQL Analytics M3 - HAVING|HAVING]]

7. Write a single query to display the average price of the products in each category. Show only categories that have an average price of at least $25. Order the results from highest to lowest average price.
8. Write a single query to display the number of times each product has been ordered (using orderdetails). Show only products that have been ordered at least 100 times.
### [[SQL Analytics M3 - Understanding Query Order|Understanding Query Order]]

9. Answer the following in a comment in your SQL script. A junior data analysist at Northwind comes to you and asks why one of their queries works while the other doesn't. Identify which query will succeed and which will fail. Then explain in simple and clear terms (that a new data analyst could understand) your reasoning for this.

```sql
/* Query #1 */
SELECT
    Category,
    SUM(Quantity) AS TotalQuantity,
FROM Sales
WHERE TotalQuantity > 10;
```

```sql
/* Query #2 */
SELECT
    Category,
    SUM(Quantity) AS TotalQuantity,
FROM Sales
ORDER BY TotalQuantity DESC;
```

Submit your answers for the "M3 Practice" assignment on canvas.