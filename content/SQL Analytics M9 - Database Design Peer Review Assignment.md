# M9 Peer Review Assignment - Database Design

For this assignment, you will be designing and implementing a database to solve a business problem. To give some exposure to the ways you might use your SQL knowledge in industry, this problem will be roughly based on a real-world application I was tasked with designing and implementing during my first software development internship.

**Background**:

Edanava is a multinational digital consulting company. This means that other large companies hire Edanava to create software solutions for them or their customers. Edanava has grown quickly and, at any given time, has thousands of **sales opportunities** to keep track of with businesses and organizations looking to potentially hire Edanava to implement a technical project. A **sales opportunity** is essentially a deal/sale in the making. It’s how the company tracks the early stages and setup of a deal before the contract is signed and work begins.

**The Problem:**

Currently the company has no software to track these opportunities. Instead, employees on the sales team typically put each new opportunity in a word document. These documents have no enforced structure and can get very messy. Documents are emailed back and forth between different people on the sales teams which means the data can easily become unreliable or out of date as many people might end up with different versions of the same document. There is no centralized way for managers or salespeople to view or search for sales opportunities or see data or analytics about how many opportunities are closed or in progress. There is also no way to keep employees accountable or help remind them to follow up on opportunities that they may have forgotten about.

Naturally, this lack of structure means that a lot of possible business falls through the cracks. In fact, the company has estimated that it is losing out on upwards of $8 million a year in possible revenue due to opportunities that are being delayed or forgotten about due to poor tracking.

**Proposed Solution:**

In order to address this, the company has decided to create a web application that will allow the sales team to track and manage all of these opportunities in one place. The application will allow salespeople to create opportunities and add information about them. Then the application will assign available salespeople to work on the different steps of an opportunity based on their role on the team and send reminders if too much time has passed since the last step was completed. It will also allow managers to see various analytics about existing opportunities.

**Your Role:**

As the lead backend developer on this new project, you must architect the database that this new application will need.

The sales team has given you some example documents to use as a reference with the kind of information they’ll need the application to track (see documents below). All of this information is important and will need to be represented in your database with the appropriate relationships.
[[SQL Analytics - Supplemental Materials - Example Opportunity]]
[[SQL Analytics - Supplemental Materials - Opportunity Steps]]
[[SQL Analytics - Supplemental Materials - Sales Team Members]]

**Assignment Instructions:**

Design the Database: Create an Entity Relationship Diagram that contains all of the fields and relationships that will exist in your database. Make sure that your database is capable of tracking all the information currently held in the example documents without creating unnecessary redundancy.

SQL CREATE and INSERT Script: Once you have a diagram, write the SQL script to implement the tables. INSERT the data from the example documents into your tables. Start with the diagram and base your code off of it. Keep in mind that during your final I may ask questions about your approach to this assignment so make sure you understand what you're submitting!

**NOTE: YOUR DIAGRAM AND CODE MUST MATCH.** If I see perfect code but a flawed diagram that doesn't match your implementation, my immediate assumption will be that you used ChatGPT or another AI tool to complete the coding section for you without understanding the underlying concepts.

There is some intentional ambiguity in the design requirements. When you’re unsure of a requirement, use your best judgment to come up with what would make the most sense for the scenario. Feel free to reach out or stop by office hours if you have any questions/concerns. I'm looking forward to seeing what you all come up with!

**Hints**:

There are many possible ways to design this database depending on the decisions and interpretations you make. However, if you find yourself with fewer than 4 tables or more than 8, it's likely your design is either failing to track important data or it's not using tables efficiently. Either of these is an indication that you should step back and re-evaluate your design.

A good way to validate your design is to think through the actual records it might store. It is not enough to just give me a diagram, the diagram has to be viable. It is often worth creating some sample tables in excel or google sheets according to your diagram, adding in some mock data (maybe for the example opportunity linked above), and verifying that your tables can logically store and relate the data they need to track.

Keep in mind that fewer tables isn't necessarily better if it comes at the cost of losing data or failing to effectively represent a relationship.

It may be worth reviewing our lessons on database design if you aren't sure how to approach this: [[SQL Analytics M8 - Database Design]]. 

START EARLY!!! And feel free to come by office hours or work with our tutors if you need support.