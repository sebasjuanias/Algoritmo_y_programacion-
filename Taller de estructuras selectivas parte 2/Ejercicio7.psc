Algoritmo Ejercicio7
	Definir num, iteracion Como Entero
	Escribir "Escriba un numero para verificar si es primo o no"
	Leer num
	contar<-0
	Para iteracion<-1 Hasta num Hacer
		si num % iteracion = 0 Entonces
			contar<-contar+1
		FinSi
	FinPara
	si contar = 2 Entonces
		Escribir "es primo"
	SiNo
		Escribir "no es primo"
	FinSi
FinAlgoritmo