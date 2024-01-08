## Running Database Scripts

To get started with hands-on practice, you'll need data to populate your database. We'll do this by running a SQL script. Follow these steps to execute the script on your database:

1. **Download and Open the SQL File**:
    - Download the script file [[CustomerScript.sql]]. It contains the commands to create tables and insert data into them. It can be opened with any text or code editor. I'd recommend [Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/) but you can use whatever software you'd like.
2. **Access phpMyAdmin**:
    - From your WebHostingForStudents Client Area (https://webhostingforstudents.com/accounts/clientarea.php), find your website and click the "Log in to cPanel" button.
    - Once in cPanel, click "phpMyAdmin" under the "Databases" section.
3. **Connect to Your Database**:
    - Make sure you're connected to the correct database where you want to run the script. In this case, it will be the database you created for this class. In phpMyAdmin you can do this by clicking on the database name on the left side of the screen.
4. **Run the Script**:
    - To run SQL code, click the "SQL" tab in the horizontal menu at the top of the screen.
    - Copy over the entire contents of the SQL script into the editor. 
    - Click the "Go" button at the bottom right. This will create tables and populate them with data.
5. **Verify the Data**:
    - After running the script, check to ensure that tables are created and data is inserted. You can do this by running a simple SELECT query, like `SELECT * FROM tablename;`.

Back: [[Select and Filter Data - Introduction]] | Next: [[Select and Filter Data - SELECT Statement]] 