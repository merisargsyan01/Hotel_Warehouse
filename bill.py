import json
import psycopg2
import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import timedelta,date
from connection_ import connection


def generator():
    conn = connection
    with conn.cursor() as cursor:
        conn.autocommit = True
        sql = 'SELECT payment_method_id FROM payment_method;'
        payment_method = pd.io.sql.read_sql_query(sql,  conn)
        sql = 'SELECT facility_id FROM facilities;'
        facilities = pd.io.sql.read_sql_query(sql,  conn)
        sql = 'SELECT customer_id FROM customer;'
        customer = pd.io.sql.read_sql_query(sql, conn)
     
        bill = defaultdict(list)

        for i in range(10):
            bill['transaction_date'].append(date.today() - timedelta(days = int(np.random.choice(list(range(1,5))))))
            bill['amount'].append(np.random.choice(list(range(30000,100000,5000))))
            bill['payment_method_id'].append(np.random.choice(payment_method.payment_method_id))
            bill['facility_id'].append(np.random.choice(facilities['facility_id'].unique()))
            bill['customer_id'].append(np.random.choice(customer['customer_id'].unique()))
            
        bill = pd.DataFrame(bill)
        print(bill)
        for i, row in bill.iterrows():
            sql = 'INSERT INTO bill (transaction_date,amount, payment_method_id,facility_id,customer_id) VALUES (%s,%s,%s,%s,%s)'
            cursor.execute(sql, tuple(row))
    conn.close()
    print('Conn closed.')

generator()


