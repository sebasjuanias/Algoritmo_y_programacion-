#entradas
sueldo_base=int(input("ingresar sueldo base"))
venta1=int(input("ingresar venta 1"))
venta2=int(input("ingresar venta 2"))
venta3=int(input("ingresar venta 3"))
#caja negra
venta_total=venta1+venta2+venta3
porcentaje_ventas=(venta_total*0.10)
#salidas
print("valor de comision", porcentaje_ventas)
print("inngreso total", sueldo_base+porcentaje_ventas)
