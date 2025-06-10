#Uso del operador AND

a = True
b = False

resultado = a and b
print(resultado)

edad_uno = 15
edad_dos = 15
edad_tres = 20

print(edad_uno == 15 and edad_dos == 15 and edad_tres == 20)

# Uso de la operador OR

print(edad_uno == 12 or edad_dos == 11 or edad_tres == 20)

#Uso del NOT

resultado = (edad_uno == 15 and edad_dos == 15 and edad_tres == 20)

print(f' el resultado es {resultado}')

resultado = not resultado

print(f' el resultado es {resultado}')


edad = 20
tiene_licencia = True
puede_conducir = False

puede_conducir = edad >= 18 and tiene_licencia

print(f'El usuario puede conducir: {puede_conducir}')

# Verificar si la persona es menor de edad o NO tiene licencia de conducir
edad = 16
tiene_licencia = False
no_puede_conducir = False

no_puede_conducir = edad < 18 or not tiene_licencia

print(f'El usuario no puede conducir: {no_puede_conducir}')