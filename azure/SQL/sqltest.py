  
"""
title - This is a python script to simply connect to Azure mysql cluster.
author name - Aditya Kumar
creation time -  9 April 2021 
modified time - 30 April 2021

"""
import pyodbc
from decouple import config

server = config('server')
database = config('database')
username = config('username')
password = config('password' )  
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
