from numpy import *
from funciones import *
usuarios=open('u.txt')
principal=zeros((943,1682))
usuario_a_recomendar=10
for linea in usuarios:
	linea=linea.strip().split(' ')
	principal[(int(linea[0])-1),(int(linea[1])-1)]=int(linea[2])

