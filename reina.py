import random

#Bloque todas las posiciones en las que ya no se podran ubicar reinas
def bloquearceldas(m,fil,col):
	i=fil
	j=col
	jizq=col
	jder=col
	i=i+1

	while i<len(m):	
		jizq=jizq-1
		if(jizq>=0):
			m[i][jizq]="x"
		jder=jder+1	
		if(jder<len(m)):
			m[i][jder]="x"
		m[i][j]="x"	
		i+=1
	return 0

#Crea la matriz que simula el tablero
def creamatrix(n):
	fila=['']*n
	for i in range(len(fila)):	
		fila[i]=[0]*n
	return fila

#Llena la matrix con las reinas en las posiciones correctas
def llenamatrix(m):
	for fil in range(len(m)):
		if((0 in m[fil])==True):
			listo=False		
			while listo==False:
				col=random.randint(0,len(m)-1)		
				if (m[fil][col]!="x"):
					m[fil][col]=1
					bloquearceldas(m,fil,col)
					listo=True
		else: break
	return 0

#Limpia la matriz para volver a intentar el llenado
def limpiamatrix(m):
	for i in range(len(m)):
		for j in range(len(m)):
			m[i][j]=0	
	return 0

#Imprime la matriz
def imprimir(m):
	for i in range(len(m)):
		for j in range(len(m)):
			print m[i][j],
		print '\n',
	return 0

#Main de reina

n= int(raw_input("Ingrese el tamano del tablero que desea: "))
m=creamatrix(n)
completo=False
while (completo==False):
	limpiamatrix(m)
	llenamatrix(m)
	completo=True
	for i in range(n):
		completo= completo and (1 in m[i])
imprimir(m)


#FALTA IMPRIMIR LA MATRIZ DE LAS X's ANTES DE IMPRIMIR





