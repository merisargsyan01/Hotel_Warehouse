import boto3
import psycopg2
import pytz
import pandas as pd
from datetime import datetime, timedelta
from info import connection_params

BucketName = 'my--bucket1'

connection = psycopg2.connect(
    host = connection_params["host"],
    database = connection_params["database"],
    user = connection_params["user"],
    password = connection_params["password"],
    port = connection_params["port"]
    )

def put_object_to_S3(
	conn,
	client,
	tables: tuple
):
	for table in tables:
		sql = f"""
				SELECT * FROM {table}
				;
			   """
		frame = pd.io.sql.read_sql_query(sql,  conn)
		frame.to_parquet(
			f's3://{BucketName}/{table}/{table}',
			compression='brotli',
			engine='pyarrow',
			index=False
			)
	
def lambda_handler(event, context):
    conn = connection
    s3_client = boto3.client('s3')
    
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
    
    
    put_object_to_S3(conn, s3_client, hotel_tables)
    
    return 0