# class Tienda: #Ejemplo de como acceder a atributos globales

#     impuesto_iva = 0.13

#     def __init__(self, productos):
#         self.__productos = productos

#     @classmethod
#     def cambiar_impuesto(cls, nuevo_impuesto):
#         cls.impuesto_iva = nuevo_impuesto

# Tienda.cambiar_impuesto(0.15)  #Ejemplo importante


class RegistroVisitantes: # si funciona
    total_personas = 0

    def __init__(self, nombre_visitante):
        self.nombre = nombre_visitante
        RegistroVisitantes.total_personas += 1

        print(f" [{self.nombre} ha ingresado]. La pizarra global ahora  marca:{RegistroVisitantes.total_personas}")
       

Persona1 = RegistroVisitantes("Juan")
Persona2 = RegistroVisitantes("Maria")  
Persona3 = RegistroVisitantes("Pedro")

#/////////////////////////////////////// Ejercicio 2

class EmpleadoTienda:
    #atributo de clase
    sueldo_minimo = 300
    cantidad_empleado = 0

    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id = id_empleado
        EmpleadoTienda.cantidad_empleado += 1

    @classmethod
    def aumento_nacional(cls, nuevo_sueldo):
        cls.sueldo_minimo_legal = nuevo_salario

        print("\n[Comunicado oficial] El gobierno ha cambiado el sueldo minimo" )
    def mostrar_recibo(self):
        print(f"empleado {self.id}: {self.nombre} | Pago a Recibir: {EmpleadoTienda.sueldo_minimo_legal}")


print("\n -- SISTEMA DE PLANILLA  NACIONAL -- ")

#CREAMOS DOS PERONSONAS

empleado1 = EmpleadoTienda("Juan", 1) 
empleado2 = EmpleadoTienda("Maria", 2)

print(f" Total de empleado: {EmpleadoTienda.cantidad_empleado}")


