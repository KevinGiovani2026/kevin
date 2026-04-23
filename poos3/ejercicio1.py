class PersonajeBase:
    def caminar(self):
        print("El Personaje esta avanzando por el mapa")

    def descansar(self):
        print("El personaje esta recuperando Energia")

class Mago(PersonajeBase):
    def lanzar_hechizo(self):
        print("!El mago lanza una bola de fuego!") 


class Guerrero(PersonajeBase):
    def bloquar_ataque(self):
        print("El Guerrero levanta su escudo de metal")

#////////////////////////////////////////////////////////////////
mi_mago = Mago()
mi_guerrero = Guerrero()

print("Acciones mi mago")
mi_mago.caminar()
mi_mago.descansar()
mi_mago.lanzar_hechizo()

print("Acciones mi Guerrero")
mi_guerrero.caminar()
mi_guerrero.descansar()
mi_guerrero.bloquar_ataque()

#mi_guerrero.lanzar_hechizo()  solo prueba se supone que de error

class Vehiculos:
    cantidad_vehiculos = 0
    tarifa_diaria = 100

    def __init__(self, placa, marca, modelo,kilo_salidad):
         
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = kilo_salidad

        Vehiculos.cantidad_vehiculos += 1

    @classmethod
    def cambiar_tarifia(cls, nueva_tarifa):
        cls.impuesto_iva = nueva_tarifa

    @property
    def kilometraje(self): # ()
         return self.__kilometraje 
    
# --- PRUEBAS ---
# Crear vehículos
v1 = Vehiculos("P123ABC", "Toyota", "Corolla", 50000)
v2 = Vehiculos("P456DEF", "Honda", "Civic", 30000)

# Ver cantidad de vehículos creados
print("Cantidad de vehículos:", Vehiculos.cantidad_vehiculos)

# Acceder a atributos
print("Placa v1:", v1.placa)
print("Marca v2:", v2.marca)

# Usar la propiedad kilometraje
print("Kilometraje v1:", v1.kilometraje)

# Cambiar la tarifa diaria
Vehiculos.cambiar_tarifa(150)
print("Nueva tarifa diaria:", Vehiculos.tarifa_diaria)

    







