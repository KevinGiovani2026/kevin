from abc import ABC, abstractmethod

class Trabajdor(ABC):
    
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(Trabajdor):
    def realizar_tarea(self):
        print("El ingeniero está diseñando Planos.")
class Medico(Trabajdor):
    def realizar_tarea(self):
        pass

inge1=Ingeniero()
inge1.realizar_tarea()

medico1=Medico()
medico1.realizar_tarea()