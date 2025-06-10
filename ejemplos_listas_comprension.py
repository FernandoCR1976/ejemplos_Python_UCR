# Instrucciones:
# Resuelve los siguientes ejercicios usando listas por inclusión. No uses bucles tradicionales.

# Crear una lista con los cubos de los números del 1 al 10.
cubos = [x**3 for x in range(1,11)]
print(cubos)

# Generar una lista con los números impares del 1 al 20.
impares = [x for x in range(1,21) if x % 2 != 0]
print(impares)
# Convertir una lista de strings a minúsculas.
frases = ['Luis Fernando','Jose Pablo', 'Maria Jose', 'Elena Patricia', 'Alba Isabel']
frases_minisculas = [frase.lower() for frase in frases]
print(frases_minisculas)
# Filtrar los nombres que empiezan con la letra "A".
nombres = ['Ana','Juana','Angela','Ricardo','Antonio']
empieza_con_a = [nombre for nombre in nombres if nombre.startswith('A')]
print(empieza_con_a)
# Crear una lista de los primeros 10 múltiplos de 3.
multiplos_3 = [ x for x in range(1,31) if x % 3 == 0]
print(multiplos_3)
# Dada una lista de palabras, obtener su longitud.
palabras = ['python','listas','esdrujula','codigo']
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)
# Crear una lista de números del 1 al 100 que sean divisibles por 5 y 7.
# Reemplazar los espacios por guiones en una lista de frases.
# Crear una lista de booleanos que indiquen si los números del 1 al 10 son pares.
# Dada una lista de temperaturas en Celsius, convertirlas a Fahrenheit.