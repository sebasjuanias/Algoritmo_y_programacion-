km=int(input(" Km "))

if(km<=300):
    print("Pago $", 50000)
elif(km>300 and km<=1000):
    print("Pago $", 70000 + (km-300)*30000)
elif(km>1000):
    print("Pago $", 150000 + (km-1000)*9000)
    