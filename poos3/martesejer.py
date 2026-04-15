# class Productos:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

    
#     def __add__(self, otro_producto):
#          return self.precio + otro_producto.precio

#     def __str__(self):
#         return f"{self.nombre} (Q{self.precio})"
    

# producto1 = Productos("camara", 100)
# producto2 = Productos("gorra", 30)
# producto3 = Productos("pantalla", 500)
# producto4 = Productos("Teclado", 50)

# resultado = producto1 + producto2 + producto3 + producto4

# print(resultado.precio)

# ##no funciona
#///////////////////////////////////////////
# import math

# raiz = math.sqrt(25)

# print(raiz)

# from math  import pi,pow 
# area_circulo = pi * pow(5,2)

# print(area_circulo)

# import datetime as dt

# fecha_de_hoy = dt.date.today()

# print(fecha_de_hoy)
#////////////////////////////////////

import random 

prueba = random.randint(1, 10)
print(prueba)

#////////////////////////////

from random import choice 

mi_lista = ["ana", "Luis", "carlos"]

print(random.choice(mi_lista))

#///////////////////////////////////////////

import math as matematicas

numero = matematicas.ceil(10.5)

print(numero)

