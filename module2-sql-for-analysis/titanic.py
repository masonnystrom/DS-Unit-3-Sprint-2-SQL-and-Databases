import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() # looks inside the .env file for some env vars
# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_PORT =  os.getenv("DB_PORT", default="OOPS") 

titanic = pd.read_csv('titanic.csv')
# print(titanic.columns)
sql_url = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(sql_url)

titanic.to_sql('titanic', engine, if_exists='replace', index=False)

conn = engine.connect()
print(type(conn)) 

result = conn.execute('SELECT * From titanic').fetchone()
