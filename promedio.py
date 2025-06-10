#Este es un programa que calcula el promedio de 3 notas
nota1 = 0
nota2 = 0
nota3 = 0
sumatoria = 0
cantidad = 3
promedio = 0
nombre_estudiante = ''

nombre_estudiante = input('Ingrese el nombre del estudiante: ')
nota1 = float(input('Introducir la nota del examen 1: '))
nota2 = float(input('Introducir la nota del examen 2: '))
nota3 = float(input('Introducir la nota del examen 3: '))

sumatoria = nota1 + nota2 + nota3

promedio = sumatoria / cantidad #Esta variable calcula el promedio de las notas

#print('El valor del promedio es de: ',promedio)
#print('El valor del promedio es de: '+str(promedio))
print(f'{nombre_estudiante} su valor del promedio es de : {promedio}')
#print(f'El valor promedio de  las notas es {sumatoria/cantidad}')

