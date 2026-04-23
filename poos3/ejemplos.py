class Persona:
    def __init__(self, nombre): 
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre_ingresado, nota_ingresada): 
        super().__init__(nombre_ingresado)
        self.nota = nota_ingresada


    def mostrar_info(self):
        print(f"Hola, mi nombre es {self.nombre} y mi nota es: {self.nota}")

estudiante1 = Estudiante("Juan", 8.5)

estudiante1.mostrar_info()

#////////////////////////////////

class PersonaMayor():
    def Saludar(Self):
        print("Buenas tardes como se encuentra el dia de hoy es un placer saludarlo")

class Adolecente(PersonaMayor):
    def Saludar(Self):
        print("Hola, todo bien?")

senor = PersonaMayor()
chico = Adolecente()

senor.Saludar()
chico.Saludar()
#///////////////////////////////////////

### ejmplo simulacion de la granja

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Animal: {self.nombre}"

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido generico")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | el Perro hace: Guau, Guauuuuu")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | el gato hace: Miau, Miauuuuu")

class Pato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | el pato hace: Cuac, Cuaauuuuu")


animal1 = Perro("Pochiberto")
animal2 = Gato("Porfirio")
animal3 = Pato("Pancracio")

lista_granja = [animal1,animal2]
lista_granja.append(animal3) 

animal_desconocido = Animal("Extraterrestre")

lista_granja.append(animal_desconocido)

#print(lista_granja) investigar

print(animal_desconocido)

for animal in lista_granja:
        #animal.hacer_sonido()
        print(animal)


#//////////////////////////////////////////////////////

class EmpleadoBase:
    def iniciar_rutina(self):
        print("1. Llego a la oficina a las 8.00 am")
        print("2. Planifico mi dia")
        print("3. REviso mis correos electronicos")

    def monto_salario(self):
        return 3000



class Programador(EmpleadoBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()
    # mas 1 cambio
        print("4. Escribo codigo y Resuelvo problemas tecnicos")    

