import sqlite3

connection = sqlite3.connect('student1.db')

cursor = connection.cursor()

table_info =  """
CREATE TABLE IF NOT EXISTS Student1 (
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    section TEXT
);

"""
cursor.execute(table_info)  

cursor.execute("INSERT INTO Student1 values('John Doe', 20, 'A', 'A1')")
cursor.execute("INSERT INTO Student1 values('Jane Smith', 22, 'B', 'B1')")
cursor.execute("INSERT INTO Student1 values('Alice Johnson', 19, 'A', 'A2')")
cursor.execute("INSERT INTO Student1 values('Bob Brown', 21, 'C', 'C1')")    

connection.commit()
connection.close()