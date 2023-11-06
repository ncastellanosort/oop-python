#usar pascal case para definir el nombre de la clase

class NombreClase():
    nombre = 'nicolas'
    apellido = 'castellanos'


#instanciar un objeto
yo = NombreClase()
print(yo)
yo2 = NombreClase()
yo3 = NombreClase()

#acceder a los atributos
print(NombreClase.apellido)

#editar un atributo ya establecido
yo.nombre = 'felipe'

#atributos son variables de una clase
#crear una clase como normalmente hago en POO
class Celular:
    #este es el constructor de la clase
    #el self hace referencia a si mismo
    #luego le pasamos lo que quiera que tenga
    def __init__(self, marca, modelo, camara):
        #aca vamos a definir los atributos
        #es como el this de poo
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    #metodos
    #con self uno de los parametros es el mismo objeto
    def llamar(self):
        print(f'esta llamando desde un: {self.modelo}')

apple = Celular('apple', '12 pro', '12MP')
print(apple.marca)

apple.llamar()









