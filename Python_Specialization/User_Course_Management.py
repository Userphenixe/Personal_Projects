import json
import sqlite3
# Connecting to the Sqlite Database
con = sqlite3.connect('Users.sqlite')
cur = con.cursor()
# Tables Creation
cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    
    CREATE TABLE User(
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
    
    CREATE TABLE Course(
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        titre TEXT
    );
    
    CREATE TABLE Member(
        id_user INTEGER,
        id_course INTEGER,
        role INTEGER,
        PRIMARY KEY(id_user, id_course)
    )
    ''')
# Importing The file and loading the data inside it as a JSON format
file = input('Please enter the json file name:')
if len(file) < 1:
    file = 'roster_data.json'
text = open(file)
data = json.load(text)
# Iterating the List and storing the 3 Components each one in a Variable
for item in data:
    name = item[0]
    titre = item[1]
    role = item[2]
# Inserting the data into the DataBase
    cur.execute('''
        INSERT OR IGNORE INTO User(name) VALUES(?) ''', (name,))
# Retrieving The Primay key for this table, storing it in the id_user variable for future insert.
    cur.execute('''
        SELECT id FROM User WHERE name = ?''', (name,))
    id_user = cur.fetchone()[0]

    cur.execute('''
        INSERT OR IGNORE INTO Course(titre) VALUES(?)''', (titre,))
    # Retrieving The Primay key for this table, storing it in the id_user variable for future insert.
    cur.execute('''
        SELECT id FROM Course WHERE titre = ?''', (titre,))
    id_course = cur.fetchone()[0]
# Inserting the primary keys in the table , this primary keys came from the two other tables.
    cur.execute('''
        INSERT OR REPLACE INTO Member(id_user, id_course, role) VALUES(?, ?, ?)''', (id_user, id_course, role))
    con.commit()
# Interacting with the Database.
cur.execute('''
        SELECT User.name, Course.titre, Member.role
        FROM User
        JOIN Member ON User.id = Member.id_user
        JOIN Course ON Member.id_course = Course.id
        ORDER BY User.name DESC, Course.titre DESC, Member.role DESC
        LIMIT 2;
    ''')
Outputs = cur.fetchall()
print(Outputs)
# Interacting with the Database, this time as a hexadecimal format.
cur.execute('''
        SELECT 'XYZZY' || hex(User.name || Course.titre || Member.role ) AS X FROM 
        User JOIN Member JOIN Course 
        ON User.id = Member.id_user AND Member.id_course = Course.id
        ORDER BY X LIMIT 1;
    ''')
Output = cur.fetchall()
print(Output)














