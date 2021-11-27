
def eliminarEspacios(texto):
    mensaje_nuevo = ""
    for letra in texto:
        if letra != " ":
            mensaje_nuevo += letra
    return mensaje_nuevo
#sin_espacios = eliminarEspacios(mensaje_plano)
#print(sin_espacios)


def agrupar(texto, grupo):
    mensaje_grupo = ""
    #grupo = 4
    x = 0
    for x in range (0, len(texto)):
        if x%grupo==0 and x!=0:
            mensaje_grupo += " "
        mensaje_grupo += texto[x]
    return mensaje_grupo
#agrupado = agrupar(sin_espacios)
#print(agrupado)

def cifrar(texto, clave):
    mensaje_cifrado = [""] * clave
    for columna in range(clave):
        pos = columna
        while pos < len(texto):
            mensaje_cifrado[columna] += texto[pos]
            pos += clave
    #return '-'.join(mensaje_cifrado)
    return ''.join(mensaje_cifrado)
#cifrado = cifrar(sin_espacios, clave)
#print(cifrado, clave)


def main():
    #mensaje_plano = "el gran fiestion sera por la tarde a las tres"
    mensaje_plano = "el bombardeo sera por la tarde a las dos"
    clave = 8 # numero de columnas

    mensaje_sin_espacios = eliminarEspacios(mensaje_plano)
    mensaje_cifrado = cifrar(mensaje_sin_espacios, clave)
    mensaje_agrupado = agrupar(mensaje_cifrado, 4)

    print("Texto plano: {}".format(mensaje_plano))
    print("Texto cifrado: {}".format(mensaje_cifrado))
    print("Texto agrupado: {}".format(mensaje_agrupado))

if __name__=="__main__":
    main()


