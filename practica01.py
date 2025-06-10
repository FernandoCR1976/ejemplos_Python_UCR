#Hacer un programa que calcule el perimetro y el area de un rectangulo

lado1 = 0
lado2 = 0
perimetro = 0

lado1 = float(input('Ingrese el lado 1 del rectangulo: '))
lado2 = float(input('Ingrese el lado 2 del rectangulo: '))


perimetro = (lado1 * 2) + (lado2 * 2)
area = lado1 * lado2

print(f'El perimetro del rectangulo es de {perimetro} y su area es de {area}')