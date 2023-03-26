import pandas as pd

#datos
fbk =["Facebook",2449,True,2006]
twt =["Twitter",339,False,2006]
ig =["Instagram",1000, True,2010]
yt =["Youtube", 2000, False, 2005]
lkn =["LinkedIn", 663, False, 2003]
wsp =["Whatsapp", 1600, True,2009]

lista_rrss = [fbk,twt,ig,yt,lkn,wsp]
#crear dataframe 
df_rrss = pd.dataframe(lista_rrss, columns =["Nombre", "Cantidad", "ES_FBK", "Año"])

print(df_rrss)

#crear dataframe vacio
df_vacio = pd.dataframe(columns=["Nombre", "Cantidad", "ES_FBK", "Año"])

#agregar contenido
df_vacio=df_vacio.append({"Nombre":"Facebook",
                         "Cantidad":2449,
                         "ES_FBK": True,
                         "Año":2006}, ignore_index = True)

# seleccionar un elemento por etiquetas
df_rrss.loc[1, "Nombre"]

#seleccionar un elemento por numero
df_rrss.iloc[1, 0]

#seleccionar por columnas
df_rrss["Nombre"]

#seleccionar fila
df_rrss.iloc[4]

#seleccion por booleano
df_rrss["Cantidad"]>1500
df_rrss[df_rrss["Cantidad"]>1500]

#   Como ordenar columnas

#ordenar de modo ascendente: demenor a mayor
df_rrss.sort_values("Nombre", ascending= True)
#ordenar descendente: mayor a menor
df_rrss.sort_values("Cantidad", ascending= False)
#ordenar por dos valores
df_rrss.sort_values(["Año","Cantidad"],ascending=[True, False])
#ordenar por dos columnas
