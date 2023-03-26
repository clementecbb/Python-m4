import pandas as pd

#       DATAFRAMES

#datos rrss2020
fbk=['Facebook',2449, True,2006]
twt = ['Twitter',339,False,2006]
ig = ['Instagram',100, True, 2010]
yt = ['Youtube',2000, False,2005]
lkn = ['Linkedin',663, False,2003]
wsp = ['Whatsapp', 1600, True,2009]

lista_rrss = [fbk,twt,ig,yt,lkn,wsp,]

#crear dataframe a partir de listas
df_rrss=pd.DataFrame(lista_rrss, columns =["Nombre", "Cantidad","ES_FBK","Año"])

print(df_rrss)