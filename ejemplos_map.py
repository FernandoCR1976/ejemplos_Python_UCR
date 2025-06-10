import math
numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = list(map(lambda x: x**2, numeros))
print(resultado)

pares_resultado = [list(filter(lambda x: x % 2 == 0,resultado))]
print(pares_resultado)

#f(x)=x+2

palabras = ['manzana','casa','carro','tomate']
mayusculas = list(map(str.upper,palabras))
print(mayusculas)

palabras_4_letras = list(filter(lambda x: len(x)<=5,palabras))
print(palabras_4_letras)

pares_cuadrados = list(map(lambda x: x**2,filter(lambda x: x%2==0,numeros)))
print(pares_cuadrados)

# Ejercicios de práctica
#Convertir una lista de números en sus cubos usando map()
cubos = list(map(lambda x: x**3,numeros))
print(cubos)

#Filtrar números impares usando filter()
impares_cubos = list(filter(lambda x: x%2!=0,cubos))
print(impares_cubos)

#Filtrar cadenas que contienen la letra 'o' del arreglo palabras usando filter()
contiene_o = list(filter(lambda x: 'o' in x, palabras))
print(contiene_o)

#Obtener las raíces cuadradas de una lista de numeros usando map() {math.sqrt() = x**0.5}
raices_numeros = list(map(lambda x: math.sqrt(x),numeros))
raices_num_dos = list(map(lambda x: x**0.5,numeros))
print(raices_numeros)
print(raices_num_dos)

#Obtener la longitud de cada cadena de palabras usando map()
longitudes = list(map(lambda x: len(x),palabras))
print(longitudes)