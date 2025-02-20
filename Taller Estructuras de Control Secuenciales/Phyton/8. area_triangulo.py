#entradas
lado1=int(input("lado 1 triangulo"))
lado2=int(input("lado 2 triangulo"))
lado3=int(input("lado 3 triangulo"))
#caja negra
semiperimetro=(lado1+lado2+lado3)/2
area=((semiperimetro-lado1)*(semiperimetro-lado2)*(semiperimetro-lado3))**(1/2)
#salidas
print("area", area)