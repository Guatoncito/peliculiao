from numpy import *
from funciones import *
usuarios=open('u.txt')
principal=zeros((943,1682))
usuario_a_recomendar=10
usuario_recom=0
mayor_correl=0
baneados=list()
recomendadas=list()
for linea in usuarios:
	linea=linea.strip().split(' ')
	principal[(int(linea[0])-1),(int(linea[1])-1)]=int(linea[2])
	
while True:
        for p in range(1,944):
                correl=corr(usuario_a_recomendar,p,principal)
                if correl>mayor_correl and (p not in baneados):
                        usuario_recom=p
        peliculas_recomendadas=peliculas_no_comun(usuario_a_recomendar,usuario_recom,principal)
        if len(peliculas_recomendadas)==0:
                baneados.append(usuario_recom)
                mayor_correl=0
                continue
        break
for pelicu in peliculas_recomendadas:
	recomendadas.append(obtener_pelicula(pelicu))
print recomendadas
