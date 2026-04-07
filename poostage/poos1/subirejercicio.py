class CajaRegistradora:
    def cobrar_producto(self):
        precio_producto = float(input("Ingrese el precio del producto:"))
        self.dinero_acumulado += precio_producto
        print(f"Cobro exitoso: Acumulado {self.dinero_acumulado}")

    def imprimir_cierre_turno(self):
        print(f"El cajero encargado: {self.cajero_asignado} \t Total Recaudado: {self.dinero_acumulado} ")

caja_express = CajaRegistradora()
caja_express.cajero_asignado = "Kevin"
caja_express.dinero_acumulado = 0


caja_express.cobrar_producto()
caja_express.cobrar_producto()
caja_express.imprimir_cierre_turno()