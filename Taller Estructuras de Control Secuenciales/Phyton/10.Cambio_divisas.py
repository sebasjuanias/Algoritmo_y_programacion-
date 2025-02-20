#entradas
cheaustriacos=int(input("Chelines Austriacos"))
dragriegos=int(input("Dragmas Griegos"))
pesetas=int(input("Pesetas"))
#caja negra
pesetas=cheaustriacos*9.56871
franco_frances=(dragriegos*0.88607)*(1/20.110)
dolares=(pesetas*(1/122.499))
liras=(pesetas*(100/9.289))
#salidas
print("Pesetas", pesetas)
print("Franco Frances", franco_frances)
print("Dolares", dolares)
print("Liras", liras)