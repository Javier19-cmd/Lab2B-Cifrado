def ascii_a_binario_manual(ascii_valor):
    binario = ""
    while ascii_valor > 0:
        residuo = ascii_valor % 2
        binario = str(residuo) + binario
        ascii_valor //= 2
    # Rellenando con ceros a la izquierda si es necesario
    if len(binario) < 8:
        while len(binario) < 8:
            binario = "0" + binario
    return binario

def caracteres_a_ascii(cadena):
    # Conversor de cada caracter de la cadena a su valor ASCII
    ascii_resultado = []
    for caracter in cadena:
        ascii_resultado.append(ord(caracter))
    return ascii_resultado