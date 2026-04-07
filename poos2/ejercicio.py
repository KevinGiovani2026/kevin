# class LibroFisico(): #si sirve todo 
#     def __init__(self, titulo, author):
#         self.titulo = titulo
#         self.author = author
#         self.disponible = True

#     def prestar_libro(self):
#         if self.disponible == False:
#             print(f"El libro {self.titulo} no esta disponible")

#         else:
#             print(f"Libro {self.titulo} disponible! Libro prestado")
#             self.disponible = False

# libro1 = LibroFisico("El Quijote", "Miguel de Cervantes")
# libro2 = LibroFisico("Cien a;os de soledad", "Gabriel Garcia Marquez")

# libro1.prestar_libro()
# libro1.prestar_libro()

#///////////////////////////////////////////////
#Control DE Temperatura

class AireAcondicionado():
    def __init__ (self,nombre):
        self.maquina_nombre = nombre
        self.temperatura = 24

    def bajar_temp(self, grados):
        if self.temperatura -grados >= 16: 
            self.temperatura -= grados
            print(f"↓ {self.maquina_nombre} , {self.temperatura} grados")

        else: 
            print("Error suba la temperatura")

maquina1 = AireAcondicionado("Maquina 1") 

maquina1.bajar_temp(10)

