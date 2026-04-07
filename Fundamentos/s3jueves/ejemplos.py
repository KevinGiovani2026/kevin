producto = { "nombre":"arroz", "precio":1200.0, "cantidad" : 5}

print (producto["nombre"])
print (producto["precio"])

total = producto["cantidad"] * producto["precio"]
print(f"el total de los productos son: {total}")

print(producto)
#update  antes 1200 ahora 1500
producto["precio"] = 1500
#------------------------------
#si vendi un arroz voy a actualizar

producto["cantidad"] = producto["cantidad"] - 1 
print(producto)

#agregar

producto["categoria"] = "granos"

print(producto)

#Recorrer diccionario
for clave in producto:
    print(f"clave:{clave}: valor : {producto[clave]}")

#forma #forma 2
for clave, valor in producto.items():
    print(f"clave:{clave}:")