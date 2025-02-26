#Entradas
sueldo=int(input("Salario"))
#caja negra
if(sueldo<900000):
    print("Nuevo salario", (sueldo*0.15)+sueldo)
else:
    sueldo>900000
    print("Nuevo salario", (sueldo*0.12)+sueldo)


