N = int(input())
suma = 0 
for i in range(1, N):
    divisor = N%i
    if divisor == 0:
        suma = suma + i
if suma == N:    
   print("El numero es perfecto")
else:
    print("el numero no es perfecto",suma)