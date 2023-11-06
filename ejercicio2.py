class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f'nombre: {self.nombre}\n edad: {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar(self):
        print(f' nombre: {self.nombre}\n edad: {self.edad}\n grado: {self.grado}')


estudiante1 = Estudiante('nicolas', 15, 11)

estudiante1.mostrar()
