"""
import numpy as np

num_primos= [2,3,5,7,11,13,17,19,23,29]

#array de los num primos
array_primos = np.array(num_primos)

#array con ceros
array_zeros = np.zeros(10)

#crear array con numeros
array_num =np.arange(10)

#array con num sucesibos
array_pares= np.arange(0, 20, 2)

#hacer reshape para dos dimensiones
array_pares.reshape(2,5)


#operaciones con array
#sumar
array_impares= array_pares +1
#multiplicar
array_pares * 100
#dividir
array_impares / array_pares
#suma de sus valores
array_primos.sum()
#promedio
array_primos.mean()
#varianza
array_primos.var()
#como ordenar un np array
array_fibonacci = np.array([55,0,144,1,21,89,5,8,13,1,34,3,2])
#orden ascendente menor a mayor
np.sort(array_fibonacci)
#orden desendente mayor - menor
-np.sort(-array_fibonacci)


#selecciona elementos
A = np.arange(0,20,2).reshape(2,5)

#primer elemento
A[0,0]
#otro elemento
A[1,3]
#seleccionar varios elementos
A[1,:]
#seleccionar por columna
A[: ,3]
#utilizar filtros

    #condicion para menores de 20
array_fibonacci<20
    #filtro para menores de 20
array_fibonacci[array_fibonacci<20]

"""