#no podemos instanciarla
#plantilla para crear clases a partir de la plantilla
#modelo o plantilla
#implementar un metodo: definir como va a funcionar
#diferentes implementaciones con una unica plantilla
#contrato: heredar de la clase abstracta me obliga a obligarme a tener los metodos que 
#puse como abstractos implementados
#aseguran el polimorfismo

#siempre importar
from abc import ABC, abstractmethod

#que la clase persona herede de la clase ABC

class Persona(ABC):
    #una propiedad para que sea una clase abstracta
    @abstractmethod
    def __init__(self,nombre,edad,actividad):
        self.nombre = nombre
        self.edad = edad
        self.actividad = actividad

    #el metodo abstracto
    #metodo sin implementacion (con pass)
    @abstractmethod
    def hacerActividad(self):
        pass
    
    #un metodo normal
    def presentarse(self):
        print(f'hola soy {self.nombre}, tengo {self.edad}')

class Estudiante(Persona):
    def __init__(self,nombre,edad,actividad,):
        super().__init__(nombre,edad,actividad)
    
    #metodo sobreescrito gracias al metodo sin implementacion
    def hacerActividad(self):
        print(f'estoy estudiando: {self.actividad}')

class Empleado(Persona):
    def __init__(self,nombre,edad,actividad):
        super().__init__(nombre,edad,actividad)

    def hacerActividad(self):
        print(f'estoy trabajando en la actividad de: {self.actividad}')

#instanciar el objeto
nicolas = Estudiante('nicolas', 12, 'programacion')
felipe = Empleado('felipe', 25, 'barrer')

#usar los metodos
nicolas.hacerActividad()
felipe.hacerActividad()

