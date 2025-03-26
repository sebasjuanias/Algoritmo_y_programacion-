dividendo = int(input("dividendo"))
divisor = int(input("divisor"))
contador = 0
while True:
    dividendo = dividendo-divisor
    contador = contador + 1
    if dividendo<divisor:
        break
print(f"Residuo:{dividendo}")
print(f"Cociente:{contador}")