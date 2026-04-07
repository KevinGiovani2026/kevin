# ==========================================
# Ejercicio 1
# ==========================================
nombre = (input("Nombre:"))
edad= int(input("Edad:"))
inscripcion = str(input("inscripcion confirmada?:"))

if (edad >= 15 and inscripcion == "si"):
	print("Participante autorizado para ingresar. ")
else:
	print("No puede ingresar")


# ==========================================
# Ejercicio 2
# ==========================================

bateria= int(input("Ingrese el porcentaje de bateria:"))
if bateria <= 20:
	print("Conecte el cargador")
else:
    print("Bateria suficiente")

# ==========================================
# Ejercicio 3
# ==========================================

peso= float(input("Peso del Paquete:"))
if peso < 1:
	print("Paquete liviano ")

elif (peso>= 1 and peso<=5):
	print("Paquete estandar.")

else:
    print("Paquete pesado")

# ==========================================
# Ejercicio 4
# ==========================================


color= (input("ingrese el color del semaforo:"))
if color == "verde":
	print("Avanzar")

if color == "amarillo": 
	print("Precaucion.")

if color == "rojo":
    print("Detenerse")

# ==========================================
# Ejercicio 5
# ==========================================

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrse su edad:")) 
precio_bebidax= 300

if (edad >= 18): 
    print("Puede ingresar")
    entrada_tipo = str(input("ingrese su tipo de entrada (General/VIP):"))
    
    if(entrada_tipo == "VIP"):
        print("Puede ingresar AREA VIP)")
        bebida = str(input("Deseas la bebida X?:"))
        if(bebida == "si"):
            presupuesto = int(input("Cual es su presupuesto de esta noche?:"))
            if(presupuesto >= precio_bebidax):
                    cambio = presupuesto - precio_bebidax
                    print(f"compra aceptada", "su cambio es", cambio)
            else:
                print("sin dinero suficiente.")        
            
        else:
            print("gracias por su respuesta.")
    else:
        print("No Puede ingresar al area VIP.")

else:
    print("No Puede ingresar")

# ==========================================
# Ejercicio 5
# ==========================================

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrse su edad:")) 
precio_bebidax= 300

if (edad >= 18): 
    print("Puede ingresar")
    entrada_tipo = str(input("ingrese su tipo de entrada (General/VIP):"))
    
    if(entrada_tipo == "VIP"):
        print("Puede ingresar AREA VIP)")
        bebida = str(input("Deseas la bebida X?:"))
        if(bebida == "si"):
            presupuesto = int(input("Cual es su presupuesto de esta noche?:"))
            if(presupuesto >= precio_bebidax):
                    cambio = presupuesto - precio_bebidax
                    print(f"compra aceptada", "su cambio es", cambio)
            else:
                print("sin dinero suficiente.")        
            
        else:
            print("gracias por su respuesta.")
    else:
        print("No Puede ingresar al area VIP.")

else:
    print("No Puede ingresar")

# ==========================================
# Ejercicio 6
# ==========================================





