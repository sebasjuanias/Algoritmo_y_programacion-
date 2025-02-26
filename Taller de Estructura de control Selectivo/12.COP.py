# Entrada: 
cantidad = int(input("Ingrese la cantidad en COP: "))

denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

for valor in denominaciones:
    if cantidad >= valor:
        cantidad_unidades = cantidad // valor  
        cantidad %= valor  
        print(f"{cantidad_unidades} x {valor:,} COP")

    
