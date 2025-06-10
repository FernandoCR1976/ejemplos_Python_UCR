#Necesitamos desarrollar un programa, que reciba 4 calificaciones, las almacene en una lista y que calcule el promedio. Ademas que nos diga si el estudiante aprobo(nota mayor a 70), aplazo(nota mayor a 60 pero menor que 70) o reprobo el curso(nota menor que 60)

notas  = []
nota_1 = 0
nota_2 = 0
nota_3 = 0
nota_4 = 0
promedio = 0
condicion = ''

nota_1 = float(input("Ingrese la nota 1: "))
notas.append(nota_1)
nota_2 = float(input("Ingrese la nota 2: "))
notas.append(nota_2)
nota_3 = float(input("Ingrese la nota 3: "))
notas.append(nota_3)
nota_4 = float(input("Ingrese la nota 4: "))
notas.append(nota_4)

promedio = sum(notas)/len(notas)

print(promedio)

if(promedio >= 70):
    condicion = 'Aprobado'
elif(promedio >= 60):
    condicion = "Aplazado"
else:
    condicion = "Reprobado"

print(f'El promedio del alumno fue de {promedio:.2f} y su condicion es de {condicion}')

#Ahora, queremos saber cual fue la mayor nota obtenida
nota_mayor = max(notas)
indice_nota_mayor = notas.index(nota_mayor)


#Imprimir en pantalla cual fue la nota mayor y a que nota corresponde

print(f'La mayor nota obtenida fue de {nota_mayor} y corresponde a la nota {indice_nota_mayor+1}')