# Select and Filter Data - Running Scripts

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=3b6bc768-5330-4f2b-9f42-b0f20177a502&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

To get started with hands-on practice, you'll need data to populate your database. We'll do this by running a SQL script. Follow these steps to execute the script on your database:

1. **Open the SQL File**:
    - Open the script file <a href="https://github.com/kellerflint/Course-Resources/blob/hugo/content/SQL-Files/CustomerScript.sql" target="_blank">CustomerScript.sql (github.com)</a>. It contains the commands to create tables and insert data into them.
2. **Access phpMyAdmin**:
    - From the WebHostingForStudents Client Area, find your website and click the "Log in to cPanel" button.
    - Once in cPanel, click "phpMyAdmin" under the "Databases" section.
3. **Connect to Your Database**:
    - Make sure you're connected to the database that you want to run the script on. In this case, it will be the database you created for this class. In phpMyAdmin you can select the database by clicking on its name on the left side of the screen.
4. **Run the Script**:
    - To run SQL code, click the "SQL" tab in the horizontal menu at the top of the screen.
    - Copy over the entire contents of the SQL script into the editor. 
    - Click the "Go" button at the bottom right. This will create the tables defined in the script and populate them with data.
5. **Verify the Data**:
    - After running the script, check to ensure that tables are created and data is inserted. You can do this by running a simple SELECT query, like `SELECT * FROM tablename;.

# Lessons
- [[SQL - W2 Select and Filter Data - Introduction]]
- [[SQL - W2 Select and Filter Data - Creating a Database]]
- SQL - W2 Select and Filter Data - Running Scripts
- Next: [[SQL - W2 Select and Filter Data - SELECT Statement]]
- [[SQL - W2 Select and Filter Data - WHERE Clause and Comparison Operators]]
- [[SQL - W2 Select and Filter Data - Logical Operators]]
- [[SQL - W2 Select and Filter Data - ORDER BY]]
- [[SQL - W2 Select and Filter Data - SQL Comments]]
- [[SQL - W2 Select and Filter Data - Note on Semicolons]]
- [[SQL - W2 Select and Filter Data - Practice Assignment]]
