

# Querying and Analysis for HR Database Project - HR Database Overview

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=1bda4f91-4cd6-4dad-b0e3-b10100555862&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## Initialize the HR Database

- DROP the tables from your previous assignment(s), if necessary
	- See [[Table JOINs - DROP Tables]] for a refresher on dropping tables.
- Run the following script to populate your database -> <a href="https://github.com/kellerflint/Class-Intro-SQL/blob/hugo/content/Files/HRScript.sql">HRScript.sql (github.com)</a>
	- See [[Select and Filter Data - Running Scripts]] for a refresher on running DB scripts.
## HR Database Overview

The HR Database is designed to mirror a typical business's human resources data management system. It's structured to handle employee data, departmental divisions, and job details. Here's a brief description of each table:

##### 1. `employees` Table:

- `employee_id`: Unique identifier for each employee (Primary Key).
- `first_name`: First name of the employee.
- `last_name`: Last name of the employee.
- `email`: Email address of the employee.
- `phone_number`: Contact phone number of the employee.
- `hire_date`: The date when the employee was hired.
- `job_id`: Identifier for the job role of the employee, referencing `jobs` (Foreign Key).
- `salary`: The salary of the employee.
- `manager_id`: The ID of the employee's manager, referencing `employees` (Foreign Key).
- `department_id`: Identifier for the department the employee belongs to, referencing `departments` (Foreign Key).

##### 2. `jobs` Table:

- `job_id`: Unique identifier for each job role (Primary Key).
- `job_title`: Title of the job role.
- `min_salary`: Minimum salary for the job role.
- `max_salary`: Maximum salary for the job role.

##### 3. `departments` Table:

- `department_id`: Unique identifier for each department (Primary Key).
- `department_name`: Name of the department.
- `location_id`: Identifier for the location of the department, referencing `locations` (Foreign Key).

##### 4. `dependents` Table:

- `dependent_id`: Unique identifier for each dependent (Primary Key).
- `first_name`: First name of the dependent.
- `last_name`: Last name of the dependent.
- `relationship`: The relationship of the dependent to the employee.
- `employee_id`: Identifier for the employee to whom the dependent is related, referencing `employees` (Foreign Key).

##### 5. `regions` Table:

- `region_id`: Unique identifier for each region (Primary Key).
- `region_name`: Name of the region.

##### 6. `countries` Table:

- `country_id`: Unique identifier for each country (Primary Key).
- `country_name`: Name of the country.
- `region_id`: Identifier for the region to which the country belongs, referencing `regions` (Foreign Key).

##### 7. `locations` Table:

- `location_id`: Unique identifier for each location (Primary Key).
- `street_address`: Physical address of the location.
- `postal_code`: Postal code of the location.
- `city`: City where the location is based.
- `state_province`: State or province of the location.
- `country_id`: Identifier for the country of the location, referencing `countries` (Foreign Key).



Back: [[Querying and Analysis for HR Database Project - Introduction]] | Next: [[Querying and Analysis for HR Database Project - Assignment]]
