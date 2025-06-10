# Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
celsius = 0
fahrenheit = 0

celsius = float(input('Introduzca la temperatura en grados Celsius: '))

fahrenheit = celsius * 9 / 5 + 32

print(f'La temperatura en grados Farenheit es: {fahrenheit:.2f}°F ')

# Crea un programa que pida al usuario el radio de un círculo y luego imprima el perímetro del círculo. Usa el valor de π (pi) como 3.14159.
pi = 3.14159
radio = 0
perimetro = 0


radio = float(input('Introduzca el radio del circulo: ' ))
perimetro = 2 * pi * radio

print(f'El perimetro del circulo es {perimetro:.2f}')




# Escribe un programa que solicite al usuario una distancia en millas y luego imprima la distancia equivalente en kilómetros. Usa la conversión: 1 milla = 1.60934 kilómetros.
millas = 0
kilometros = 0


millas = float(input('Intruce la distancia en millas: '))
kilometros = millas * 1.60934

print(f' La distancia en kilometros es de {kilometros:.2f} km')






# TAREA

# Escribe un programa que solicite al usuario el capital inicial, la tasa de interés anual y el número de años, y luego imprima el interés simple. La fórmula para calcular el interés simple es: Interés = capital * tasa * años

# Crea un programa que pida al usuario una cantidad de tiempo en segundos y luego imprima el equivalente en horas, minutos y segundos.