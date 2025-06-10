#Tuplas
mi_tupla = (1,2,3,1,2,3,1)
mi_lista = [4,5,6]
print(mi_tupla[0])
print(mi_lista)
mi_lista[0] = 9
print(mi_lista)
#mi_tupla[0] = 5

print(mi_tupla.count(1))
print(mi_tupla.index(1))

#Conjuntos

mi_conjunto = {1,2,3,3,4}
print(mi_conjunto)

#Diccionarios

mi_diccionario = {'nombre': 'Luis Fernando', 'apellido': 'Corrales', 'edad': 48}
print(mi_diccionario)

estudiantes = {
    'ana':{'edad':20, 'carrera': 'Ingenieria', 'promedio': 8.7},
    'luis': {'edad':22, 'carrera': 'Medicina', 'promedio': 9.1},
    'carla': {'edad':21, 'carrera': 'Derecho', 'promedio': 8.3},
}

# nombre = 'ana'
# if nombre in estudiantes:
#     print(f'{nombre} {estudiantes[nombre]}')
# else:
#     print('Estudiante no encontrado')

# info = estudiantes.get('luis', "Estudiante no encontrado")
# print(info)

# print(estudiantes.keys())
# print(estudiantes.values())
# print(estudiantes.items())

estudiantes['ana'].update({'promedio': 10.0})

estudiantes.update({
    'mario':{'edad':23,'carrera':'Arquitectura','promedio':8.5}
})
estudiantes.update({
    'miguel':{'edad':23,'carrera':'Arquitectura','promedio':8.5}
})

print(estudiantes.items())
eliminado = estudiantes.pop('miguel','No existe')

print(estudiantes.items())

#Mostrar a todos los estudiantes con promedio mayor a 8.5

for nombre, datos in estudiantes.items():
    if datos['promedio'] > 8.5:
        print(f'{nombre.title()} tiene un promedio de {datos['promedio']}')