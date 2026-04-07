def mostrar_inventario(productos):
    #forma 1 
    for num_articulos in range (len(productos)):
        print(productos[num_articulos]["nombre"])
        print(productos[num_articulos]["precio"])
        print(productos[num_articulos]["cantidad"])
        #pass # importante para mi proyecto

        #forma 2 

        #for  num_articulo in range  (len(productos)):
    
productos = []
while True:
    nombre = input("ingrese el nombre dle producto o ingrese FIN para terminar: ")
    if nombre == "FIN": #ToDo: mejorar validacion
        mostrar_inventario(productos)
        break

    precio = float(input("ingrese el precio del producto:"))
    cantidad = int(input("ingrese la cantidad del producto:"))
    
    productito = {"nombre" : nombre, "precio" : precio, "cantidad" : cantidad}

    productos.append(productito)