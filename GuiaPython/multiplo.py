#se captura un numero y se guarda y convierte en int
numero=int(input("dame un numero entero:"))
#se alamcena en valores booleanos
#si el residuo es cero significa que el numero es multiplo
EsMultiplo3=((numero%3)==0)
EsMultiplo5=((numero%5)==0)
EsMultiplo7=((numero%7)==00)
#al usar AND se resulve como verdadero solo si todas las condiciones
#son verdaderas. cuando se usa or, se resulve por verdadero solo si
#una de ellas lo es. los parentesis sirven para que python haga las
#primeras dos condiciones juntas y la tercera
# es independiente
if((EsMultiplo3 and EsMultiplo5) or EsMultiplo7):
    print("Correcto")
else:
    print("incorrecto")

