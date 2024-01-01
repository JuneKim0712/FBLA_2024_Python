import mysql.connector

# Defining a class named Database
class Database:
    # Initializing the class
    def __init__(self):
        # Connecting to the MySQL database
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="936700",
        database="DB"
        )
        # Creating a cursor object to execute SQL queries
        self.mycursor=self.db.cursor()

    # Method to list all records from the database
    def list_all(self):
        sql = "SELECT * FROM list"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    # Method to filter records based on type and sector
    def filter(self, type=None, sector=None):
        if type != None and sector != None: sql = f"SELECT * FROM list WHERE type = '{type}' AND sector ='{sector}'"
        if type != None:
            sql = f"SELECT * FROM list WHERE type = '{type}'"
        elif sector != None:
            sql = f"SELECT * FROM list WHERE sector = '{sector}'"
        else:
            sql = "SELECT * FROM list"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    # Method to search records based on a search term and category
    def search(self, search_term="", category="name"):
        sql = f"SELECT * FROM list WHERE {category} LIKE '%{search_term}%'"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    # Method to sort records based on a category and order
    def sort(self, category="name", order="ASC"):
        sql = f"SELECT * FROM list ORDER BY {category} {order}"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    # Method to search, filter and sort records
    def search_filter_sort(self, search_term="", search_category="name", filter_type="", filter_sector="", sort_category="name", order="ASC"):
        sql = f"""  SELECT * FROM list 
                    WHERE {search_category} LIKE '%{search_term}%' AND 
                    type LIKE '%{filter_type}%' AND sector LIKE'%{filter_sector}%' 
                    order by {sort_category} {order}"""
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    # Method to store a new record in the database
    def store(self, name, type, sector, resources, individual, email, phone, address, date):
        self.mycursor.execute("SELECT COUNT(*) FROM LIST")
        id = int(self.mycursor.fetchone()[0]) + 1
        sql = """   INSERT INTO list (id, name, type, sector, resources, individual, email, phone, address, date) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        values = (id, name, type, sector, resources, individual, email, phone, address, date)
        self.mycursor.execute(sql, values)
        self.db.commit()
        return

    # Method to alter an existing record in the database
    def alter(self, id, name, type, sector, resources, individual, email, phone, address, date):
        sql = """   UPDATE list 
                    SET name = %s, type = %s, sector = %s, resources = %s, 
                    individual = %s, email = %s, phone = %s, address = %s, date = %s
                    WHERE id = %s   """
        values = (name, type, sector, resources, individual, email, phone, address, date, id)
        self.mycursor.execute(sql, values)
        self.db.commit()
        return

    # Method to delete a record from the database
    def delete(self, id):
        sql = "DELETE FROM list WHERE id = %s"
        self.mycursor.execute(sql, (id,))
        self.db.commit()
        return

    # Method to close the database connection
    def close(self):
        self.mycursor.close()
        self.db.close()
        return