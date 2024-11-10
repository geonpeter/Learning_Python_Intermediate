import sqlite3

class Person:
    def __init__(self, id=-1, fname="", lname="", age=-1) -> None:
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.connection = sqlite3.connect('mydb.db')
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS person (
                                id INTEGER PRIMARY KEY,
                                first_name TEXT,
                                last_name TEXT,
                                age INTEGER
                            )
                            """)
        self.connection.commit()
        
    def load_data(self):
        
        self.cursor.execute("""
                            INSERT INTO person (id, first_name, last_name, age) VALUES ({}, '{}', '{}', {})
                            """.format (self.id, self.fname, self.lname, self.age))
        self.connection.commit()
        print("Record loaded successfully")
        
    def fetch_data(self):
        self.cursor.execute("SELECT * FROM person")
        results = self.cursor.fetchall()
        print(results)
        
    def __del__(self):
        # Ensure the connection is closed when the object is deleted
        self.connection.close()

if __name__ == "__main__":
    
    p1 = Person(1, 'Miriam', 'Peter', 6)
    p1.create_table()
    p1.load_data()
    p1.fetch_data()
