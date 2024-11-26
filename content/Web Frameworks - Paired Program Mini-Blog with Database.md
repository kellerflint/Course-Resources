# Paired Program: Mini Blog with Database

## Objective

Your task is to enhance the mini blog app by replacing the in-memory array with a database. This will allow blog entries to persist beyond the server session, making the app more practical for real-world use.

## Requirements

You will need to have your database and MySQL Workbench installed and have completed the first mini blog app. You’ll be connecting to a database to store and retrieve data instead of using an array.

## Setup

 **Database Setup**:
- Open your MariaDB client and create a new database for the blog app.
- Within that database, create a table called `posts` with columns for `id`, `author`, `title`, `content`, and `created_at`. Make sure the `id` is set as the primary key and is auto-incrementing, while `created_at` defaults to the current timestamp.
- Here’s an example of how to structure the columns:
	- `id`: integer, primary key, auto_increment
	- `author`: string
	- `title`: string
	- `content`: text

**Connect to MariaDB**:
- In your `app.js` file, install the `mariadb` package. Import the package.
- Use the `mariadb.createPool()` method to set up a connection pool.
- In the connection pool configuration, specify the `host`, `user`, `password`, `database`.
- Write a helper function called `connect()` to retrieve a connection from the pool.

```js
// Import the MariaDB Package
const mariadb = require('mariadb');

// Configure the database connection
const pool = mariadb.createPool({
    host: 'localhost',
    user: 'root',
    password: '1234',
    database: 'miniblog'
});

// Function for connecting to the database
async function connect() {
    try {
        let conn = await pool.getConnection();
        console.log('Connected to the database');
        return conn;
    } catch (err) {
        console.log('Error connecting to the database: ' + err);
    }
}
```

<br>
<br>
## Update the Form Submission Route

**Convert the `/submit` Route to Save Data in the Database**:
- In your existing `/submit` POST route, instead of pushing the new post to an array, connect to the database and insert the submitted post data into the `posts` table.
- Retrieve `author`, `title`, and `content` from the request, and use an SQL `INSERT` query to save them in the database.
- After storing the data, display a confirmation page showing the submitted post details.

**Return to the Form**:
- Test that the `/submit` route successfully stores posts in the database and shows a confirmation for the submission.

## Backend Validation

**Prevent Submission of Invalid Posts**: To ensure data integrity, implement the following validation logic in your `/submit` POST route before inserting the data into the database:
- Ensure that the `title` is not empty and has more than 5 characters.
- Ensure that the `content` is not empty.
- Allow `author` to be an empty string. If `author` is empty it should be inserted into the database as `NULL` rather than an empty string.

Remove leading or trailing whitespace:
```js
data.firstName.trim()
```

**Show an error message on the frontend**: Send the user back to the home page along with any error messages from the backend.

**Make the Form Sticky**: Retain user-entered data in the form fields after any backend validation errors.

You will need to pass both the form data and the errors to the home page from your `/submit` route:
```js
res.render('home', { data: data, errors: errors });
```
## Retrieve All Posts from the Database

**Set Up the `/entries` Route**:
- Create a new route called `/entries` to display all blog posts.
- In this route, query the database to retrieve all posts from the `posts` table, ordering by `created_at` in descending order.
- Use `res.render` to display an `entries.ejs` page that will show all posts.

**Render the Posts in EJS**:
- In your `entries.ejs` file, use a loop to display each post's `author`, `title`, `content`, and `created_at`.
- Add a message like “No posts found” if there are no entries.

**Test the App:**
- Test the app by submitting a few posts via the form and verifying that each post appears on the `/entries` page.
- Check that the data persists even after restarting the server, proving the posts are stored in the database.
