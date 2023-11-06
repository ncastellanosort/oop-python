#encapsular codigo para que no sea usado

class ClasePrivado:
    def __init__(self):
        #se entiendo que no _con la barra baja
        self._atributoPrivado = 'valor'



#para acceder con getter y setter
#son metodos

#nivel covencion
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #getters
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    #metodos privados
    def __hablar(self):
        print('hola')

    #acceder a ellos con el name mangling
    
    #setters
    def set_nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


nicolas = Persona('nicolas', 12)

#obtener el nombre
nombre = nicolas.get_nombre()
print(nombre)

#setear un nuevo nombre
nicolas.set_nombre('felipe')
nombre = nicolas.get_nombre()
print(nombre)

#metodo con name mangling
#nicolas._Persona__hablar()
