#pedir informacion
cajas_disponibles= int(input("cantidad de cajas:"))
if cajas_disponibles> 20:
	print("Inventario saludable")

elif (cajas_disponibles>= 1) and (cajas_disponibles<=20):
    #(edad >= 18) and (entrada == "si")
	print("ALERTA, hacer pedido al proveedor.")

else:
    print("URGENTE: producto agotado")

