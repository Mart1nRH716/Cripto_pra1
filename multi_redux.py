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
    
    # Realizar la multiplicación en GF(2^8)
    producto = 0
    while num1 and num2:
        if num2 & 1:
            producto ^= num1
        num2 >>= 1
        num1 <<= 1
        if num1 & 0x100:
            num1 ^= 0x11B  # Polinomio irreducible x^8 + x^4 + x^3 + x + 1

    # Si el producto es mayor que 255, aplicamos la reducción módulo P(x)
    if producto > 255:
        producto ^= 0x11B
    
    # Convertir el producto de nuevo a hexadecimal
    resultado_hex = hex(producto)
    return resultado_hex

#Psar de hexadecimal a polinomio
#Devuelve un string que corresponde al hexadecimal
def hex_polinomio(hex):
    lista = []
    cadena_binaria = bin(int(hex, 16))[2:] #Cambiamos de hexadecimal a binario para identifcar los 1 y guardar las posiciones
    cadena_binaria = cadena_binaria[::-1]
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



# Ejemplo de uso:
num1 = input("Ingrese el primer numero hexadecimal: ")
num2 = input("Ingrese el segundo numero hexadecimal: ")

resultado = multiplicacion(num1, num2)
print(f'El resulatdo de la multiplicacion es :  {resultado}')

print(f'El resultado de la multiplicacion (polinomio) :  {hex_polinomio(resultado)}')
