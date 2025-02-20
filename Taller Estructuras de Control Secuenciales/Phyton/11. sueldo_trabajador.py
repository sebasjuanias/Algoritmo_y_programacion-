#entradas
nombre=str(input("Nombre de empleado"))
horas=int(input("Numero de Horas"))
valor_hora=int(input("Valor hora"))
horas_extras=int(input("Horas extras"))
hijos=int(input("Numero de hijos"))
#caja negra
valor_horaextra=(horas_extras*0.25)+horas
Sueldo_base=horas*valor_hora
pago_extra=horas_extras*(horas*1.25)
asignaciones=pago_extra+250000+(173000*hijos)+180000
deducciones=(Sueldo_base*0.05)+(Sueldo_base*0.02)+(Sueldo_base*0.07)
sueldo_neto=(Sueldo_base+asignaciones)-deducciones
#salidas
print("Asignaciones: ", asignaciones)
print("Deducciones: ", deducciones)
print("Sueldo neto: ", sueldo_neto)