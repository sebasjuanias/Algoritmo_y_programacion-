estudiantes = {}
aprobados = []
suspendidos = [] 
contador = 0
while contador < 10:
    numero = input("Numero del estudiante: ")
    nombre = input("Nombre del estudiante: ").capitalize()
    nota = float(input("La nota del estudiante es: "))
    estudiantes[numero] = {"nombre": nombre, "nota": nota}  
    contador += 1



for numero, datos in estudiantes.items():
    if datos["nota"] >= 3.0:
        aprobados.append(datos["nombre"])
    else:
        suspendidos.append(datos["nombre"])  

total_notas = sum(float(datos["nota"]) for datos in estudiantes.values())  
media = total_notas / len(estudiantes)

print(aprobados, "Aprobaron")
print(suspendidos, "Suspendieron") 
print("Esta es la nota media:", media)
print(estudiantes)