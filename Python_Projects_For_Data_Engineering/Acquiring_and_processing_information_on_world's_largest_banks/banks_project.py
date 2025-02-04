import pandas as pd
import sqlite3
import datetime as dt
from bs4 import BeautifulSoup
import requests

url_path = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
target_file = './Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_file = 'code_log.txt'
frame_attributes = ['Name', 'MC_USD_Billion']


def log_progress(message):
    date_format = '%Y-%h-%d-%H:%M:%S'
    date_time = dt.datetime.now()
    date = date_time.strftime(date_format)
    with open(log_file, 'a') as file:
        file.writelines(f'{date} : {message}\n')

def extract():
    df = pd.DataFrame(columns= frame_attributes)
    site = requests.get(url_path).text
    soup = BeautifulSoup(site, 'html.parser')
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        if len(data) != 0:
            if data[1].find_all('a') is not None:
                link = data[1].find_all('a')
                context = {
                    'Name': link[1].get_text(strip= True),
                    'MC_USD_Billion': data[2].contents[0].strip()
                }

                df_data = pd.DataFrame([context], index = [0])
                df = pd.concat([df, df_data], ignore_index= True)
    return df


def transform(df):
    df_rate_exchange = pd.read_csv('exchange_rate.csv').set_index('Currency')
    dict_rate_exchange = df_rate_exchange.to_dict()['Rate']
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype('float')
    df['MC_GBP_Billion'] = round(df['MC_USD_Billion'] * dict_rate_exchange['GBP'], 2)
    df['MC_EUR_Billion'] = round(df['MC_USD_Billion'] * dict_rate_exchange['EUR'], 2)
    df['MC_INR_Billion'] = round(df['MC_USD_Billion'] * dict_rate_exchange['INR'], 2)
    return df


def load_to_csv(df):
    try:
        df.to_csv(target_file)
        print('File Downloaded successfully !')
    except:
        print('File Not Downloaded !')


def load_to_db(df):
    conn = sqlite3.connect(db_name)
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=True)
        print('Table created successfully !')
    except:
        print('Table not created !')
    finally:
        conn.close()


def run_queries(query_statement):
    conn = sqlite3.connect(db_name)
    print(query_statement)
    data = pd.read_sql(query_statement, conn)
    print(data)
    conn.close()


log_progress('Preliminaries complete. Initiating ETL process')

data = extract()

log_progress('Data extraction complete. Initiating Transformation process')

data_transformed = transform(data)

log_progress('Data transformation complete. Initiating Loading process')

load_to_csv(data_transformed)

log_progress('Data saved to CSV file')
log_progress('SQL Connection initiated')

load_to_db(data_transformed)

log_progress('Data loaded to Database as a table, Executing queries')

query = 'SELECT * FROM Largest_banks'
run_queries(query)
query = 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
run_queries(query)
query = 'SELECT Name from Largest_banks LIMIT 5'
run_queries(query)

log_progress('Process Complete')

log_progress('Server Connection closed')

