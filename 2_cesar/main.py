
alfabeto_cifrado = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mensaje = "Hola Mundo"
mensaje_cifrado = ""

clave = 25

for letra in mensaje.upper():

    if letra in alfabeto_cifrado:
        posicion = alfabeto_cifrado.index(letra)
        posicion = (posicion + clave) % len(alfabeto_cifrado)
        mensaje_cifrado += alfabeto_cifrado[posicion]
    else:
        mensaje_cifrado += letra


print("Texto plano: {}".format(mensaje))
print("Texto cifrado: {}".format(mensaje_cifrado))

