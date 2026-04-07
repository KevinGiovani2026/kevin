class Producto:
    pass


articulo_1 = Producto()
articulo_2 = Producto()

articulo_1.nombre = "camiseta"
articulo_1.precio = 19.99
articulo_1.cantidad = 10

print(f" nombre: {articulo_1.nombre} precion: {articulo_1.precio} cantidad: {articulo_1.cantidad}" )

#///////////////////////////////////////////////////////////

class Empleado:
    pass

empleado_1 = Empleado()  #si funciona

empleado_1.nombre = "kevin"
empleado_1.cargo = "Gerente" 
empleado_1.salario = 10000

empleado_2 = Empleado()

empleado_2.nombre = "Giovani"
empleado_2.cargo = "cajero"
empleado_2.salario = 5000

empleado_3 = Empleado()

empleado_3.nombre = "Thomas"
empleado_3.cargo = "Bodeguero"
empleado_3.salario = 4900

print(f"Buen dia mi informacion personal es : {empleado_1.nombre}\t Cargo: {empleado_1.cargo} Salario: {empleado_1.salario}")
print(f"Buen dia mi informacion personal es: {empleado_2.nombre} \t  Cargo: {empleado_2.cargo} Salario: {empleado_2.salario}")
print(f"Buen dia mi informacion personal es: {empleado_3.nombre} \t Cargo: {empleado_3.cargo} Salario: {empleado_3.salario}")

#/////////////////////////////////////////////////////

class Colaborador:
    def saludar_cliente(self):
        print(f"hola me llamo  {self.nombre}, bienvenido a nuestra tienda:")

colaborador_1 = Colaborador()
colaborador_2 = Colaborador()

colaborador_1.nombre = "Kevin"
colaborador_2.nombre = "Diego"

colaborador_1.saludar_cliente()
colaborador_2.saludar_cliente()
