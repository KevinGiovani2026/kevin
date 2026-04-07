# match
# opcion = input("seleccione (1-3):")
# match opcion:
# 	case"1":
# 		print("registrando producto..")
# 	case "2":
# 		print("mostrando inventario...")
# 	case "3":
# 		print("Saliendo...")
# 	case _:
# 		print("opcion invalido")
#/////////////////////////////////////////////////

# while True: #si sirve
#     x = int(input("Ingrese la cantidad:")) 
#     if x <= 0:
#         print("programa terminado")
#     elif x < 100:
#         print("Insufieciente")
#     elif x <300:
#         print("regular")
#     elif x <600:
#         print("Idoneo")
#     else:
#         print("sobreproduccion")

#lista_productos = [0,0,0]
def mostrar_nombre(nombre):
    print("mi nombre es:" + nombre)
mostrar_nombre("kevin")
#/////////////////////////////////

while True:
    codigo_producto = input("¿ingrese el codigo/fin para terminar: ")
    if codigo_producto == "fin":
        print("Adiós!")
        break


    codigo_producto = int(codigo_producto)
    if codigo_producto == 0 or codigo_producto > 3:
        print("Codigo invalido")

#////////////////////////////////////////

saludo = ("Bienvenidos")
digito_first=(saludo[1:6])
print (digito_first)