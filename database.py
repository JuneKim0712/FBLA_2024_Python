import mysql.connector


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="936700",
        database="DB"
        )
        self.mycursor=self.db.cursor()
        
    def all(self):
        sql = "SELECT * FROM list"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
        
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
    
    def search(self, keyword="", category="name"):
        sql = f"SELECT * FROM list WHERE {category} LIKE '%{keyword}%'"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def sort(self, category="name", order="ASC"):
        sql = f"SELECT * FROM list ORDER BY {category} {order}"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_filter_sort(self, search_keyword="", search_category="name", filter_type="", filter_sector="", sort_category="name", order="ASC"):
        sql = f"""  SELECT * FROM list 
                    WHERE {search_category} LIKE '%{search_keyword}%' AND 
                    type LIKE '%{filter_type}%' AND sector LIKE'%{filter_sector}%' 
                    order by {sort_category} {order}"""
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def store(self, name, type, sector, resources, individual, email, phone, address, date):
        self.mycursor.execute("SELECT COUNT(*) FROM LIST")
        id = int(self.mycursor.fetchone()[0]) + 1
        sql = """   INSERT INTO list (id, name, type, sector, resources, individual, email, phone, address, date) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        values = (id, name, type, sector, resources, individual, email, phone, address, date)
        self.mycursor.execute(sql, values)
        self.db.commit()
