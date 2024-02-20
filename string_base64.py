def bin_to_base64(bin_list):
    # Convertiendo de binario a ASCII
    ascii_list = [chr(int(b, 2)) for b in bin_list]
    ascii_string = ''.join(ascii_list)

    # Convertiendo de ASCII a base 64 de manera manual
    base64_string = ''
    base64_chars = {i: char for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

    # Convertiendo cada caracter a su representación binaria de 8 bits
    bin_string = ''.join([format(ord(c), '08b') for c in ascii_string])

    # Añadir ceros al principio si la longitud no es múltiplo de 6
    while len(bin_string) % 6 != 0:
        bin_string = "0" + bin_string #+ "0" # Se debe agregar al final no al principio.

    # Convertiendo cada grupo de 6 bits a su correspondiente caracter en base 64
    for i in range(0, len(bin_string), 6):
        base64_string += base64_chars[int(bin_string[i:i+6], 2)]

    # Añadiendo '=' al final si la longitud no es múltiplo de 4
    while len(base64_string) % 4 != 0:
        base64_string += '='

    return base64_string

def base64_to_ascii(base64_string):
    # Diccionario para mapear cada caracter en base 64 a su correspondiente número entero
    base64_chars = {char: i for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

    # Eliminando los caracteres '=' al final de la cadena
    base64_string = base64_string.rstrip('=')

    # Convertir cada caracter en base 64 a su representación binaria de 6 bits
    bin_string = ''.join([format(base64_chars[c], '06b') for c in base64_string])

    # Añadiendo ceros al principio si la longitud no es múltiplo de 8
    while len(bin_string) % 8 != 0:
        bin_string = "0" + bin_string  #+ "0" # Se debe agregar al final no al principio.

    # Convertiendo cada grupo de 8 bits a su correspondiente caracter ASCII
    ascii_string = ''.join([chr(int(bin_string[i:i+8], 2)) for i in range(0, len(bin_string), 8)])

    return ascii_string
