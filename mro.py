#metodo de resolucion de orden
#orden en el que busca metodos y atributos

class A:
    def hablar(self):
        print('Hola desde A')


class B(A):
    def hablar(self):
        print('Hola desde B')


class C(A):
    def hablar(self):
        print('Hola desde C')



class D(B,C):
    def hablar(self):
        print('Hola desde D')


objeto = D()

objeto.hablar()

#primer clase heredada es b, primero es b, la segunda es C, despues va C y si no encuentra el metodo en ninguna va a A

#.funcion para ver # %% 
print(D.mro())

#otra funcion para ejecutar metodos desde cierta clase

objeto2 = D()
#desde que clase.hablar y dentro el objeto
C.hablar(objeto2)
