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

#Psar de hexadecimal a polinomio
def hex_polinomio(hex):
    lista = []
    cadena_binaria = bin(int(hex,16)) #Cambiamos de hexadecimal a binario para identifcar los 1 y guardar las posiciones
    for i in range(len(cadena_binaria)):
        if cadena_binaria[i] == "1":
            lista.append(i)

    polinomio = ''
    for i in lista[::-1]:
        if i == 0:
            polinomio += "1"
        else:
            polinomio += f"x^{i} + "
    return polinomio

def operacion_xor(hex1, hex2):
    # Ejemplo 2
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)
    result = num1 ^ num2 #Operacion XOR entre numeros
    return result


# Ejemplo de uso:
num1 = input("Ingrese el primer numero hexadecimal: ")
num2 = input("Ingrese el segundo numero hexadecimal: ")

resultado_multi = multiplicacion(num1, num2)
print(f'El resulatdo de la multiplicacion es :  {resultado_multi}')

print(f'El resulatdo de la multiplicacion (polinomio) :  {hex_polinomio(resultado_multi)}')


# dividendo = binario_polinomio("110110110110")
# divisor = [8, 4, 3, 1, 0]  # Representa x^8 + x^4 + x^3 + x + 1
# print("El residuo de la división es:")
