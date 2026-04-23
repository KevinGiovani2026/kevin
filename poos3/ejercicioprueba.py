from abc import ABC, abstractmethod

class VehiculoTerrestre(ABC):
    @abstractmethod
    def conducir_ruedas(self):
        pass

class VehiculoAcuatico(ABC):
    @abstractmethod
    def encender_helices(self):
        pass

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def conducir_ruedas(self):
        print("Activando traccion 4x4 en terreno Rocoso.")
    
    def encender_helices(self):
        print("Retrayendo ruedas y activando propulsion acuatica.")

class AutoComun(VehiculoTerrestre):
    def conducir_ruedas(self):
        print("Conduciendo normal.")

class Lancha(VehiculoAcuatico):
    def encender_helices(self):
        print("Navegacion normal.")

auto1=AutoComun()

lancha1=Lancha()

autolancha1=VehiculoAnfibio()

ruta_terrestre = [auto1, autolancha1]

for vehiculo in ruta_terrestre:
    vehiculo.conducir_ruedas()

ruta_acuatica = [lancha1, autolancha1]

for vehiculo in ruta_acuatica:
    vehiculo.encender_helices()
    