#entradas
horas=int(input("Horas trabajadas"))
precio_hora=int(input("Precio hora"))
#caja negra
salario_bruto=(horas*precio_hora)
salario_neto=(salario_bruto*0.2)
#salidas
print("Salario neto", salario_bruto-salario_neto, "COP")
