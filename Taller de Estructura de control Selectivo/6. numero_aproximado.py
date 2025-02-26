# Entrada
N = input("N")
a, b, c, d = map(int, N)
#Caja negra
N = a * 1000 + b * 100 + c * 10 + d

centenas = (N // 100) * 100
decenas = N % 100  

if decenas >= 50:
    N_redondeado = centenas + 100 
else:
    N_redondeado = centenas

# Salida
print("Numero redondeado", N_redondeado)
