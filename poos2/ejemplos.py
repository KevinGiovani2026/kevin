class SondaMonitoreo: #crea los objetos
    def __init__(self, modelo, ubicacion):
        self.modelo_sonda = modelo
        self.ubicacion_sonda = ubicacion
        self.energia_sonda = 100
        self.activado = False

    def cambio_estado(self): #si el televisor esta apagado lo enciende
        if self.activado == False:
            self.activado = True
            print("Sonda monitoreo Activado")
        else:
            self.activado = False
            print("sonda monitoreo apagado")

    def realizar_lectura(self):
        if self.activado == True:
            print(f"Lectura exitosa. Temperatura registrada en {self.ubicacion_sonda}")
        else:
            print("Sonda apagada enciendala primero")

mi_sonda = SondaMonitoreo("SS-2026","Laboratorio Central" )

mi_sonda.realizar_lectura()
mi_sonda.cambio_estado()
mi_sonda.realizar_lectura()