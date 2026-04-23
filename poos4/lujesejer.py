class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def marcar_como_prestado(self):
        self.prestado = True

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, id_libro, titulo, autor):
        nuevo_libro = Libro(id_libro, titulo, autor)
        self.libros.append(nuevo_libro)

    def obtener_libros(self):
        return self.libros

    def buscar_libro_por_id(self, id_libro):
        for libro in self.libros:
            if libro.id == id_libro:
                return libro
        return None
    
class VistaBiblioteca:
    @staticmethod
    def mostrar_menu():
        print("\n--- GESTIÓN DE BIBLIOTECA ---")
        print("1. Agregar Libro")
        print("2. Listar Libros")
        print("3. Prestar Libro")
        print("4. Salir")
        return input("Seleccione una opción: ")
    
    @staticmethod
    def solicitar_datos_libro():
        id_libro = input("ID del libro: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        return id_libro, titulo, autor
    
    @staticmethod
    def mostrar_lista_libros(libros):
        print("\nID | TÍTULO | AUTOR | ESTADO")
        for libro in libros:
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.id} | {libro.titulo} | {libro.autor} | {estado}")


    @staticmethod
    def buscar_id():
        return input("Ingrese el ID del libro: ")
    
    @staticmethod
    def mostrar_mensaje( mensaje):
        print(f"\n>> {mensaje}")


class ControladorBiblioteca:
    def __init__(self):
        self.modelo = Biblioteca()
        self.vista = VistaBiblioteca()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            
            if opcion == "1":
                id_l, tit, aut = self.vista.solicitar_datos_libro()
                self.modelo.agregar_libro(id_l, tit, aut)
                self.vista.mostrar_mensaje("Libro agregado con éxito.")
                
            elif opcion == "2":
                libros = self.modelo.obtener_libros()
                self.vista.mostrar_lista_libros(libros)
                
            elif opcion == "3":
                id_l = self.vista.buscar_id()
                libro = self.modelo.buscar_libro_por_id(id_l)
                if libro:
                    libro.marcar_como_prestado()
                    self.vista.mostrar_mensaje("Libro prestado correctamente.")
                else:
                    self.vista.mostrar_mensaje("Error: Libro no encontrado.")
                    
            elif opcion == "4":
                self.vista.mostrar_mensaje("Saliendo de la aplicación.")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida.")

if __name__ == "__main__":
    controlador = ControladorBiblioteca()
    controlador.ejecutar()





 

