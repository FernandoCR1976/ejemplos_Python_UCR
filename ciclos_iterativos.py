# contador = 1
# while contador <= 5:
#     print('Iterando', contador)
#     contador = contador + 1

# palabra = "Python"
# for letra in palabra:
#     print(letra)

# cadena = [1,2,3,4,5,6,7]
# print(f'La palabra Python tiene {len(palabra)} ')



# for i in cadena:
#     print(i)

# for i in range(5):
#     print("Repeticion numero ", i)

# #Utilizando for  in range hagan un conteo que empiece en 1 y termine en 5

# for i in range(5):
#     print("Repeticion numero ", i + 1)





# cadena_2 = [1,2,3,4,5,6,7]
# acumulador = 0
# for numero in cadena_2:
#     print(f'Numero: {numero}')
#     acumulador += numero
#     print(f'Aculador: {acumulador}')

while True:
    print("\n---MENU PRINCIPAL--")
    print('1. Saludar')
    print('2. Suma de dos numeros')
    print('3.salir')

    opcion = input("Elige una opcion (1-3): ")

    if opcion == '1':
        print("Hola, este es un programa de prueba")
    elif opcion == '2':
        a = float(input('Ingresa el primer numero: '))
        b = float(input('Ingresa el segundo numero: '))
        print(f' La suma de los dos numeros es {a+b}')
    elif opcion == '3':
        print('Gracias por utilizar mi software')
        break
    else:
        print("Opcion invalida, INTENTE DE NUEVO")