#Diocelina sierra martinez
#22/11/16
#ejercicio  5
peso=input("calcular indice de masa corporalen kg:")
haltura=input("calcular la haltura en m:")
indice=p/h**h
print "indice de masa corpora es: ", indice
if indice<16.0:
    print "de acuerdo atu indice tines, delgadez"
elif indice>=16 and indice<=16.99:
    print "delgadez moderada"
elif indice>=17 and indice<=18.49:
    print "delgadez leve"
elif indice<=18.5 and indice<=24.99:
    print "normal"
elif indice<=25:
    print "sobrepeso"
elif indice<=30:
    print "obesidad"
elif indice<=40:
    print "obesidad morbida"
