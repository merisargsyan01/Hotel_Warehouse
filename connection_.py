import psycopg2
from info import connection_params, connection_params_dw


connection = psycopg2.connect(
    host = connection_params["host"],
    database = connection_params["database"],
    user = connection_params["user"],
    password = connection_params["password"],
    port = connection_params["port"]
    )


print("Done Connection")

connection_dw = psycopg2.connect(
    host = connection_params_dw["host"],
    database = connection_params_dw["database"],
    user = connection_params_dw["user"],
    password = connection_params_dw["password"],
    port = connection_params_dw["port"]
    )


print("Done Connection DW")