#entradas
Departamento1=int(input("Departamento 1"))
Departamento2=int(input("Departamento 2"))
Departamento3=int(input("Departamento 3"))

salario_bruto=int(input("Salario bruto"))
#caja negra
Ventas_totales=Departamento1+Departamento2+Departamento3
Incentivo=Ventas_totales*0.33

if(Departamento1>Incentivo):
    print((salario_bruto*0.2)+salario_bruto)
elif(Departamento2>Incentivo):
    print((salario_bruto*0.2)+salario_bruto)
elif(Ventas_totales>Incentivo):
    print((salario_bruto*0.2)+salario_bruto)  
else:0

    
    