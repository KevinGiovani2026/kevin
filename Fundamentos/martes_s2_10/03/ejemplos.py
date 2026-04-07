#ejemplo 1
#dinero = 1000
#precio = 750

#if dinero >= precio:
#    print ("venta aprobada")


#print("===SISTEMA DE SEGURIDAD DE LA BODEGA===") #ejemplo 2

#clave_ingresada = input("ingrese la clave de seguridad:")
#clave_correcta= "1234"

#if clave_ingresada == clave_correcta:
#	print("clave correcta. Acceso permitido.")
#	print("Bienvenido a la bodega super segura")

#print("fin del programa")

opcion = input("seleccione (1-3):")
match opcion:
	case"1":
		print("registrando producto..")
	case "2":
		print("mostrando inventario...")
	case "3":
		print("Saliendo...")
		break
	case _:
		print("opcion invalido")
