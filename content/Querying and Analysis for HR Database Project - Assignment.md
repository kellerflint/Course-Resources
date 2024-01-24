
Every questions should be answered with exactly one query. You will need exactly one SELECT statement per question. Be sure to provide complete and correct answers to each questions.
# Section 1: Understand the Data Structure

**Question 1:** Write a query to list all the regions available in the `regions` table.

**Question 2:** Find all countries in the `countries` table that are part of the region with `region_id` 2. Display the country names and their respective region IDs.

**Question 3:** List the job titles from the `jobs` table where the minimum salary is greater than 5,000 a month. Order the results by the minimum salary in ascending order.

**Question 4**: Retrieve the city and street address of all locations from the `locations` table that have the `country_id` of of 'UK'. Sort the results by city in alphabetical order.

**Question 5**: Identify all departments in the `departments` table that have the `location_id` 1700. Display the department name and location ID.

**Question 6**: Find all employees whose last name starts with an 'H'. Display their employee ID, first name, last name, email, and salary.

**Question 7**: Display the first and last names of dependents along with the ID of the employee they are related to. Order the results by employee ID in descending order.

# Section 2: Construct Relational Queries

**Question 8**: List all dependents along with the names of the employees they are dependent on. Display each dependent's first and last name, and the first and last name of the associated employee.

**Question 9**: Which employees work in the 'Shipping' department? Display the department name along with each employee's IDs, first name, and last name.

**Question 10**: Find all locations in the 'Americas' region. Display the country name, state/province, city and street address.  List them in alphabetical order by the state/province.

**Question 11**: List the first names, last names, job titles and salaries a of all employees who have 'Manager' in their job title.

**Question 12**: Display the names and job titles of employees who work in a city than 'Seattle'. Display the name of the city they work in as well.

# Section 3: Perform Data Analysis

***Use a multi-line comment to write explanations in the same .sql file as your queries.***

**Question 13**: In what months are most employees hired? Provide a single query to justify your answer.
*You can use `MONTH(some_date_column)` to extract just the month from a date.*

**Question 14**: Why is Steven King's manager ID null? Write a one or two sentence explanation. Provide a single query to prove your answer.

**Question 15**: Which cities seem to pay the highest salaries? Provide the query you wrote to explore this relationship. Write a few sentences explaining how you came to this conclusion based on your query results.
*It might be useful to order by two columns! Think about which two would make the most sense. See [[Select and Filter Data - ORDER BY]] for a refresher on ordering by multiple columns.*

**IMPORTANT**: Make sure you copy your **ENTIRE SCRIPT** into PHPMyAdmin and run it against the database before you submit. Confirm that everything works as expected. **If you submit a script that does not run it will receive a ZERO!** Start early so you have time to get help and make corrections if needed!

Back: [[Querying and Analysis for HR Database Project - HR Database Overview]]