def saludo(nombre):
     print("hola como estas?")
     print(f"¿como estas, {nombre}?")

def despedida():
    print("adios, que tengas un buen dia")

def calculo_impuestos(precio):
    impuesto = precio * 0.15
    total = precio + impuesto

    return total

#saludo(nombre)
#despedida()
#saludo(nombre)


def menu():
    print("1. Saludo")
    print("2.despedida")
    print("3. Calcular impuesto")
    print("4.salir")

    opcion = input("seleccione una opcion")
    nombre = input("ingrese su nombre")
    while  True:
        match opcion:
            case "1":
                saludo(nombre)
            case "2":
                despedida()
            case "3":
                precio = float(input("ingrese el precio:"))
                precio_total = calculo_impuestos(precio)

                print(f"el precio total con impuestos es: {prec}")
            case "4":
                print("saliendo")
                break
            case _:
                print("opcion no valida")
        opcion = input("seleccione una opcion")
menu()