class Arma:
    def __init__(self, nombre, puntos_danio):
        self.nombre = nombre
        self.puntos_danio = puntos_danio

class Guerrero:
    def __init__(self, nombre, arma_equipada):
        self.nombre_guerrero = nombre
        self.arma = arma_equipada

    def atacar(self):
        print(f"{self.nombre_guerrero} ataca con {self.arma.nombre} causando {self.arma.puntos_danio} danio")


arma1 = Arma("Espada Larga",50)

guerrero1 = Guerrero("Rambo", arma1)

guerrero1.atacar()
