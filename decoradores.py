#recibe una funcion, le agrega nueva funcion y la devuelve otra vez
#agrega una funcionalidad antes y despues

def decorador(funcion):
    def funcion_modificada():
        print('antes de llamar a la funcion')
        funcion()
        print('despues de llamar a la funcion')
    return funcion_modificada

#def saludo():
#   print('hola nicolas')

#guardarla en una variable
#la variable ahora va a ser una funcion


#saludo_modificado = decorador(saludo)
#saludo_modificado()

#para no hacer lo de guardar la variable y todo eso
#@el nombre de la funcion
@decorador  
def saludo():
    #la funcion que se le va a pasar
    print('hola nicolas')

#como se va a llamar?
#esta ya es la funcion modificada
#sirve para hacer validaciones
saludo()
#que decorador estamos aplicandole a tal funcion
#agarra una funcion y le agrega mas funcionalidad, antes y o despues de ejecutarla, y la devuelve
