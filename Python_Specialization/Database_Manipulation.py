import sqlite3
import re
con = sqlite3.connect('Coursera_Task.sqlite')
cur = con.cursor()
cur.execute('DROP Table IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
liste = list()
file = 'mbox.txt'
handle = open(file)
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        liste.append(line[1])
for item in liste:
    # Using Regular Expressions
    matches = re.findall(r'@([A-Za-z0-9.-]+\.[A-Za-z]{2,})', item)
    org = matches[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    con.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()