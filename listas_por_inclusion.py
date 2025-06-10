# nueva_lista = [expresion for elemento in iterable condicion]

#Crear una lista de numeros al cuadrado

cuadrados = []
for numeros in range(1,10):
    cuadrados.append(numeros ** 2)

print(cuadrados)

cuadrados_por_inclusion = [i ** 2 for i in range(1,10000)]

print(cuadrados_por_inclusion)

#Sacar los numeros pares de una lista
pares = []
for i in cuadrados_por_inclusion:
    if i % 2 == 0:
        pares.append(i)
print(pares)
print(f'Hay {len(pares)} numeros pares en la lista')

pares_por_inclusion = [i for i in cuadrados_por_inclusion if i % 2 == 0]
print(pares_por_inclusion)
print(f'Hay {len(pares_por_inclusion)} numeros pares en la lista')


palabras = ['manzana', 'pera', 'zanahoria','sandia','papaya']

longitud_palabra = [len(palabra) for palabra in palabras]
print(longitud_palabra)

mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)