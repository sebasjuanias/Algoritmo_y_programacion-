P=int(input("P"))
Q=int(input("Q"))

resultado=(P**3+Q**4-2*P**2)

if(resultado>680):
    print("P= " + str(P) + " Y Q=" + str(Q) + " P y Q satisfacen la expresión")
else:
    print("P= " + str(P) + " Y Q=" + str(Q) + " P y Q no satisfacen la expresión")
