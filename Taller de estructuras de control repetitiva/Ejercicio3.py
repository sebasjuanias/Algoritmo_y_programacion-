suma = 0 
for i in range(97,1004,1):
    pares = i%2
    if pares == 0:
        suma = suma + i
        print(suma)

print (suma)    