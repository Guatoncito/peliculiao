def obtener_pelicula(codigo):
    peliculas = open('movies.txt')
    letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    peli = ''
    for linea in peliculas:
        inf = linea.strip().split()
        if int(inf[0]) == codigo:
            for d in inf:
                c = 0
                if d[0] != '(' and d != codigo:
                    peli += ' ' + d 
                if d[0] == '(':
                    if d[1] in letras:
                        peli += ' ' + d
    peli = peli.split()
    peli = ' '.join(peli)
    return peli

def peliculas_en_comun(usuario1,usuario2,matriz):
    comun=list()
    for i in range(1682):
        if matriz[usuario1-1,i]!=0 and matriz[usuario2-1,i]!=0:
            comun.append(i+1)
    return comun


def corr(usuario1,usuario2,matriz):
    rating1=list()
    rating2=list()
    sum1=0
    sum2=0
    sum3=0
    for i in range(1682):
        if matriz[usuario1-1,i]!=0:
            rating1.append(matriz[usuario1-1,i])
        if matriz[usuario2-1,i]!=0:
            rating2.append(matriz[usuario2-1,i])
    rating1=sum(rating1)/len(rating1)
    rating2=sum(rating2)/len(rating2)
    peliculas_comunes=peliculas_en_comun(usuario1,usuario2,matriz)
    for i in peliculas_comunes:
        sum1+=(matriz[usuario1-1,i-1]-rating1)*(matriz[usuario2-1,i-1]-rating2)
        sum2+=(matriz[usuario1-1,i-1]-rating1)**2
        sum3+=(matriz[usuario2-1,i-1]-rating2)**2
    correlacion=sum1/((sum2**0.5)*(sum3**0.5))
    return correlacion 

def peliculas_no_comun(u1, u2, matriz): #Peliculas que u1 ha visto y u2 no
    no_comun = list()
    mayor = 0
    for i in range(1682):
        if matriz[u1-1, i] != 0 and matriz[u2-1, i] == 0:
            if matriz[u1-1, i] > mayor:
                no_comun = list()
                no_comun.append(i+1)
                mayor = matriz[u1-1, i]
            elif matriz[u1-1, i] == mayor:
                no_comun.append(i+1)
    return no_comun
