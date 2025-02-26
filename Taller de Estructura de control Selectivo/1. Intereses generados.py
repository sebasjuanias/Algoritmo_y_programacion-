#entradas
inversion=int(input("Inversion"))
tiempo=int(input("tiempo"))
intereses=float(input("intereses"))
#caja negra
Capital_final=(inversion*tiempo*intereses)
if(Capital_final>100000):
#salida
    print("Reinvertir")
else:
    (Capital_final<100000)
    print("No Reinvertir")
print("Intereses ganados", Capital_final)
print("Capital + intereses ganados", (Capital_final+ inversion))