from cryptography import atbash, unatbash

mensaje = "Hola Mundo $$"
cifrado = atbash(mensaje)
print("Texto plano: {}".format(mensaje))
print("Texto cifrado: {}".format(cifrado))
print("Texto descifrado: {}".format(unatbash(cifrado)))

