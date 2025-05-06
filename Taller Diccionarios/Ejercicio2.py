Diccionario = {
    "Mikel": 3,
    "Ane": 8,
    "Amaia": 12,
    "Unai": 5,
    "Jon": 8,
    "Ainhoa": 7,
    "Maite": 5,
}

Lista = []

for Values in Dicccionario.values():
    if (Lista.count(Values) == 0):
        Lista.append(Values)
    
print(Lista)