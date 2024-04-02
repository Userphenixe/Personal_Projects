import sqlite3
# Connecting to the Sqlite Database

conn = sqlite3.connect('Tracks.sqlite')
cur = conn.cursor()
# Tables Creation

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name  TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title  TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);
''')
# Importing The file
handle = open('tracks.csv')

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7 :
        continue
# Iterating the List and storing the 7 Components each one in a Variable
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    print(name, artist, album, count, rating, length, genre)
# Inserting the data into the DataBase
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
# Retrieving The Primay key for this table, storing it in the id_user variable for future insert.
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
# Retrieving The Primay key for this table, storing it in the id_user variable for future insert.
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre(name)
        VALUES (?)''',(genre, ))
# Retrieving The Primay key for this table, storing it in the id_user variable for future insert.
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]
# Inserting the primary keys in the table , this primary keys came from the two other tables.
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id , len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, length, rating, count ) )
# Interacting with the Database.
    cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
                FROM Track JOIN Genre JOIN Album JOIN Artist
                ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id
                ORDER BY Artist.name LIMIT 3''')
    Output = cur.fetchone()
    print(Output)
    conn.commit()