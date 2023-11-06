#misma funcion diferente finalidad

class Gato:
    def sonido(self):
        print('miau')


class Perro:
    def sonido(self):
        print("guau")


#polimorfismo de funcion

def hacerSonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacerSonido(gato)

#otro polimorfismo
print(gato.sonido())
