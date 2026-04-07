class DronVigilancia:
    def __init__(self, nombre, modelo):
        self.nombre_dron = nombre
        self.modelo_dron = modelo
        self.bateria_dron = 100
        self.current_status = "En Tierra"

    def despegar(self):
        if self.current_status == "En Tierra":
            if self.bateria_dron >= 25:
                self.current_status = "En vuelo"
            else:
                print("Error: Low Battery")
        else:
            print("ERROR: EL DRON YA ESTA EN VUELO")


    def patrullaje(self):
        if self.current_status == "En vuelo":
            self.current_status = "patrullando"
            self.bateria_dron -= 30
            if self.bateria_dron < 0:
                self.bateria_dron = 0

        else:
            print("Error. El dron debe estar en vuelo")
            


    # def recargar(self):
    #     pass

    def mostrar_estado(self):
        print(f"NOMBRE: {self.nombre_dron} MODELO: {self.modelo_dron} NIVEL DE BATERIA:{self.bateria_dron} ESTADO: {self.current_status}")

print("INICIANDO SISTEMA SKYWATCH")

usuario_nombre = input("Ingrese nombre del dron:")
usuario_modelo = input("Ingrese el modelo:")

dron = DronVigilancia(usuario_nombre, usuario_modelo)

#dron.mostrar_estado()

while True:
    dron.mostrar_estado()
    opcion = int(input(" {1} :DESPEGAR \n {2}: PATRULLAJE \n {3}: RECARGAR: \n {4}: SALIR \n Elija una opcion:" ))
    
    if opcion == 1:
        dron.despegar()
    
    elif opcion ==2:
        dron.patrullaje()
    elif opcion == 3:
        dron.recargar()

    elif opcion == 4:
        print("saliendo")
        break
    else:
        print("opcion invalida")