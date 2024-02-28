def hexadecimal_a_binario(hexadecimal):
    # Convierte el número hexadecimal a un entero
    entero = int(hexadecimal, 16)
    # Convierte el entero a una cadena binaria y elimina el prefijo '0b'
    binario = format(entero, 'b')
    return binario

def binario_polinomio(binario):
    lista = []
    cadena_binaria = str(binario)
    for i in range(len(cadena_binaria)):
        if cadena_binaria[i] == "1":
            lista.append(i)
    return lista


var = binario_polinomio(hexadecimal_a_binario("4"))
print(var)