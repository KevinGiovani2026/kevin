#****************************************
inventario=8
print(inventario > 5)

inventario=8
print(inventario == 8)
#*************************************** 

manzanas = 5
producto_nombre = manzana
precio_manzanas = 500

print("----------------------reporte---------------")
#tenemos mas de 10 manzanas?
hay_manzanas = manzanas > 10
print("¿hay mas de 10 manzanas?",hay_manzanas)

#nos quedamos sin stock en la bodega
sin_stock = manzanas == 0
print(f"¿nos quedamos sin stock en la bodega?",{sin_stock})
#comparacion de nombres de productos
producto_buscado =  "Manzana"

es_manzana = producto_nombre == producto_buscado
print(f"¿el producto buscado esta en bodega?" [es_manzana])