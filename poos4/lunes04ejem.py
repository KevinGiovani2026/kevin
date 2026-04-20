
from abc import ABC, abstractmethod
class Personaje(ABC):
    @abstractmethod
    def atacar(self):
        pass

class Guerrero(Personaje):
        
    def atacar(self): return "ataca con espada"

class Mago(Personaje):
    def atacar(self): return "Ataca con magia"


#Fabrica (el corazon del patron) 

class FabricaPersonajes:
    @staticmethod
    def crear_personaje(tipo):

        tipo = tipo.lower()

        if tipo == "guerrero":
            return Guerrero()
        
        elif tipo == "mago":
            return Mago()
        
        else:
            raise ValueError(f"La fabrica no sabe crear: {tipo}")
        
try:
    eleccion = input("Que personaje deseas: Guerrero/ Mago : ")
    heroe = FabricaPersonajes.crear_personaje(eleccion)
    print (heroe.atacar())

except ValueError as error:
    print(error)

#///////////////////////////////////////////////////////////
#MODELO
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False


#VISTA
class VistaTarea:
    @staticmethod
    def mostrar_menu():
        print("\n1. Agregar tarea\n2. Mostrar Tarea\n3 Salir")
        return input("opcion:")
    
    @staticmethod
    def mostrar_lista(lista):
        print("\nLista de tareas:")

        for tarea in lista:
            print(f"{tarea.descripcion} esta en estado: {tarea.completada}")

    @staticmethod
    def solicitar_descripcion():
        return input("Descripcion de la Tarea")
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)


#CONTROLADOR    
class ControladorTareas:
    def __init__(self):
        self.tareas = []
        self.vista = VistaTarea()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                descripcion = self.vista.solicitar_descripcion()
                tarea = Tarea(descripcion)
                self.tareas.append(tarea)
            elif opcion == "2":
                self.vista.mostrar_lista(self.tareas)

            elif opcion == "3":
                self.vista.mostrar_mensaje()
                break


