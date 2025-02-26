#entradas
categoria=(int(input("Categoria")))
Salario=(int(input("Salario")))

if(categoria==1):
    aumento=0.10
elif(categoria==2):
    aumento=0.15
elif(categoria==3):
    aumento=0.20
elif(categoria==4):
    aumento=0.40
elif(categoria==5):
    aumento=0.60
else:
    print("No esta en inguna categoria de la 1-5")
    
monto_aumento=(Salario*aumento)
Salario_nuevo=(Salario+monto_aumento)

print("Categoria:", categoria)
print("salario bruto", Salario_nuevo)
    
