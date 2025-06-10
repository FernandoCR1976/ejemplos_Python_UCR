# edad = 20
# mayor_de_edad = 0
# if edad >= 18:
#     mayor_de_edad = True
# else:
#     mayor_de_edad = False

# print(f'El usuario es mayor de edad: {mayor_de_edad}')


clasificacion = ''
edad = float(input('Ingrese la edad de la persona: '))

if edad <= 12:
    clasificacion = "Niño"
elif edad <= 18:
    clasificacion = "Adolescente"
elif edad <= 40:
    clasificacion = "Adulto Joven"
elif edad <= 65:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto Mayor"

print(f'La clasificacion de la persona es de : {clasificacion}')
