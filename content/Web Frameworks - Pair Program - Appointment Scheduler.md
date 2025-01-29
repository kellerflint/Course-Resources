# Pair Program: Appointment Scheduler

## Overview

Your goal is to create a simple appointment scheduler. The application will include a form where users can enter their first and last name along with a meeting date and time. The form will submit this data to a backend server, which will store and return the array of booked appointments.

---

## Collaboration Setup

### GitHub Repository Setup

1. One person creates a new repository on GitHub with a README file.
    
2. Both partners create a new folder on their local machine and open it in VS Code.
    
3. Open the VS Code terminal and run the following command inside the folder:
    
    ```
    git clone <repo-url> .
    ```
    

### Collaboration Process

- Only **one person should be typing** at a time (the driver). The other person (the navigator) provides guidance.
    
- Switch roles **every 5 minutes**.
    
- Follow the proper Git workflow:
    
    1. **Before starting work**: Pull the latest changes `git pull`
        
    2. **After making changes**:
        
        - Stage changes: `git add .`
            
        - Commit changes: `git commit -m "your message here"`
            
        - Push changes: `git push`
            
    3. **Before switching roles**: The new driver pulls changes again to ensure they're up to date.
        

---

## Step-by-Step Implementation

### Step 1: Initialize the Project

- Set up a new Node.js project.
    
- Create an Express server that responds with "Hello, World!".
    
- Reference: [kellerflint/Node-Pizza-App at 1-hello-world](https://github.com/kellerflint/Node-Pizza-App/tree/1-hello-world?tab=readme-ov-file#create-your-project)
    
- _Remember to .gitignore your node_modules/_
    

### Step 2: Create the Appointment Form

- Build a simple HTML form with the following inputs:
    - First Name
    - Last Name
	- Date (Use `<input type="date">`)
	- Time (Use `<input type="time">`)
	- Submit Button
- Serve this page using Express.
    
- Reference: [kellerflint/Node-Pizza-App at 2-static-files](https://github.com/kellerflint/Node-Pizza-App/tree/2-static-files?tab=readme-ov-file#serving-static-files-with-express-2-static-files)
    

### Step 3: Handle Form Submissions

- Create a POST route to handle form submissions.
    
- Store submitted appointments in an array on the backend.
    
- Add a timestamp (the time of form submission) to each stored appointment.
    
- Send users to a confirmation page after submitting the form.
    
- Reference: [kellerflint/Node-Pizza-App at 3-posting-data](https://github.com/kellerflint/Node-Pizza-App/tree/3-posting-data?tab=readme-ov-file#setting-up-form-processing)
    

### Step 4: Create an Admin Route

- Set up an admin route that displays all submitted appointments.

---

## Challenges

- **Generate Dynamic Admin Page**: Instead of showing raw data, write code to generate HTML that displays the stored appointments in a user-friendly way.
- **Validation**: Prevent the server from saving submissions if the first or last name is blank. 
- **Generate Dynamic Confirmation Page**: After form submission instead of sending the user a static confirmation page, write code to generate the HTML to display a confirmation with the data they entered.
