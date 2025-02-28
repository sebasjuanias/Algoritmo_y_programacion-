#entrada
consumo_acutal=(int(input("Consumo actual")))
consumo_anterior=(int(input("consumo anterior")))

if(0<=consumo_acutal<=100):
    kw=4600
elif(101<=consumo_acutal<=300):
    kw=80000
elif(301<=consumo_acutal<=500):
    kw=100000
else:
    (120000)
    
consumo_real=consumo_anterior - consumo_acutal
costo_factura=consumo_real*kw

print("Monto a pagar:", abs(costo_factura))
 
