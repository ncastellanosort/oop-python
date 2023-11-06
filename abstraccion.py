#manejar la complejidad
#interfaz simple que oculte lo complejo
class Auto:
    def __init__(self):
        self.estado = 'apagado'

    def encender(self):
        self.estado = 'encendido'
        print('el carro esta encendido')


    def conducir(self):
        if self.estado == 'apagado':
            self.encender()
            print('el auto esta encendido')


carro = Auto()
carro.conducir()

#clases abstractas para tener abstraccion
