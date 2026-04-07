def mostrar_productos(inventario):
    for fila in inventario:
        for producto in fila:
            print("inventario:",producto)

print("inciando inventario")



inventario = [
    ['pizza','campero','comida china'],
    ['agua','jugo','gaseosa'], 
]

#ciclo externo, viaja por las filas completas (niveles)


for fila in inventario:
    for producto in fila:
        if producto == "agua":
            #producto = "vacio"
            fila[fila.index(producto)] = "vacio"
            break
print("="*15)

mostrar_productos(inventario)


#manera 2
for fila in range (len (inventario)):
    for columna in range (len(inventario[fila])):
        if inventario [fila][columna] == "vacio":
            inventario[fila][columna] = "pepsi"
            break
        

mostrar_productos(inventario)