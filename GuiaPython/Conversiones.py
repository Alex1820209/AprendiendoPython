#se declara una variable str
numero="1234"
#Se muestra el tipo de variable
print(type(numero))

#Aqui se hace el cambio de la cadena al
#equivalaente en int
numero=int(numero)

#Se muestra en pantalla la nueva clase de variable
print(type(numero))

#se declara un str con met sustitucion y donde iran los
#valors usando format
salida="el numero utilizado es: {}"

#SE muestra el resultado Las llaves seran donde se haga
#la sustitucion
print(salida.format(numero))