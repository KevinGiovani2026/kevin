class TarjetaVIP:
    def mostrar_puntos(self):
        print(f"Total Puntos:{self.puntos}" )

    def sumar_puntos(self):
        self.puntos = self.puntos + 50
        print("Felicidades obtuviste 50 pts")


tarjeta_carlos = TarjetaVIP()
tarjeta_carlos.puntos = 100

tarjeta_carlos.mostrar_puntos()
tarjeta_carlos.sumar_puntos()
tarjeta_carlos.mostrar_puntos()
