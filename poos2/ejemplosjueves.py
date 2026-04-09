# archivo_prueba = open("newtemajueves.txt", "a")

# archivo_prueba.write("Hoy aprendi a escribir en un archivo")

# archivo_prueba.close()


with open("registro.txt","w") as archivo_prueba:
     archivo_prueba.write("Hoy aprendi a escribir en un archivo")


# contador = 0   #si funciona 
# with open("registro.txt","r") as archivo_prueba:
#     for linea in archivo_prueba:
#         print(linea.strip)
#         contador += 1
# print(f"Total de líneas: {contador}")   