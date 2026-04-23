# class Motor:
#     def __init__(self, caballos_fuerza):
#         self. caballos = caballos_fuerza
#         self.encendido = False


#     def arrancar(self):
#         self.encendido = True
#         print("Encendiendo el motor")

    
# class Auto:
#     def __init__(self, marca, modelo,potencia_motor):
#         self.marca = marca
#         self.modelo = modelo

#         self.corazon_mecanico = Motor(potencia_motor)

#     def encender_auto(self):
#         print("girando la llave para encender..")

#         self.corazon_mecanico.arrancar()

# mi_carro = Auto("toyota", "corolla", 200)
# mi_carro.encender_auto()

#/////////////////////////////////////////////////

# class Bateria:
#     def __init__(self,porcentaje = 100):
#         self.porcentaje = porcentaje

#     def descargar (self):
#         if self.porcentaje > 0:
#             self.porcentaje -= 10
#         print(f"Bateria al {self.porcentaje}%")

        

# class Celular:
#     def __init__(self, marca):
#         self.marca = marca
#         self.energia = Bateria()

#     def usar_app(self):
#         print("abriendo aplicacion")
        
#         self.energia.descargar()

# celular1 = Celular("Xiaomi")
# celular1.usar_app()
# celular1.usar_app()

#///////////////////////////////////
#si funciona
class Procesador:
    def __init__(self,modelo):
        self.modelo = modelo

class TarjetaVideo:
    def __init__(self, memoria_gb):
        self.memoria = memoria_gb

class Computadora:
    def __init__(self, cpu_externo, gpu_externa):
        self.cpu = cpu_externo
        self.gpu = gpu_externa

    def mostrar_especificaciones(self):
        print("Especificaciones del Equipo:")

        print(f" - Procesador: {self.cpu.modelo}")
        print(f"- Graficos: {self.gpu.memoria} GB de video")


intel_i9 = Procesador("Intel Core i9 14900k")
nvidia_x = TarjetaVideo(24)

pc_gamer = Computadora(intel_i9, nvidia_x)

pc_gamer.mostrar_especificaciones()

#////////////////////////////////////////////////////////////

class Estudiante:
    def __init__(self, nombre,carnet):
        self.nombre = nombre
        self.carnet = carnet

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.lista_matriculados = []

    def matricular(self,nuevo_estudiante):
        self.lista_matriculados.append(nuevo_estudiante)

        print(f"Sistema: {nuevo_estudiante.nombre} matriculado con exito")

    def pasar_lista(self):
        for alumno in self.lista_matriculados:
            print(f" - {alumno.carnet}: {alumno.nombre}")



alumno1 = Estudiante("Luis" ,"A001")
alumno2 = Estudiante("Keyla","A0002")

curso_poo = Curso("POO")

curso_poo.matricular(alumno1)
curso_poo.matricular(alumno2)
 
curso_poo.pasar_lista()

curso_poo.lista_matriculados[0].nombre = "Luis Fernando" 
curso_poo.pasar_lista()