
# inventario = [  
# [10, 4, 8],
# [5, 12, 3],
# [7, 20, 6]
# ]
# #esto si sirve
# total = 0


# for fila in inventario:
#         for cantidad in fila:
#             if cantidad > 5 and cantidad % 2 == 0:
#                 total = total + cantidad

# print("la cantidad de frutas es:", total)

#//////////////////////////////////////

precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

# precio = 0
# for fila in precios_pasillos:
#         for cantidad in fila:
#             if cantidad < 50 :
#                 precio = precio + cantidad * 0.1
               
# print(precio)

#//////////////////////

for fila in range(len(precios_pasillos)):
    for columna in range(len(precios_pasillos)[fila]):
        print(precios_pasillos[fila][columna])
        #if precios_pasillos[fila][columna] < 50:
            #precios_pasillos[fila][columna] = precios_pasillos[fila][columna] * 0.1
            
#print (precios_finales)


