class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print(f'hola soy {self.nombre} y estoy hablando')

class Artista(Persona):
    def __init__(self,nombre, edad, instrumento):
        super().__init__(nombre,edad)
        self.instrumento = instrumento

    def habilidad(self):
        print(f'toco: {self.instrumento}')

#hereda de persona y de artista
class ArtistaEmpleado(Artista):
    def __init__(self,nombre,edad,instrumento,empresa):
        super().__init__(nombre,edad,instrumento)

    #como es herencia multiple
    #ya no pasamos el super
    #si no pasamos el nombre de la clase
        # Persona.__init__(self,nombre,edad)
        # Artista.__init__(self,instrumento)
        self.empresa = empresa
    
    #heredar metodo habilidad de clase Artista
    def presentarse(self):
        return f'{super().habilidad()}'

    def palabras(self):
        return f'{super().hablar()}'

    #super siempre es acceder a clase padre
    #self es dentro de la misma clase

andres = ArtistaEmpleado('andres', 17, 'saxofon', 'coca cola')

andres.presentarse()
andres.palabras()




