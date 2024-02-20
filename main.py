from decimal_binario import *
from binario_decimal import *
from string_base64 import *
from xor_cadenas import *

def main():
    cadena = "Hola Mundo"

    # Obteniendo los valores ASCII de los caracteres
    ascii_resultado = caracteres_a_ascii(cadena)
    print("Representación ASCII de la cadena:")
    print(ascii_resultado)

    # Convertiendo los valores ASCII a su representación binaria manualmente
    binario_resultado = [ascii_a_binario_manual(valor) for valor in ascii_resultado]
    print("Representación binaria de la cadena:")
    print(binario_resultado)
    
    key = 'lla'
    
    ascii_key = caracteres_a_ascii(key)
    ascii_key = [ascii_a_binario_manual(valor) for valor in ascii_key]

    print("Representación ASCII de la llave: ")
    print(ascii_key)
    
    # binario_resultado = [xor_bin_strings(binario, ascii_a_binario_manual(ascii_key[i % len(ascii_key)])) for i, binario in enumerate(binario_resultado)]
    
    binario_resultado = xor_cadenas(binario_resultado, ascii_key)
    
    print("El resultado de la operación XOR es: ")
    print(binario_resultado)
    
    resultado_xor = xor_cadenas(binario_resultado, key)

    # print("El resultado de la operación XOR es: ")
    # print(resultado_xor)
    
    # reversion = xor_strings(resultado_xor, key)
    # print("El resultado de la operación XOR es: ")
    # print(reversion)
    
    
    # base64 = bin_to_base64(binario_resultado)
    # print("Representación base 64 de la cadena:")
    # print(base64)
    
    # string = base64_to_ascii(base64)
    # print("Representación ASCII de la cadena:")
    # print(string)

    # # Convertiendo la representación binaria a la cadena original
    # cadena_original = binario_a_cadena(''.join(binario_resultado))
    # print("Cadena original obtenida de la representación binaria:")
    # print(cadena_original)

if __name__ == "__main__":
    main()