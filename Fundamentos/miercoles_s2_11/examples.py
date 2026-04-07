# nombre = input("Ingrese su nombre:")
# edad = int(input("Ingrse su edad:")) 
# precio_bebidax= 300

# if (edad >= 18): 
#     print("Puede ingresar")
#     entrada_tipo = str(input("ingrese su tipo de entrada (General/VIP):"))
    
#     if(entrada_tipo == "VIP"):
#         print("Puede ingresar AREA VIP)")
#         bebida = str(input("Deseas la bebida X?:"))
#         if(bebida == "si"):
#             presupuesto = int(input("Cual es su presupuesto de esta noche?:"))
#             if(presupuesto >= precio_bebidax):
#                     cambio = presupuesto - precio_bebidax
#                     print(f"compra aceptada", "su cambio es", cambio)
#             else:
#                 print("sin dinero suficiente.")        
            
#         else:
#             print("gracias por su respuesta.")
#     else:
#         print("No Puede ingresar al area VIP.")

# else:
#     print("No Puede ingresar")
#//////////////////////////////////////////////

# nombre = input("Ingrese su nombre:")
promedio_final = int(input("Ingrese su Promedio:"))
ingreso = int(input("Ingrese sus ingresos familiares mensual:"))
# materias = int(input("cantidad de materias aprobas?:"))

if (promedio_final < 70): 
    print("Beca no aprobada")

elif promedio_final >= 70 <= 84 and ingreso <= 400000:
    
	print("recibes beca parcial")

#elif promedio_final < 85 and ingreso <= 400000:
    #print("Elegible")

else:
    print("Beca  aprobada")
