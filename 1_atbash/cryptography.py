
def atbash(message):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrado = alfabeto.upper()[::-1]
    message = message.lower()
    result = ""
    for letra in message:
        if letra in alfabeto:
            result += cifrado[alfabeto.index(letra)]
        else:
            result += letra
    return result

def unatbash(message):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrado = alfabeto.upper()[::-1]
    message = message.upper()
    result = ""
    for letra in message:
        if letra in cifrado:
            result += alfabeto[cifrado.index(letra)]
        else:
            result += letra
    return result


