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

def peliculas_en_comun(u1, u2):
    
