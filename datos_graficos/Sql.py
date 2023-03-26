import sqlite3
import pandas as pd

#como extraer working directory

import os
os.getcwd()

#   CARGAR LA BASE DE DATOS 

path = "ruta sqlite-sakila.db"

sqliteConecconnection = sqlite3.connect(path)
cursor = sqliteConecconnection.cursor()

#mirar las tablas de una BBDD
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

#   COMO HACER QUERIES CON SQLITE3

#como hacer queries con fetchall e imprimir todo
query = "SELECT * FROM film LIMIT 5"
cursor.execute(query)
print(cursor.fetchall())

#comos hacer queries con fetchallcy ciclo for
query = "SELECT * FROM film LIMIT 5"
cursor.execute(query)
output = cursor.fetchall()
for row in output:
    print(row)

