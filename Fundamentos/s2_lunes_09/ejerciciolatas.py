print("Bievenido a la tienda")
print("="*25)
cantidad_latas = int(input("ingrese cantidad de latas de atun:"))
latas_por_estantes = int(input("ingrese la cantidad de latas en cada estante:"))

#division entera
valor1 = cantidad_latas//latas_por_estantes
valor2 = cantidad_latas%latas_por_estantes
#print("cantidad de estantes:", (valor1)) opcion 1
print("%30s, %10d" % ("cantidad de estantes",valor1) ) #opcion 2
print("latas Restantes:", (valor2))