class SensorPresion:
    total_lecturas = 0
    LIMITE_PELIGRO = 200

    def __init__(self, nombre, presion):
        self.nombre = nombre
        self.__presion = presion
        SensorPresion.total_lecturas += 1

    @property
    def presion(self):
        return self.__presion
    
    @presion.setter
    def presion(self, nuevo_valor):
        if nuevo_valor <= 0:
            print("Valor de presión invalido")
        else:
            self.__presion = nuevo_valor
            print(f"Nuevo valor correctamente asignado: {self.__presion}")


    
with open("registros.txt") as archivo:
    lineas = archivo.readlines()
    valores1 = lineas[0:2]
    valores2 = lineas[2:4]
    valores3 = lineas[4:6]
    valores4 = lineas[6:8]

lista_en_pares = []

for i in valores1:
    lista_en_pares.append(i.strip())

for i in valores2:
    lista_en_pares.append(i.strip())

for i in valores3:
    lista_en_pares.append(i.strip())

for i in valores4   :
    lista_en_pares.append(i.strip())


    #print(i.strip())
print(lista_en_pares)
#with open(resultado)