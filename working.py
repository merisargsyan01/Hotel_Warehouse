import pandas as pd
import numpy as np
import psycopg2
import json
from collections import defaultdict
from datetime import timedelta,date
from connection_ import connection

def lambda_handler():
    conn = connection
    with conn.cursor() as cursor:
        conn.autocommit = True
        sql = 'SELECT employee_id FROM employee;'
        employee = pd.io.sql.read_sql_query(sql,  conn)
        sql = 'SELECT room_id FROM room;'
        room = pd.io.sql.read_sql_query(sql, conn)
     
        working = defaultdict(list)

        for i in range(20):
            working['employee_id'].append(np.random.choice(employee['employee_id'].unique()))
            working['room_id'].append(np.random.choice(room['room_id'].unique()))
            working['working_date'].append(date.today()- timedelta(days = 1))
            
        working = pd.DataFrame(working)
        working = working.drop_duplicates(
            subset = ['room_id'],
            keep = 'last').reset_index(drop = True)

        print(working)
        for i, row in working.iterrows():
            sql = 'INSERT INTO working (employee_id,room_id, working_date) VALUES (%s,%s,%s)'
            cursor.execute(sql, tuple(row))
    conn.close()
    print('Conn closed.')

lambda_handler()





