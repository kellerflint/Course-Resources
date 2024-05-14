# Final Exam Info

There is a **required in-person final exam** for this course on **Monday June 17th from 12:00-2:00pm** PST at the Auburn Center in room AC 310 (1221 D St NE, Auburn, WA 98002).

If you cannot attend the final exam at that time you **MUST** get in contact with me as soon as possible to make other arrangements. Please email me at kflint-blanchard@greenriver.edu.

# Topics

The following topics may appear on the final exam:

### Database Concepts:
- Tables and their structure
- Primary and foreign keys
- Relationships between tables (one-to-many, many-to-many)
- Data types
	- DATE
	- INT
	- TEXT
	- VARCHAR
	- DECIMAL

### SQL Querying:
- SELECT statements
- WHERE clauses
- LIKE operator
- ORDER BY clause
- Aggregate functions (e.g., AVG, SUM, COUNT)
- GROUP BY clause
- JOINs (if included in the exam)

### Entity Relationship Diagrams (ERDs):
- Understanding and creating ERDs given the SQL CREATE statements or a set of tables
- Identifying entities, attributes, datatypes, and relationships
- Crow's foot notation for representing relationships

### Applying SQL Queries for Data Analytics:
- Applying SQL concepts to solve real-world scenarios
- Calculating aggregated metrics (e.g., total sales, average price, etc.)
- Combining data from multiple tables using JOINs
- Presenting data in a meaningful and understandable format
- Drawing insights and conclusions from the data

# Cheat Sheet

I **do not** allow you to bring your own notes for the final exam. I will provide the following cheat sheet on the exam day that will show the basic syntax of all the commands you will need.

### SELECTs, Operators and Clauses
```sql
-- SELECT Syntax
SELECT Column1, Column2, ... FROM TableName

-- Table JOIN Syntax
JOIN TableName2 ON TableName1.PrimaryKeyColumn = TableName2.ForeignKeyColumn

-- WHERE Syntax
WHERE condition

-- WHERE Operator List
WHERE condition AND condition
WHERE condition OR condition
WHERE ColumnName BETWEEN x AND y
WHERE NOT condition
WHERE ColumnName IN (x, y, z)
WHERE ColumnName LIKE "Pattern"
-- The LIKE operator is used in the WHERE clause to search for a specified pattern in a column. It is often used with wildcard characters such as:
-- The percentage sign (%) represents zero, one, or multiple characters.
-- The underscore sign (_) represents a single character.
```

```sql
-- ORDER BY
-- 1 Column, Descending
ORDER BY ColumnName DESC
-- Multiple Columns, Ascending
ORDER BY Column1, Column2,... ASC
```

### GROUP BY and Aggregation
```sql
-- GROUP BY Command
GROUP BY ColumnName
HAVING condition

/* GROUP BY Example: Selects the COUNT of rows for each unique value in Column1, but only includes groups with a COUNT greater than 10. */
SELECT Column1, COUNT(*) FROM TableName 
GROUP BY Column1 
HAVING COUNT(*) > 10; 

-- Aggregate Functions
COUNT(*)
MAX(ColumnName)
MIN(ColumnName)
SUM(ColumnName)
AVG(ColumnName)
```


### CREATE and INSERT Statements
```sql
-- CREATE Table
CREATE TABLE TableName(
	-- Add Column
	Column1 datatype,
	-- Can be NULL
	Column2 datatype NULL,
	-- Cannot be NULL
	Column3 datatype NOT NULL,
	
	-- Establish Primary Key Constraint
	Primary Key (Column1),
	-- Establish Foreign Key Constraint
	FOREIGN KEY (ForeignKeyColumn) REFERENCES OtherTable(PrimaryKeyColumn)
);

INSERT INTO TableName VALUES ("Column1Value", "Column2Value", ...);

-- Data Types
DATE -- Stores the date in the format "YYYY-MM-DD"
INT
TEXT -- Stores long form text
VARCHAR(MaxCharacters)
DECIMAL(Digits, NumberOfDigitsAfterDecimalPoint)
```
