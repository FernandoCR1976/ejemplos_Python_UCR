#Hacer un juego mediante el cual el jugador tenga que adivinar entre 5 colores cual es el correcto
# 
import random

colores = ['rojo','negro','blanco','morado','naranja'] 
len(colores)
color_secreto = random.choice(colores)
intentos = 0

while True:
    intento = input('Adivina el color: ').lower()
    intentos += 1

    if intento == color_secreto:
        print(f'ADIVINASTE EL COLOR !!! en {intentos} intentos')
        break
    else:
        print("Incorrecto.... Intenta de Nuevo")



### HACER EL JUEGO DE PIEDRA PAPEL TIJERA, la computadora en cada turno escoge una de las tres opciones y el jugador elige cual va a ser su opcion. Gana el que acumule tres victorias.
#Reglas Papel, gana piedra; piedra gana tijera; tijera gana papel. Si escogen el mismo no hay punto

##PALINDROMOS !!!! Haz un programa que determine si una palabra es palindromo o no !!!!!