numero_uno = 0
numero_dos = 0

suma = numero_uno + numero_dos

# def nombre_de_la_funcion(parametros):
        #return

def saludar(nombre):
    #Esto es una funcion para saludar por el nombre a una persona
    return f'Hola {nombre}, espero que tengas un excelente dia'

#print(saludar('Fernando'))
#print(saludar('Ricardo'))

def saludar_sin_return(nombre):
    print(f'Hola {nombre}, espero que tengas un excelente dia')


#saludar_sin_return('Luis')


def sumar(a,b):
    suma = a + b
    return suma

#print(sumar(25,33))

def recibir_un_valor():
    parametro = float(input('Ingrese un numero'))
    return parametro

#print(sumar(recibir_un_valor(),recibir_un_valor()))


def mostrar_menu():
    while True:
        print('\n----MENU PRINCIPAL---')
        print('1. Saludar')
        print('2. Sumar dos numeros')
        print('3. Salir')

        opcion = input('Elige una opcion (1-3)')

        if opcion == '1':
            nombre = input(' Como te llamas:? ')
            saludar_sin_return(nombre)
        elif opcion =='2':
            try:
                a = recibir_un_valor()
                b = recibir_un_valor()
                print(sumar(a,b))
            except ValueError:
                print('Por favor ingresa un numero valido')
        elif opcion == '3':
            print('Hasta luego')
            break
        else:
            print('Ingresa una opcion entre 1 y 3')


mostrar_menu()