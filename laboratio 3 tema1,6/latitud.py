#Diocelina Sierra Martinez
#01/112/16
import math as r
def cos(ang):
    return r.cos(r.radians(ang))
def sin(ang):
    return r.sin(r.radians(ang))
def acos(ang):
    return r.acos(r.radians(acos))
a1=float(input ("Introduzca latitud: "))
b1=float(input ("Introduzca longitud: "))
a2=float(input ("Introduzca latitud: "))
b2=float(input ("Introduzca longitud: "))
def distancia(x1,y1,x2,y2):
    a=6371.01*r.acos(r.sin(x1)*r.sin(x2)+r.cos(x1)*r.cos(x2)*r.cos(y1-y2))
    print a
distancia(a1,b2,a1,b2)
