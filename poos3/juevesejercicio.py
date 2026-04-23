class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'"{self.titulo}" escrito por {self.autor}'

class Biblioteca:
    def __init__(self,nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal

        self.catalogo = []

    def agregar_libro(self, nuevo_libro):
        self.catalogo.append(nuevo_libro)

    def mostrar_inventario(self):
        print(f"Nombre de la sucursal: {self.nombre_sucursal}")
        for librito in self.catalogo:
            print(librito)
            #print(f" - {librito.titulo}: {librito.autor}") cual es mejor?

libro1 = Libro("Rebelión en la granja", "George Orwell")
libro2 = Libro("Orgullo y prejuicio","Jane Austen")
libro3 = Libro("Los miserables", "Victor Hugo")

biblio1 = Biblioteca("Biblioteca Central")


biblio1.agregar_libro(libro1)
biblio1.agregar_libro(libro2)
biblio1.agregar_libro(libro3)

biblio1.mostrar_inventario()

#####Si funciona########################

