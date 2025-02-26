#entradas
compra=int(input("Compra"))
nombre_cliente=str(input("Nombre cliente"))

if(compra<50000):
    descuento=0.0
elif(compra<=100000):
    descuento=0.05
elif(compra<=700000):
    descuento=0.11
elif(compra<=1500000):
    descuento=0.18
else:
    descuento=0.25
Valor_decuento=(compra*descuento)
Valor_a_pagar=(compra - Valor_decuento)

#salidas
print("Nombre cliente", nombre_cliente)
print("Compra", compra)
print("Monto a Pagar:", Valor_a_pagar)
print("Valor de Descuento", Valor_decuento)

