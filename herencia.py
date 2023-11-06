class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def hablar(self):
        print('hola')

#dentro de los parentesis se pone la clase que va a heredar
#pass sirve para crear algo, pero algo vacio

class Estudiante(Persona):

    #pass

    #en el constructor le pasamos los atributos que queramos agregar 
    #la clase hija

    #aca se va a agregar el grado y el colegio
    def __init__(self, nombre, apellido, edad, grado, colegio):
        #va a heredar lo que esta dentro de parentesis de la clase padre
        #dentro del super no va el self
        super().__init__(nombre,apellido,edad)
        self.grado = grado
        self.colegio = colegio

    #podemos sobreescribir el metodo
    def hablar(self):
        print('hola sobreescrito')


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, salario, cargo):
        super().__init__(nombre,apellido,edad)
        self.salario = salario
        self.cargo = cargo

#ya se hereda todo lo de la clase Persona
carlitos = Estudiante('carlitos', 'perez', 19, 11, 'albert einstein')
anderson = Empleado('anderson', 'castro', 24, 1400, 'administrador')

print(carlitos.nombre)
#tambien hereda los metodos
lista = []

lista.append()

