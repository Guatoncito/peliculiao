def obtener_pelicula(codigo):
    peliculas = open('movies.txt')
    letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    peli = ''
    for linea in peliculas:
        inf = linea.strip().split()
        if inf[0] == codigo:
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

def peliculas_no_comun(u1, u2, matriz): #Peliculas que u1 ha visto y u2 no
    no_comun = list()
    for i in range(1682):
        if matriz[u1-1, i] != 0 and matriz[u2-1, i] == 0:
            no_comun.append(i+1)
    return no_comun
