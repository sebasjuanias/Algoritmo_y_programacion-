ContadorLicor = 0
ContadorNoLicor = 0
ContadorMujer = 0
ContadorHombre = 0
ContadorEdadMujer = 0
ContadorHombreSinAguardiente = 0
ContadorAlguardiente = 0
ContadorRon = 0
ContadorCerveza = 0
ContadorTequila = 0
ContadorWhisky = 0
ContadorOtro = 0
EdadPromedio = 0
while True:
    Consumelicor = input("\nconsume licor? ")
    LicorPreferido = int(input("Que licor es su preferido? "))
    if LicorPreferido == 1:
        ContadorAlguardiente = ContadorAlguardiente + 1
    elif LicorPreferido == 2:
        ContadorRon = ContadorRon + 1   
    elif LicorPreferido == 3:
        ContadorCerveza = ContadorCerveza + 1 
    elif LicorPreferido == 4:
        ContadorTequila = ContadorTequila + 1         
    elif LicorPreferido == 5:
        ContadorWhisky = ContadorWhisky + 1
    elif LicorPreferido == 6:
        ContadorOtro = ContadorOtro + 1    
    Sexo = input("Escriba su sexo? ")
    Edad = int(input("Que edad Tiene? "))
    if Consumelicor == "si":
        ContadorLicor = ContadorLicor + 1
    else:
        ContadorNoLicor = ContadorNoLicor + 1
    LicorTotal = ContadorLicor + ContadorLicor
    if Sexo == "mujer":
        if Edad < 18:
          ContadorEdadMujer = ContadorEdadMujer + 1
    if Sexo == "hombre":
        if 20<=Edad<=25:
            ContadorHombres = ContadorCerveza + ContadorRon + ContadorTequila+ ContadorWhisky + ContadorOtro
    if LicorPreferido == 3:
        EdadPromedio = (EdadPromedio + Edad)
    ContinuarEncuesta = input("\nDesea continuar Encuenta? ")
    if ContinuarEncuesta == "si":
        continue
    else:
        break  
print(f"Total consumen licor son: {ContadorLicor}")
print(f"Total mujeres menor de edad {ContadorEdadMujer}")
print(f"Total hombres que no consumenten aguardiente y tienen entre 20 y 25 años {ContadorHombres}" )
print(f"Promedio de edad de quienes consumen cerveza:{EdadPromedio/ContadorCerveza}")
print(f"Personas que consumen whisky respeto al total encuentado {(ContadorWhisky/ContadorLicor)*100}")