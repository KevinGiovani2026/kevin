class Cajero:
    def __init__(self, nombre , i_d,):
        self.nombre_cajero = nombre
        self.id_cajero = i_d
        self.dinero_en_caja = 0

    def cobrar_articulo(self, cantidad):
        self.dinero_en_caja += cantidad 

    def mostrar_dinero_caja(self):
        print(f"Dinero en caja:{self.dinero_en_caja}\tnombre:{self.nombre_cajero}\tID:{self.id_cajero}")

cajero_uno = Cajero("cajero_genesis", "C0004")

cajero_uno.cobrar_articulo(150)
cajero_uno.cobrar_articulo(3700)

cajero_dos = Cajero("cajero_terminal","A0001")
cajero_dos.cobrar_articulo(300)
cajero_uno.mostrar_dinero_caja()
cajero_dos.mostrar_dinero_caja()