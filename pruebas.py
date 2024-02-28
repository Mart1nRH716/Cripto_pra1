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

# Ejemplo de uso:
A = "0xc3" # 162
B = "0x12" # 22
resultado = multiplicacion(A, B)
print(resultado)  # Debería imprimir: 0x2f
