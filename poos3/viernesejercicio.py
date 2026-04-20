from abc import ABC, abstractmethod

class PersonalMedico(ABC):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    @abstractmethod
    def realizar_labor(self):
        pass

class Doctor(PersonalMedico):

    def __init__ (self, nombre, especialidad):
        super().__init__(nombre,especialidad) 

    def realizar_labor(self):
        print("Realizando diagnostico especializado")

    def atender_paciente(self, objeto_paciente):
        diagnostico = input("Ingrese diagnostico")
        objeto_paciente.paciente_historial.agregar_observacion(diagnostico)

        dosis = int(input("Ingrese La dosis"))
        objeto_paciente.salud_paciente += dosis

class Enfermero(PersonalMedico):

    def __init__(self, nombre, especialidad):
        super().__init__(nombre,especialidad)
        
    def realizar_labor(self):
        print("Aplicando Cuidados y revisando signos Vitales")

#/////////////////////////// fase composicion
class HistorialClinico:
    def __init__(self):
        self.observaciones = []

    def agregar_observacion(self, nueva_observacion):
        self.observaciones.append(nueva_observacion)

    def __str__(self):
        return str(self.observaciones)
        
    def mostrar_notas(self):
        for notes in self.observaciones:
            print(notes)
           
class Paciente:
    def __init__(self, nombre_paciente, edad, salud = 15):
        self.nombre_paciente = nombre_paciente
        self.edad_paciente = edad
        self.salud_paciente = salud
        self.paciente_historial = HistorialClinico()

    def estado_critico(self):
        if self.salud_paciente <= 0:
            self.salud_paciente = 0
        
        elif self.salud_paciente < 20:
            print("Paciente en estado crítico")
            
        elif self.salud_paciente >= 100:
            self.salud_paciente = 100
            print("Paciente totalmente recuperado")
            
        else:
            print("Paciente en recuperación")


doctor1 = Doctor("Gregory House", "Diagnóstico")
enfermero1 = Enfermero("Juan Pérez", "Cuidados Intensivos")
paciente1 = Paciente("Willson", 45, salud=10)


print(f"Atendiendo a {paciente1.nombre_paciente}...")
doctor1.atender_paciente(paciente1)

print("--- Reporte Médico ---")
paciente1.paciente_historial.mostrar_notas()
paciente1.estado_critico()
print(f"Nivel de salud actual: {paciente1.salud_paciente}")

enfermero1.realizar_labor()









