
from collections import defaultdict
import pandas as pd
import psycopg2
import numpy as np
import boto3
from info import connection_params_dw

s3 = boto3.client('s3')

def connect_to_db(instance_params: dict):
    conn = None
    conn = psycopg2.connect(
            host = connection_params_dw['host'],
            port = connection_params_dw['port'],
            database = connection_params_dw['database'],
            user = connection_params_dw['user'],
            password = connection_params_dw['password']
        )
    return conn
    
def lambda_handler(event, context):
    conn = connect_to_db(connection_params_dw)
    with conn.cursor() as cursor:
        conn.autocommit = True
        hotel_tables = (
            'employee',
            'hotel_location',
            'customer' ,
            'payment_method',
            'facilities',
            'hotel',
            'room',
            'shop',
            'restaurant',
            'cafe',
            'hotel_shop',
            'hotel_restaurant',
            'hotel_cafe',
            'hotel_employee',
            'hotel_facility',
            'working',
            'stay',
            'bill'
            )
        
        for table in hotel_tables:
            copy_data = f"COPY {table} FROM 's3://my--bucket1/{table}/{table}' iam_role 'arn:aws:iam::935537535054:role/service-role/AmazonRedshift-CommandsAccessRole-20220111T222240' FORMAT AS PARQUET;"
            cursor.execute(copy_data)
    conn.close()