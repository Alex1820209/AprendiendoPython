numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
#"for" ejecuta un bloque de codifo con un numero determinado
#numero de veces, cuando se pide que recorra un rnado fe valores. Elsegundo parametro 
#de range no se inclute en la serie de valores. aqui seria del 1 al 10
for i in range(1,11):
    #i va variando a cada interacion
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))