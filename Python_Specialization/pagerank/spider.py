import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen, Request

import webs

from bs4 import BeautifulSoup
import time

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# To add a User-Agent to the request header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
     error INTEGER, old_rank REAL, new_rank REAL)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Links
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

# Check to see if we are already in progress...
cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.")
else :
    starturl = input('Enter web url or enter: ')
    # Your URL handling and initialization code

many = 0
while True:
    if many < 1:
        sval = input('How many pages:')
        if len(sval) < 1:
            break
        many = int(sval)
    many = many - 1

    cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NOT NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cur.fetchone()
        fromid = row[0]
        url = row[1]
    except:
        print('No unretrieved HTML pages found')
        many = 0
        break

    print(fromid, url, end=' ')

    cur.execute('DELETE from Links WHERE from_id=?', (fromid, ) )
    try:
        retries = 3
        for attempt in range(retries):
            try:
                req = Request(url, headers=headers)
                document = urlopen(req, context=ctx)

                html = document.read()
                if document.getcode() != 200 :
                    print("Error on page: ",document.getcode())
                    cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )
                    break

                if 'text/html' != document.info().get_content_type() :
                    print("Ignore non text/html page")
                    cur.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
                    conn.commit()
                    break

                print('('+str(len(html))+')', end=' ')

                soup = BeautifulSoup(html, "html.parser")
                break  # Break out of retry loop if successful
            except Exception as e:
                print(f"Error retrieving page ({e}), retrying...")
                time.sleep(2 ** attempt)  # Backoff strategy

        if attempt == retries - 1:
            print("Failed to retrieve page after multiple retries")
            cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
            conn.commit()
            continue

    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except Exception as e:
        print(f"Unable to retrieve or parse page ({e})")
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
        conn.commit()
        continue

    cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( url, ) )
    cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url ) )
    conn.commit()

    # Retrieve all the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href', None)
        if href is None:
            continue
        # Resolve relative references like href="/contact"
        up = urlparse(href)
        if len(up.scheme) < 1:
            href = urljoin(url, href)
        ipos = href.find('#')
        if ipos > 1:
            href = href[:ipos]
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif'):
            continue
        if href.endswith('/'):
            href = href[:-1]
        if len(href) < 1:
            continue

        found = False
        for web in webs:
            if href.startswith(web):
                found = True
                break
        if not found :
            continue

        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) )
        count = count + 1
        conn.commit()

        cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id')
            continue
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( fromid, toid ) )

    print(count)

cur.close()
