# M4 SQL for Data Analytics

## Lessons and Example Scenario

<iframe src="https://share.descript.com/embed/Ood9LD2dOMG" width="720" height="405" frameborder="0" allowfullscreen></iframe>

Example Dataset (if interested): https://github.com/kellerflint/Course-Resources/blob/hugo/content/SQL-Files/NetflixShowsScript.sql

---
# M4 Peer Review Assignment - Video Game Market Analysis Assignment

<iframe src="https://share.descript.com/embed/oJrKOhRRAU0" width="720" height="405" frameborder="0" allowfullscreen></iframe>

## Background
You are a data analyst working for a video game studio. The studio is planning their next game and wants to use relevant market data to inform their decision. They've approached you with a request to analyze recent video game sales data.

## The Studio's Request
>We're trying to decide what our next big game should be. We'd like to look at video game sales data to understand which genres are most relevant and which games in those genres are the most popular. We also need to know what platform we should develop for. Analyze this data and present your findings at our next meeting.

## Your Task
You will use SQL to analyze a database of video game sales. Your goal is to provide insights that will help the studio make informed decisions about their next game. This task involves dealing with a large, somewhat ambiguous request. You'll need to break it down into manageable parts and make some assumptions along the way.

## Data
You have access to a table named `games` in a SQL database. This table contains information about video games, including their sales figures. You can view the structure of this table using the query `SELECT * FROM games;`.

## Assignment Instructions

### Setup
Create a new database and run the following script:
https://github.com/kellerflint/Course-Resources/blob/hugo/content/SQL-Files/VideoGameScript.sql

**IMPORTANT**: Use ONLY SQL commands covered in our class so far! (`SELECT` `AS` `FROM` `WHERE` `GROUP BY` `HAVING` `ORDER BY` `LIMIT`). This ensures peer reviewers can understand your work and tests your ability to solve problems with the tools you’ve learned so far.

### 1. Data Exploration
Begin by examining the data available to you. First, make sure you are using the correct database.

```sql
USE games;
```

Use the following query to retrieve all records:

```sql
SELECT * FROM games;
```

Take note of the columns available and the type of information they contain. This will help you understand what data you have to work with.

### 2. Question Breakdown
Consider how you can use the available data to answer the studio's request. Break down the main question into specific sub-questions that you can answer with SQL queries. List these sub-questions.

### 3. Identify Ambiguities and Assumptions
Identify any ambiguities in these questions. What assumptions do you need to make to proceed with your analysis? For example, how do you define "relevant" sales data? List your assumptions and explain your reasoning for any choices you make.

### 4. Write and Execute Queries
Write SQL queries to answer the sub-questions you identified in step 2. Do not try to write a single giant query that does everything. Use multiple queries to answer different parts of the request and that clearly show the results. Your queries should:
- Be clear and readable
- Include comments explaining your thought process
- Logically follow from one to the next
- Support your conclusions

Remember, you should write these queries so that another data analyst could follow your process and reasoning.

### 5. Analysis and Presentation
Based on the results of your queries, what conclusions can you draw? 
- In a comment, write a few sentences giving your specific findings and recommendations.
- Write a few clear, concise queries that show only the most essential data and results to support your conclusions. These should be queries you could present to business stakeholders to support your conclusions.

Note: There may not be one perfect answer. The results you get will depend on the assumptions you made and how you approached the request.

### 6. Limitations of the Analysis
Reflect on the limitations of your data and analysis. Are there any ways in which this data might not show the full picture? What additional information might be helpful for making a more informed decision?

## Submission
Submit a single SQL file to Canvas containing your code and comments for each section. This should include:
1. Your data exploration query
2. Your list of sub-questions
3. Your list of assumptions
4. Your analysis queries with comments
5. A brief written section discussing your conclusions and presentation queries for business leadership
6. A brief written section on the limitations of your data and analysis

Remember to use ONLY the SQL techniques we've covered in class such as SELECT statements using AS, WHERE, GROUP BY, ORDER BY, LIMIT, and calculations or aggregate functions.

# Peer Review Component

After the due date, you will be assigned to review the work of two peers. Reviews should provide professional, clear and constructive feedback in a 2-3 paragraph response. Peer reviewers are expected to clearly identify at least one area they thought could be improved on or an additional consideration the submission could have considered.

Your feedback will be graded separately for it's clarity and relevance. I'll provide more information about peer reviews next week.