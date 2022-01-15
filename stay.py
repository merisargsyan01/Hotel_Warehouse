import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import timedelta
from connection_ import connection
    
def generator():
    conn = connection
    with conn.cursor() as cursor:
        conn.autocommit = True
        sql = 'SELECT customer_id FROM customer;'
        customer = pd.io.sql.read_sql_query(sql,  conn)
        sql = 'SELECT room_id FROM room;'
        room = pd.io.sql.read_sql_query(sql, conn)

        sql = 'SELECT * FROM stay;'
        stays = pd.io.sql.read_sql_query(sql, conn)
        stay = defaultdict(list)

        for k in range (10):
            stay['customer_id'].append(np.random.choice(customer['customer_id'].unique()))
            stay['room_id'].append(np.random.choice(room['room_id'].unique()))
            stay['check_in'].append(stays[stays['room_id'].isin(stay['room_id'])]['check_out'].max())
            stay['check_out'].append(stay['check_in'][k] + timedelta(days = int(np.random.choice(list(range(1,31))))))
            stay['num_of_people'].append(np.random.choice(list(range(1,6))))

        stay = pd.DataFrame(stay)
        stay = stay.drop_duplicates(
            subset = ['room_id'],
            keep = 'last').reset_index(drop = True)
        
        print(stay)
        for i, row in stay.iterrows():
            sql = 'INSERT INTO stay (customer_id, room_id, check_in, check_out, num_of_people) VALUES (%s,%s,%s,%s,%s)'
            cursor.execute(sql, tuple(row))
    conn.close()
    print('Conn closed.')

generator()


