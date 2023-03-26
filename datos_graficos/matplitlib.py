import matplotlib.pyplot as plt

#ejemplo basico
x= [1,2,3,4,5]
y= [1,9,12,34,122]
plt.plot(x,y)
plt.show()



#grafico de lineas 
plt.plot(df_rrss["Nombre"], df_rrss["Cantidad"])
plt.show()
#grafica de puntos
plt.scatter()

#Extra mtodos de un dataframe de pandas
"dataframe".plot(kind="scatter", x="Nombre", y="Cantidad")


#grafico de barras
plt.bar()

#grafico de barra ordenada
"dataframe".sort= "dataframe".sort_value("Cantidad", ascending=False)


#grafica de torta
plt.pie()