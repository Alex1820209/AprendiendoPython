for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #si el print no tiene argumento salta una linea
    print()
    #se pone un "for" dentro de otro
    for j in range (1,11):
        #i guarda el numero base y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #al conclui con las iteracones indicadas se ejecuta este codido,
        #que es un salto de linea
        print()