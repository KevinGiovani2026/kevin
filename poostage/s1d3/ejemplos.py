# class Libro:
#     def __init__ (self,titulo_ingresado, autor_ingresado):
        
#         self.titulo = titulo_ingresado
#         self.autor = autor_ingresado


# libro_nuevo = Libro("el principito ")

#//////////////////////////////////////////////////

class Alcancia:
    def __init__(self):
        self.dinero_guardado = 0

    def depositar_dinero(self, cantidad):
        self.dinero_guardado += cantidad 

    def mostrar_ahorros(self):
        print(f"el dinero ahorrado es:{self.dinero_guardado}")

mi_cochinito = Alcancia()

mi_cochinito.depositar_dinero(500)

mi_cochinito.mostrar_ahorros()

#/////////////////////////////////////////

class Cliente:

    def __init__(self, nombre, pais = "Guatemala"): # exepcion ya se definio el parametro
        self.nombre = nombre
        self.pais = pais


client1 = Cliente("Diego","Costa Rica")

Cliente2 = Cliente("Kevin")

#///////////////////////////////////////////

class Televisor:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False # estado unicial: apagado
        self.volumen = 10 # estado inicial 10

    def presionar_boton_encendido(self):

        if self.encendido == False:
            self.encendido = True
            print(f"El Televisor {self.marca} se ha encendido. ")

        else:
            sefl.encendido = False
            print(f"El televisro {self,marca} se ha apagado.")

    def subir_volumen(self):
        if self.encendido:
            self.volumen +=1 
            print(f"El volumen actual: {self.volumen} ")

        else:
            print("error: no se puede subir el volumen. El televisor esta apagado. enciendalo   ")
