#entradas
parciales=float(input(" Nota de parciales "))
examen_final=float(input(" Nota de examen final "))
trabajo_final=float(input(" Nota de trabajo final "))
#caja negra
porceparcial=(parciales*0.55)
porcexamen=(examen_final*0.30)
porctrabajo=(trabajo_final*0.15)
#salidas
print("nota final", porctrabajo+porcexamen+porceparcial)
