class Temperatura:
    def __init__(self):
        self.__grados = 20

    @property
    def grados(self):
        return self.__grados

    @grados.setter
    def grados (self, nuevo_grado):
        if nuevo_grado <0:
            print("Temperatura Invalida")
        else:
            self.__grados = nuevo_grado

clima = Temperatura()

print(clima.grados)
clima.grados = 50
print(clima.grados)

##miniEjercicio

class Empleado:
    def __init__(self):
        self.__salario = 300

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario (self, nuevo_salario):
        if nuevo_salario <300:
            print("Cantidad no valida")
        else:
            self.__salario = nuevo_salario

salary = Empleado()

print(salary.salario)
salary.salario = 200
print(salary.salario)