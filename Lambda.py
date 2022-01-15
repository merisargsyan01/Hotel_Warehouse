## Stay table 
import psycopg2
import json
import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import datetime,timedelta,date
from info import connection_params


connection = psycopg2.connect(
    host = connection_params["host"],
    database = connection_params["database"],
    user = connection_params["user"],
    password = connection_params["password"],
    port = connection_params["port"]
    )
    
def lambda_handler(event, context):
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



## Bill table 

def lambda_handler(event, context):
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


## Working table 

def lambda_handler(event, context):
    conn = connection
    with conn.cursor() as cursor:
        conn.autocommit = True
        sql = 'SELECT employee_id FROM employee;'
        employee = pd.io.sql.read_sql_query(sql,  conn)
        sql = 'SELECT room_id FROM room;'
        room = pd.io.sql.read_sql_query(sql, conn)
     
        working = defaultdict(list)

        for i in range(5):
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











