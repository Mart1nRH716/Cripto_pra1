"""
GF(2^8)
Input:
        A(x) = 0xc3 = 195
        B(x0) = 0x12 = 18
Output:
        C(x) = A(x) * B(x) mod P(x) (en polinomio y en hexadecimal) = 0x19 = x^4 + x^3 + 1
        P(x) = 0x11B = 283
"""

#Multiplica dos numeros hexadecimales y devuelve el valor en hexadecimal
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
#Devuelve un string que corresponde al hexadecimal
def hex_polinomio(hex):
    lista = []
    cadena_binaria = bin(int(hex,16)) #Cambiamos de hexadecimal a binario para identifcar los 1 y guardar las posiciones
    for i in range(len(cadena_binaria)):
        if cadena_binaria[i] == "1":
            lista.append(i)

    polinomio = ' '
    for i in lista[::-1]:
        if i == 0:
            polinomio += "1"
        else:
            polinomio += f"x^{i} +"
    return polinomio

#Recibe dos numeros en hexadecimal
#No se si devolver el resultado en hexadecimal
def operacion_xor(hex1, hex2):
    # Ejemplo 2
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)
    result = num1 ^ num2 #Operacion XOR entre numeros
    return result

#Recibe un numero hexadecimal y extra el sobrante
def extraer_residuo(num_hex):
    return str(num_hex)[0]

def reducir_modulo(resultado_hex):
    # Convertir el resultado a entero
    resultado_entero = int(resultado_hex, 16)
    # Definir el polinomio irreducible P(x) = x^8 + x^4 + x^3 + x + 1
    polinomio_irreducible = 0x11B
    # Realizar la reducción módulo el polinomio irreducible
    while resultado_entero >= 256:
        reduccion = polinomio_irreducible << (resultado_entero.bit_length() - 9)
        resultado_entero ^= reduccion
    # Convertir el resultado reducido de nuevo a hexadecimal
    resultado_hex_reducido = hex(resultado_entero)
    return resultado_hex_reducido


# Ejemplo de uso:
num1 = input("Ingrese el primer numero hexadecimal: ")
num2 = input("Ingrese el segundo numero hexadecimal: ")

resultado_multi = multiplicacion(num1, num2)
print(f'El resulatdo de la multiplicacion es :  {resultado_multi}')

print(f'El resultado de la multiplicacion (polinomio) :  {hex_polinomio(resultado_multi)}')

print(reducir_modulo(resultado_multi))

# dividendo = binario_polinomio("110110110110")
# divisor = [8, 4, 3, 1, 0]  # Representa x^8 + x^4 + x^3 + x + 1
# print("El residuo de la división es:")
