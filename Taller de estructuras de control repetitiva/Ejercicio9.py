MinPromedio = 0
MaxPromedio = 0
NumeroDeEstudiantes = int(input("Cuantos estudiantes Tiene: "))
Contador = 0
while Contador<NumeroDeEstudiantes:
    Contador = Contador + 1 
    Nombre = input("Ingrese nombres completos del estudiante: ")
    Puntaje = float(input("Ingrese el puntaje del estudiante: "))
    Nombres.append(Nombre)
    Puntajes.append(Puntaje) 
PunMax = max(Puntajes)
PuntajeMax = [x for x in Puntajes if x == PunMax]
PunMin = min(Puntajes)
PuntajeMin = [x for x in Puntajes if x == PunMin]
NomMax = Nombres[Puntajes.index(PunMax)]
NombreMax = [x for x in Nombres if x == NomMax]
NomMin = Nombres[Puntajes.index(PunMin)]
NombreMin = [x for x in Nombres if x == NomMin]
Promedio = sum(Puntajes)/len(Puntajes)
for i in Puntajes:
    if i <Promedio:
        MinPromedio = MinPromedio + 1
    else:
        MaxPromedio = MaxPromedio + 1    
print(f"El Estudiante con Nota mas alta es: {NombreMax}")
print(f"El Estudiante con Nota mas baja es: {NombreMin}")
print(f"La nota mas alta es: {PuntajeMax}")
print(f"La nota mas baja es: {PuntajeMin}")  
print(f"El promedio de nota es: {Promedio}")
print(f"Estudiante por arriba del promedio es: {(MaxPromedio/NumeroDeEstudiantes)*100}")
print(f"Estudiante por abajo del promedio es: {(MinPromedio/NumeroDeEstudiantes)*100}")