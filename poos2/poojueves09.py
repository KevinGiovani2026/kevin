class CuentaBancaria:
    tasa_interes_global = 0.05
    cantidad_cuentas_creadas = 0

    def __init__(self, nombre_titular):
        self.__titular = nombre_titular
        self.__saldo = 0.0
        CuentaBancaria.cantidad_cuentas_creadas += 1

    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nuevo_titular):
       
        if nuevo_titular == "":
            print("Nombre de titular inválido")
        else:
            self.__titular = nuevo_titular

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes")
        elif cantidad <= 0:
            print("Cantidad a retirar debe ser positiva")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

    def proyectar_interes(self):
        ganancia = self.__saldo * CuentaBancaria.tasa_interes_global
        print(f"Ganancia proyectada por intereses: {ganancia}")
    
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        # recordatorio, usar cls y no self en los métodos de clase
        cls.tasa_interes_global = nueva_tasa

        print("\n[COMUNICADO OFICIAL] El banco ha cambiado la tasa de interés")  


cuenta1 = CuentaBancaria("sofia")
cuenta2 = CuentaBancaria("diego") 

print(f"Total de clientes activos: {CuentaBancaria.cantidad_cuentas_creadas}")

cuenta1.depositar(10000)
cuenta2.depositar(50000)

cuenta1.retirar(5000)
cuenta2.retirar(15000)


cuenta1.proyectar_interes()


CuentaBancaria.modificar_tasa_interes(0.10)

cuenta1.proyectar_interes()

cuenta1.titular = "" 



#//////////////////////////////
# @classmethod
# def cambiar_impuesto(cls, nuevo_tasa):
#     if nuevo_tasa <= 0:
#         cls.tasa_interes_global = nuevo_tasa 
#         print(f"[SISTEMA] Tasa de interés cambiada a: {cls.tasa_interes_global}")