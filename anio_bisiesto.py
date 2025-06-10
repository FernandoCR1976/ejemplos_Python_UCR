anio = 0
bisiesto = False

try:
    anio = int(input('Introduce el año a evaluar: '))

    if(anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        bisiesto = True
    else:
        bisiesto = False

    if(bisiesto):
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} es NO bisiesto')

except ValueError:
    print('Introduzca un valor valido')
