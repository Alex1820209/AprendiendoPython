numero1 =input("Numero 1: ")
numero2=input("Numero 2: ")
#se muestran los valores
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #se mete a esta funcion si los capturados son iguales
    print(salida.format(numero1, numero2,"Los numeros son iguales"))
else:
    #se usa un if dentro de otro (condiciones anidadas)
    #si los numeros son iguales.
    if numero1>numero2:
        #se hace si el primer valor es mayor al segundo
        print(salida.format(numero1, numero2, "el mayor es el primero"))
    else:
        #si no es asi el segundo es mayor
        print(salida.format(numero1, numero2, "el mayor es el segundo"))

