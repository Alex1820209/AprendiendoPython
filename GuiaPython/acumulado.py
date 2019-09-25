#se declaran las variables peor con tipo explicito
acumulado=int(0)
numero=str("")
#al colocar true como condicion de while se forma un ciclo
#eset sera infinito hasta que de forma explicita se
#utilice la instruccion "break"

while True:
    numero=input("dame un numero entero: ")
    if numero=="":
        #si no se coloca ningun numero muestra en pantalla ya sale
        print("vacio. salida del programa")
    else:
        #si se proporciono valor, acumulado = acumulado + numero
        #se realiza el calculo usando suma incluyente (+-)
        acumulado+=int(numero)
        salida="monto acumulado: {}"
        print(salida.format(acumulado))
