Gas Management System - Tkinter and MySQL Project
This project is a Gas Management System implemented using Python's Tkinter for the GUI and MySQL for database management. It allows users to perform CRUD (Create, Read, Update, Delete) operations on gas records.

Features:
CRUD Operations: Users can add, view, update, and delete gas records. Each record contains fields for gas type, quantity, price per unit, and date.

GUI Interface: Implemented using Tkinter, the application provides a user-friendly interface with entry fields for input and buttons for actions like adding, updating, and deleting records.

MySQL Database: Utilizes MySQL as the backend database to store and manage gas records. The database connection and CRUD operations are handled through Python's mysql.connector library.

Treeview Display: A Treeview widget is used to display the records fetched from the database, showing all fields of each record in a structured format.

Usage:
Add Record: Fill in the details in the input fields and click "Add Record" to insert a new gas record into the database.

View Records: Click "View Records" to fetch and display all existing gas records from the database in the Treeview widget.

Update Record: Double-click on a record in the Treeview to populate the input fields. Modify the details and click "Update Record" to save changes to the selected record.

Delete Record: Select a record in the Treeview, confirm the deletion prompt, and click "Delete Record" to remove the selected record from the database.

How to Run:
Install Python: Ensure Python is installed on your system (Python 3.x recommended).

Install Required Libraries: Run pip install tkinter mysql-connector-python to install the necessary libraries if not already installed.

Database Setup: Modify the database connection parameters (host, database, user, password) in connect_db() function to match your MySQL setup.

Run the Application: Execute the gas_management.py script. The Tkinter GUI will launch, allowing you to interact with the Gas Management System.

Files:
gas_management.py: Main script containing the Tkinter GUI and CRUD operations.
README.md: This file, providing an overview of the project, features, usage instructions, and setup details.
requirements.txt: List of Python packages required by the project.
