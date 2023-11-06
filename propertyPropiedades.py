#setters, getters y deleters
#decorador reservado

#@property
#esto es un getter rey

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    #aca usamos el @property para no usar la convencion
    @property
    #ya se le puede quitar el get_nombre
    def nombre(self):
        return self.__nombre
    
    #aca se usa el nombre de la funcion del getter y se agrega el metodo.setter
    @nombre.setter 
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
   
    #literal para eliminar
    @nombre.deleter 
    def nombre(self):
        del self.__nombre

nico = Persona('nicolas', 12)

#el nombre ahora se puede setear sin el set_nombre()
nico.nombre = 'felipe'

#nico.nombre es el get
nombre = nico.nombre

#eliminar
#del nico.nombre
print(nombre)


