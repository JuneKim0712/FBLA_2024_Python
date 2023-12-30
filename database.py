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
        
    def filter(self, type=None, sector=None):
        if type != None and sector != None: return False
        if type != None:
            sql = f"SELECT * FROM list WHERE type = '{type}'"
        elif sector != None:
            sql = f"SELECT * FROM list WHERE sector = '{sector}'"
        else:
            sql = "SELECT * FROM list"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search(self, keyword="", category="name"):
        sql = f"SELECT * FROM LIST WHERE {category} LIKE '%{keyword}%'"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    