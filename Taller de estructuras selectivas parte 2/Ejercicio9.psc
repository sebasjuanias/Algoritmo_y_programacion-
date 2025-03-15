Algoritmo Ejercicio9
	Palabra<- ""
	escribir"escribir una palabra"
	Leer palindromo1
	long<-Longitud(palindromo1)
	inversa<-""
	para i <- long Hasta 1 con paso -1 Hacer
		inversa<-inversa+Subcadena(palindromo1,i,i)
		
	FinPara
	Escribir inversa
	si palindromo1 = inversa Entonces
		escribir "Es un palindromo"
	SiNo
		Escribir "No es un palindromo"
	FinSi
FinAlgoritmo