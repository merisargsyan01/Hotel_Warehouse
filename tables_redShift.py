import pandas as pd
import psycopg2
import tables
from connection_ import connection_dw


def create_tables():
    commands = tables.hotel_tables_dw

    try:
        cur = connection_dw.cursor()
        for command in commands:
            cur.execute(command)
            
        table_names = tables.table_names
        cur.close()
        connection_dw.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection_dw is not None:
            connection_dw.close()          
        

create_tables()

print("Done")

