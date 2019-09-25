entrada=input()
print(type(entrada))
#se verifica con la variable booleana
#si lo capturado es digito y si se encuentra un punto
#indicaria que se trata de un numero con decimales (float)
#si find retorna -1 quiere decir que lo buscado
#no se encontro, si EsEntero es igual a verdadero
#lo capturado es entero
EsEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (EsEntero):
    #Lineas que se ejecutaran si la condicion es verdadera(true)
    print("dato entero. ¡muy bien!")
else:
    #las lineas que se ejecutaran si la condicion es falsa (False)
    print("El dato no es entero. intentar nuevamente.")