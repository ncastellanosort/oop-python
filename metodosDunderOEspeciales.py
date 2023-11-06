#tienen un nombre especial reservado
#inician con __nombre__


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #devolver como string
    def __str__(self):
        return f'Persona(nombre = {self.nombre}, edad = {self.edad})'
    
    def __repr__(self):
        return f'Persona({self.nombre}, {self.edad})'
    
    #modificar la suma, para sumar objetos
    def __add__(self, otro):
        nuevoValor = self.edad + otro.edad
        return Persona(self.nombre + '-' +otro.nombre, nuevoValor)


nicolas = Persona('nicolas', 12)

#devuelve en si como el constructor de la clase STR string
#devuelve una representacion del objeto
print(nicolas)

#devuelve el valor de los atributos del constructor
#devuelve el objeto en si
repre = repr(nicolas)
print(repre)

#sobrecarga de operadores

carlos = Persona('carlos', 12)
andres = Persona('andres', 19)

nuevaPersona = carlos + andres
#practicamente estamos sumando edades y nombres, devolviendolos como str

#tambien se puede acceder a los atributos de este nuevo objeto
#nuevaPersona.edad R/: 31
#round() para quitar decimales

print(nuevaPersona)
