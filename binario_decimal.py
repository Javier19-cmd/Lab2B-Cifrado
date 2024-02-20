def binario_a_ascii(binario):
    # Conversor de la representación binaria a su valor ASCII
    ascii_valor = 0
    for i in range(len(binario)):
        ascii_valor += int(binario[i]) * (2 ** (len(binario) - i - 1))
    return ascii_valor

def ascii_a_caracter(ascii_valor):
    # Conversor al valor ASCII a su carácter correspondiente
    return chr(ascii_valor)

def binario_a_caracter(binario):
    # Conversor a la representación binaria directamente a su carácter correspondiente
    ascii_valor = binario_a_ascii(binario)
    return ascii_a_caracter(ascii_valor)

def binario_a_cadena(binario):
    # Convirtiendo a una cadena de string todo lo que tenía en binario.
    cadena = ""
    for i in range(0, len(binario), 8):
        cadena += binario_a_caracter(binario[i:i+8])
    return cadena