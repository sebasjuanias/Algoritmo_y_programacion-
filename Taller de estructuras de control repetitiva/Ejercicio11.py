saldo_inicial = [4000000]

deposito = []
retiros = []

while True:

    depositar = input("depositar el dinero (Si/No): ").capitalize()
    
    if depositar == 'Si':
        cuanto_d = int(input("Cuanto depositas: "))
        deposito.append(cuanto_d)
        print(f"El deposito fue de: {cuanto_d}")
        
        saldo = saldo_inicial.pop(0)
        saldototal = saldo + sum(deposito)
        saldo_inicial.append(saldototal)
        print(f"saldo: {saldototal}")
    
    elif depositar == 'No':

        while True:
            retiro = input("Quiere retirar su dinero (Si/No): ").capitalize()
            
            if retiro == 'Si':
                cuanto_r = int(input("Monto a retirar: "))
                saldo_actual = saldo_inicial.pop(0)
                
                if cuanto_r <= saldo_actual:
                    cuanto_queda = saldo_actual - cuanto_r
                    retiros.append(cuanto_r)
                    saldo_inicial.append(cuanto_queda)
                    print(f"Lo que queda es: {cuanto_queda}")
                else:
                    print("Saldo insuficiente para realizar el retiro")
                    saldo_inicial.append(saldo_actual)
            
            elif retiro == 'No':
                break
        
        consultar_saldo = input("Desea saber cual es su saldo (Si/No): ").capitalize()
        if consultar_saldo == 'Si':
            print(f"Su saldo es: {saldo_inicial[0]}")
        
        continuar_encuesta = input("Si desea finalizar escriba 'Salir': ").capitalize()
        
        if continuar_encuesta == 'Salir':
            break



