import pandas as pd
import psycopg2
from io import StringIO
import tables
from connection_ import connection


def copy_data_to_database(cur, data: pd.DataFrame, table_name: str):
    buffer = StringIO()
    # Save dataframe to an in memory buffer
    data.to_csv(buffer, header=False, index=False)
    buffer.seek(0)
    cur.copy_from(buffer, table_name, sep=",", columns=data.columns)
    buffer.close()
    print(f"The {table_name} data has been successfully copied to the database.")

def create_tables():
    commands = tables.hotel_tables

    try:
        cur = connection.cursor()
        for command in commands:
            cur.execute(command)
            
        table_names = tables.table_names

        for name, data in table_names.items():
            data = data
            copy_data_to_database(cur=cur, data=data, table_name=name)
        cur.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()          
        

create_tables()

print("Done")