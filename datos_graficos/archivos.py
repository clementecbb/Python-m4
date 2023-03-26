import pandas as pd

#archivos EXCEL

#extraer la ruta del archivo
path = "nombre de fichero"

# datos completos en la primera hoja
ps.read_excel(path)


#los datos no estan en la primera hoja
pd.read_excel(path,sheet_name="Hoja 2")

#no hay nombres de columnas
pd.read_excel(path, sheet_name="Hoja 3", header= Nonen, names=["Nombre", "Cantidad","Es_FBK","Año"])



#archivos CSV

#datos separados por comas
pd.read_csv("ruta.csv")

#datos separados por punto y coma (;)
pd.read_csv("ruta.csv",sep=";")

#no hay nombres de columnas
pd.read_csv("ruta.csv", header=None, names=["Nombres","Calidad","Es_FBK","Anio"])

