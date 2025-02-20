#entradas
descuento=float(input("porcentaje de descuento"))
compra=int(input("valor de compra"))
#caja negra
valor_final=compra*descuento
#salidas
print("Pago de compra", compra-valor_final, " COP ")
