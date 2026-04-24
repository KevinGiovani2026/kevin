from abc import ABC, abstractmethod

# 1. Definición de la Clase Base Abstracta (El ADN de la Flota)
class NaveEspacial(ABC):
    contador_global = 0

    def __init__(self, nombre, codigo, energia):
        self.nombre = nombre
        self.codigo = codigo
        self._energia = energia  # Atributo privado
        self._combustible = 100  # Atributo privado
        self._escudos_nivel = 100     # Atributo privado
        self.estado_escudo = "Activo"
        self.nucleo = NucleoEnergia()
        NaveEspacial.contador_global += 1

    @abstractmethod
    def mision_especializada(self):
        pass

    # 3. Decoradores para manejo de atributos privados (Encapsulamiento)
    @property
    def combustible(self):
        return self._combustible

    @combustible.setter
    def combustible(self, nivel_combustible):
        if 0 <= nivel_combustible <= 100:
            self._combustible = nivel_combustible
        else:
            raise ValueError("Nivel invalido.")

    @property
    def escudos_nivel(self):
        return self._escudos_nivel

    @escudos_nivel.setter
    def escudos(self, capacidad):
        if capacidad < 0:
            self._escudos_nivel = 0
        else:
            self._escudos_nivel = capacidad
            
        if self._escudos_nivel == 0:
            self.estado_escudo = "Vulnerable"

    # 4. Sobrecarga de operadores
    def __lt__(self, other):
        return self._energia < other._energia

    def __str__(self):
        return f"Nave {self.nombre} ({self.codigo}) - Energía: {self._energia}"

# Componente Interno
class NucleoEnergia:
    def gestionar_consumo(self, energia):
        return f"Consumiendo {energia} unidades de energía del núcleo."

# Ramas Principales
class NaveCombate(NaveEspacial):
    def mision_especializada(self):
        return "Disparando láseres de alta potencia."
    

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, codigo, energia, capacidad):
        super().__init__(nombre, codigo, energia)
        self.capacidad = capacidad

    def mision_especializada(self):
        return "Transportando suministros críticos."

    def __add__(self, other):
        if isinstance(other, NaveCarga):
            return NaveCarga("Fusionada", "MIX", 0, self.capacidad + other.capacidad)
        raise TypeError("Solo se pueden fusionar naves de carga.")

# Nave de Élite
class InterceptorHibrido(NaveCombate, NaveCarga):
    def mision_especializada(self):
        return "Combate y transporte simultáneo activado."

# 2. Estación Espacial (Relación 1 a Muchos)
class EstacionEspacial:
    def __init__(self):
        self.flota = []

    def inyectar_nave(self, nave):
        self.flota.append(nave)

# ... (Aquí irían tus clases definidas anteriormente)

# 1. Instanciamos la estación fuera de cualquier función
mi_estacion = EstacionEspacial()

# 2. Ciclo principal directo
print("Bienvenido al sistema de control de la estación")

while True:
    try:
        print("\n1. Registrar Nave")
        print("2. Ver Flota")
        print("3. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            # Aquí iría la lógica para pedir datos y usar mi_estacion.inyectar_nave()
            nombre = input("Nombre de la nave: ")
            # ... resto de inputs
            print("Nave registrada exitosamente.")
            
        elif opcion == 2:
            for nave in mi_estacion.flota:
                print(nave)
                
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
            
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
