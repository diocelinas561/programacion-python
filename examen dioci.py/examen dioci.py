#Diocelina Sierra Martinez
#14/12/16
palabra=input("ingrese palabra: " )
print palabra
i=0
alreves = ""
j= len(palabra)-1
while(i <= j):
    alreves = alreves + palabra[j]
    j=j-1
print ( "palabra alreves es:", alreves)
