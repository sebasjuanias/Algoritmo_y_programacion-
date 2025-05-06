diccionario = {}
Lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
for i in Lista:
    if i in diccionario:  
        diccionario[i] += 1
    else:
        diccionario[i] = 1
print(diccionario)
