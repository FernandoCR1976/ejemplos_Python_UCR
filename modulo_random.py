import random

# for i in range(0,10):
#     numero_random = int((random.random())*29)
 
#     print(f'{numero_random} este es el ciclo # {i+1}')

numero_random_2 = random.randint(0,29)
print(numero_random_2)

lista = ['verde','azul','amarillo','violeta']
color_aleatorio = random.choice(lista)
print(color_aleatorio)

lista_dos = ['verde','azul','amarillo','violeta']
#lista_random = lista_dos
random.shuffle(lista_dos)
print(lista_dos)
#print(lista_random)