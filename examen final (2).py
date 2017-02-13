#09/02/2017
#examen final computacion 1
#Diocelina Sierra
#crear una lista de numeros de telefono que cuando inpirmas te de regrese la lista pero de mayor a menor


import csv
with open('excel1.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        lista=row[2]
        print row[2]
