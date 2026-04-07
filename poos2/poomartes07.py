class RegistroAcademico:
    def __init__(self, nombre_alumno, nota_inicial):
        self.nombre = nombre_alumno
        #atributo privado
        self.__nota = nota_inicial
        self.cuenta_activa = True

    def get_nota(self):
        return self.__nota

    def bloquear_cuenta(self):
        self.cuenta_activa = False
        
    def set_nota(self, nueva_nota):
        if self.cuenta_activa == False:
            print("La cuenta está bloqueada. No se puede modificar la nota.")
            return -2
        if 0 < nueva_nota < 100:
            self.__nota = nueva_nota
            return 1
        else:
            print("Nota inválida. Debe estar entre 0 y 100.")
            return -1