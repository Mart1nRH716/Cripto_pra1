"""
GF(2^8)
Input:
        A(x) = 0xc3 = 195
        B(x0) = 0x12 = 18
Output:
        C(x) = A(x) * B(x) mod P(x) (en polinomio y en hexadecimal) = 0x19 = x^4 + x^3 + 1
        P(x) = 0x11B = 283
"""

def multiplicacion(hexa1, hexa2):
    # Convertir los números hexadecimales a enteros
    num1 = int(hexa1, 16)
    num2 = int(hexa2, 16)
    # Multiplicar los números
    resultado = num1 * num2
    # Convertir el resultado de nuevo a hexadecimal
    resultado_hex = hex(resultado)
    return resultado_hex


def binario_polinomio(binario):
    lista = []
    cadena_binaria = str(binario)
    for i in range(len(cadena_binaria)):
        if cadena_binaria[i] == "1":
            lista.append(i)
    return lista

def operacion_xor(binario1, binario2):
    # Ejemplo 2
    x = 0b1010  # Representación binaria de 10
    y = 0b1100  # Representación binaria de 12
    result = x ^ y
    print(bin(result))  # Output: 0b110 (Representación binaria de 6)


# Ejemplo de uso:
num1 = input("Ingrese el primer numero hexadecimal: ")
num2 = input("Ingrese el segundo numero hexadecimal: ")

resultado_multi = multiplicacion(num1, num2)
print(resultado_multi)





# dividendo = binario_polinomio("110110110110")
# divisor = [8, 4, 3, 1, 0]  # Representa x^8 + x^4 + x^3 + x + 1
# print("El residuo de la división es:")
