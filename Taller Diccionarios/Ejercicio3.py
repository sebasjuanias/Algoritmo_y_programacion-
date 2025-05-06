usuarios = {
"iperurena": { "nombre": "Iñaki","apellido": "Perurena","password": "123123"},
"fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza","password": "654321"},
"aolaizola": {"nombre": "Aimar","apellido": "Olaizola","password": "123456"}
 }

intentos  = 3 
while intentos > 0:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario in usuarios:
        if usuarios[usuario]["password"] == contraseña:
            print(f"\n¡Bienvenido/a, {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}!")
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")    
    else:
        intentos -= 1
        print(f"El usuario no existe. Te quedan {intentos} intentos.")
    if intentos == 0:
        break