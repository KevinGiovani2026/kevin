# import random as rd
# #//// hacerlo funcionar reviarlo y corrgirlo 
# class SableDeLUZ:
#     def __init__(self, energia = 100):
#         self.energia = energia

#     def __recargar__(self, carga_energia = 10):
#         nueva_energia =  self.energia + carga_energia
#         return SableDeLUZ(nueva_energia)
    
#     def __sub__(self, otro_sable):
#         return self.energia - otro_sable.energia
    
#     def mostrar_energia(self):
#         print(f'La energia del sable es: {self.energia}')

    
# sable1 = SableDeLUZ()

# sable1.__recargar__()
# sable1.mostrar_energia()
# #No funciona el metodo recargar, no se actualiza la energia del sable,
#  revisar y corregir el codigo para que funcione correctamente

from abc import ABC, abstractmethod

class Trabajdor(ABC):
    
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(Trabajdor):
    def realizar_tarea(self):
        print("El ingeniero está diseñando Planos.")
class Medico(Trabajdor):
    def realizar_tarea(self):
        pass

inge1=Ingeniero()
inge1.realizar_tarea()

medico1=Medico()
medico1.realizar_tarea()

