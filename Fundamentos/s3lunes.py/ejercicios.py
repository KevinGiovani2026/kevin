# def mensaje_bienvenida ():
#     print("Bienvenido al sistema de ventas esperamos que tenga un excelente compra.")

# mensaje_bienvenida()

# #//////////////////////////
# nombre = input("Cual es su nombre:?")

# def saludar_cliente(nombre):
#     print("hola", nombre, "bienvenido al gimnasio")

# saludar_cliente(nombre)

#///////////////////////////////////////////////
# def calculo_total(precio,cantidad):
#     total = precio * cantidad

#     return total

#     precio = float(input("Ingrese el precio"))

#     cantidad = float(input("ingrese la cantidad:"))

#     total_pagar = calculo_total(precio,cantidad)
#     print("El total a pagar es:,{total_pagar}")



#////////////////////////////////////////
# def calcular_total(precio, cantidad): #si funciona
#      total = precio * cantidad
#      return total

# precio = float(input("Ingrese el precio del producto: "))
# cantidad = int(input("Ingrese la cantidad comprada: "))
# total_final = calcular_total(precio, cantidad)
# print("El total a pagar es:", total_final)


def saludo(nombre):
     print(f"¿Hola, {nombre}?")

def calcular_fichas(dinero):
     fichas = dinero // 500
     vuelto = dinero % 500  
     return fichas,vuelto

    
def menu():
    print("1. Comprar fichas")
    print("2. Salir")

    opcion = int(input("seleccione una opcion"))
    while opcion != 2:
        nombre=input("Cual es su nombre?:")
        saludo(nombre)
        dinero = int(input("Ingrese su dinero disponible:"))

        
        if dinero >= 500:
            fichas_total, cambio = calcular_fichas(dinero)
            print("cantidad fichas",fichas_total)
            print("Tu vuelto es", cambio)
            break
        else:
             print("no puede comprar monedas")
            
menu()

    
