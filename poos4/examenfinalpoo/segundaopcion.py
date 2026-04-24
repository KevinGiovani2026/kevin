from abc import ABC, abstractmethod
class NaveEspacial(ABC):
    contador_naves = 0

    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.__energia = 100
        self.__escudo = 100
        self.estado = "Activo"
        NaveEspacial.contador_naves += 1

    @abstractmethod
    def mision_especializada(self):
        pass

    @property
    def energia(self): 
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if valor < 0: self.__energia = 0
        elif valor > 100: self.__energia = 100
        else: self.__energia = valor
        if self.__energia == 0: self.estado = "Vulnerable"

    @property
    def escudo(self): 
        return self.__escudo

    @escudo.setter
    def escudo(self, valor):
        if valor < 0: self.__escudo = 0
        elif valor > 100: self.__escudo = 100
        else: self.__escudo = valor
        if self.__escudo == 0: self.estado = "Vulnerable"

    def __lt__(self, other): 
        return self.__energia < other.energia

    def __str__(self):
        return f"Nave: {self.nombre} | Energía: {self.__energia}% | Escudo: {self.__escudo}% | Estado: {self.estado}"

# --- CLASES HIJAS ---
class NaveCombate(NaveEspacial):
    def __init__(self, nombre, codigo, potencia):
        super().__init__(nombre, codigo)
        self.potencia = potencia

    def mision_especializada(self,consumo):
        self.energia -= consumo
        return f"Resultado: Desplegando ataque con potencia {self.potencia}."

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, codigo, energia, capacidad):
        super().__init__(nombre, codigo, energia)
        self.capacidad = capacidad

    def mision_especializada(self):
        return "Transportando suministros críticos."
    
class InterceptorHibrido(NaveCombate, NaveCarga):
    def mision_especializada(self):
        return "Combate y transporte simultáneo activado."


hangar = []

print(">>> ESTACIÓN AETHELGARD ACTIVADA <<<")

while True:
    print("\n1. Registrar | 2. Misión | 3. Comparar | 4. Stat | 5. Salir")
    
    try:
        opcion = int(input("Seleccione acción: "))
        
        if opcion == 1:
            nombre = input("Nombre: ")
            codigo = input("Código: ")
            potencia = int(input("Potencia: "))
            nueva_nave = NaveCombate(nombre, codigo, potencia)
            hangar.append(nueva_nave)
            print("Éxito. Total naves:", NaveEspacial.contador_naves)
            
        elif opcion == 2:
            nave_numero = int(input("Índice de nave: "))
            consumo = int(input("Energía a consumir: "))
            hangar[nave_numero - 1].mision_especializada(consumo)
            
        elif opcion == 3:
            nave_numero1 = int(input("Índice nave 1: ")) - 1
            nave_numero2 = int(input("Índice nave 2: ")) - 1
            if hangar[nave_numero1] < hangar[nave_numero2]:
                print(f"{hangar[nave_numero1].nombre} tiene menos energía.")
            else:
                print("La primera nave tiene más o igual energía.")
                
        elif opcion == 4:
            for i in range(len(hangar)):    
                print(f"[{i}] {hangar[i]}")
                
        elif opcion == 5:
            break
            
    except (ValueError):
        print("[ADVERTENCIA] Entrada inválida o índice inexistente.")
