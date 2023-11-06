class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print('esta estudiando')

nombre = input('nombre del estudiante: ')
edad = input('edad del estudiante: ')
grado = input('grado del estudiante: ')

estudiante = Estudiante(nombre, edad, grado)

print(f'''
        nombre: {estudiante.nombre}\n
        edad: {estudiante.edad}\n
        grado: {estudiante.grado}\n

      ''')

estudiar = input()

if estudiar.lower() == 'estudiar':
    estudiante.estudiar()
                 
