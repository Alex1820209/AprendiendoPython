#Python usa librerias que se nombran con modules
#para usar un module lo primero que se hace es importarse
#Se utiliza la instruccion "import"
import random
#se define una variable float y se asigana un valor
Numero1=float(24.9)

#se utiliza una funcion (conjunto de instrucciones)
#se declaran con def. todo el codigo a la derecha
#es parte de la funcion
def MiFuncion():
    #se convierte a float el numero generado
    #por random.randrange() (solo funciona si se importa
    # el modulo "random")
    Numero2=float(random.randrange(1,20))
    #se utiliza sustitucion para mostrar resultados
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(Numero1,Numero2,Numero1+Numero2))

#se ejecuta la funcion
MiFuncion()