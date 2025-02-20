#entradas
examen_mate=float(input("Examen de matematicas"))
tarea_mate=float(input("Tarea de matematicas"))
examen_fisica=float(input("Examen de fisica"))
tarea_fisica=float(input("Tarea de fisica"))
examen_quimica=float(input("Examen de quimica"))
tarea_quimica=float(input("Tarea de quimica"))
#caja negra
promedio_matematicas=(examen_mate*0.9)+(tarea_mate*0.1)
promedio_fisica=(examen_fisica*0.8)+(tarea_fisica*0.2)
promedio_quimica=(examen_quimica*0.85)+(tarea_quimica*0.15)
#salidas
print("Promedio Matematicas", promedio_matematicas)
print("Promedio fisica", promedio_fisica)
print("Promedio Quimica", promedio_quimica)