def saludo():
     print("hola como estas?")

def despedida():
    print("adios, que tengas un buen dia")


saludo()
despedida()
saludo()


def menu():
    print("1.saludar")
    print("2.despedida")
    print("3.salir")

    opcion = input("seleccione una opcion")
    
    while  True:
        match opcion:
            case "1":
                saludo()
            case "2":
                despedida()
            case "3":
                print("saliendo")
                break
            case _:
                print("opcion no valida")
        opcion = input("seleccione una opcion")
menu()