class CajaRegistradora:
    def mostrar_money(self):
        print(f"Dinero : {self.dinero}")
    def procesar_venta(self):
        self.dinero = self.dinero + 500
        print("Venta procesada")

caja_registradora_1 = CajaRegistradora()

caja_registradora_1.dinero = 1500

caja_registradora_1.mostrar_money()

caja_registradora_1.procesar_venta()

caja_registradora_1.mostrar_money()