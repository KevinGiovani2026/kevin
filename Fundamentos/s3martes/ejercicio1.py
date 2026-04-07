lista_invitados = []
def agregar_invitado(lista_invitados):
    for i in range(10):
        nombre = input("Ingrese los nombres:")
        lista_invitados.append(nombre)
    return lista_invitados
    #print(lista_invitados)

def mostrar_lista(lista_invitados):
    for invitados in lista_invitados:   
        print (invitados)

def buscar_invitado(nombre, lista_invitados):
    if nombre in lista_invitados:
        return True
    else:
        return False
    
lista_invitados = agregar_invitado(lista_invitados)
mostrar_lista(lista_invitados)

nombre_a_buscar = input("\nIngrese el nombre a buscar: ")
if buscar_invitado(nombre_a_buscar, lista_invitados):
    print(f"{nombre_a_buscar} está en la lista.")
else:
    print(f"{nombre_a_buscar} no está en la lista.")

def mostrar_menu():
    print("\n--- MENÚ DEL EVENTO ---")
    print("2. Registrar nuevo invitado")
    print("3. Ver lista completa")


#agregar_invitado(lista_invitados)
#mostrar_lista(lista_invitados)
# lista_invitados.append ("kevin")
# print(lista_invitados)   # Debería mostrar ["Ana", "Luis"]