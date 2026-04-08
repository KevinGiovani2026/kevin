class Termostato:
    def __init__(self):
        self.__temperatura = 28
    
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nueva_temperatura):
        if nueva_temperatura < 22:
            print("Temperatura Invalida")
        else:
            self.__temperatura = nueva_temperatura

objeto1 = Termostato()
print(f"Temperatura actual: {objeto1.temperatura}")
objeto1.temperatura = int(input("Ingrese la nueva temperatura: "))
print(f"Temperatura actual: {objeto1.temperatura}")

# while nueva_temperatura < 10 or nueva_temperatura > 25:  meterle el while
#       print('Temperatura invalida')
#       nueva_temperatura = int(input('Ingrese una temperatura valida: '))
#     self.__temperatura = nueva_temperatura
#     print(f'Actualizando temperatura... \nNueva temperatura: {self.__temperatura}')

