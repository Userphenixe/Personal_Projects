import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3
import datetime as dt

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
target_file = 'Countries_by_GDP.csv'
table_name = 'Countries_by_GDP'
db_name = 'World_Economies.db'
attributes = ['Country', 'GDP_USD_millions']


def extract(url_name, table_attribs):
    df = pd.DataFrame(columns = attributes)
    site = requests.get(url_name).text
    data = BeautifulSoup(site, 'html.parser')
    table = data.find_all('tbody')
    rows = table[2].find_all('tr')
    for row in rows:
        td = row.find_all('td')
        if len(td) != 0:
            if td[0].find('a') is not None and '—' not in td[2]:
                context = {
                    'Country': td[0].a.contents[0],
                    'GDP_USD_millions': td[2].contents[0]
                }
                df1 = pd.DataFrame(context, index = [0])
                df = pd.concat([df, df1], ignore_index = True)
    return df



def transform(df):
    df['GDP_USD_millions'] = df['GDP_USD_millions'].str.replace(',', '').astype('float')
    df['GDP_USD_millions'] = np.round(df['GDP_USD_millions'] / 1000, 2)
    df = df.rename(columns = {'GDP_USD_millions' : 'GDP_USD_billions'})
    return df

def load_to_csv(df, csv_file):
    df.to_csv(csv_file)

def load_to_db(df, sql_connection, table):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)



def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    now = dt.datetime.now()
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')


log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, attributes)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, target_file)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()