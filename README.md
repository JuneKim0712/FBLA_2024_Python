# FBLA_Project
--- 

## Dependencies
This script requires the following Python libraries:
- tkinter
- ttk

This script also requires the mysql-connector-python package. You can install it using pip:
```
pip install mysql-connector-python
```
.
In addition, it requires a MySQL database which can be installed on [here](https://dev.mysql.com/downloads/installer/) and press the second download button listed.

---

##  ui.py
### Overview
The ui.py script is a Graphical User Interface (GUI) application developed using Python's tkinter library. This application interacts with a MySQL database to provide a user-friendly interface for searching, filtering, and displaying data.

Features
Search Bar: 
The GUI includes a search bar where users can input search terms. The search function is triggered by either clicking the "Search" button or pressing the Enter key. This feature allows users to quickly find specific data within the database.

Filter and Sort Options: 
The GUI also includes filter and sort options, which are not currently implemented in this version of the script. These features will allow users to refine their search results based on specific criteria and sort the results in a specific order.

Results Display: 
The results of the search are displayed in a treeview widget. Each result is represented as a row in the treeview, with columns for different attributes of the result.

Usage
To run the GUI, simply execute the script. The GUI will open in a new window. You can then use the search bar to search the database, and the results will be displayed in the treeview.

---

## database.py
### Overview
The database.py script provides a Database class that interacts with a MySQL database. 
It includes methods for listing all records, filtering records, searching records, sorting records, searching, filtering, and sorting records, storing new records, altering existing records, deleting records, and closing the database connection.

---

## init_db.py 
### Overview
The init_db.py script is used to initialize a MySQL database. 
It creates a database and a table, and populates the table with data. 
This script is intended to be run once, to set up the database for the rest of the application.

### Usage
To initialize the database, simply run the script. 
It will create a database named "mydatabase" and a table named "mytable". 
The table will be populated with example data defined in init_db.py.

## Roadmap