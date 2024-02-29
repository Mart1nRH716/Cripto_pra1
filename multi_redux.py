"""
GF(2^8)
Input:
        A(x) = 0xc3 = 195
        B(x0) = 0x12 = 18
Output:
        C(x) = A(x) * B(x) mod P(x) (en polinomio y en hexadecimal) = 0x19 = x^4 + x^3 + 1
        P(x) = 0x11B = 283
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


def multiplicacion(hexa1, hexa2):
    # Convertir los números hexadecimales a enteros
    num1 = int(hexa1, 16)
    num2 = int(hexa2, 16)

    # Realizar la multiplicación en GF(2^8)
    producto = 0
    while num1 and num2:
        if num2 & 1:
            producto ^= num1
        num2 >>= 1 #Se desplaza un bit a la derecha, es decir, se elimina el bit lsb
        num1 <<= 1 #Se le agrega un cero, es decir se multiplica *2
        if num1 & 0x100: #0x100 = 256 compara el bit mas siignificativo, y hace and entre ese bit y el 1 de 256. si se 1 significa que se paso
            num1 ^= 0x11B  #Procedemos hacer la reduccion

    # Si el producto es mayor que 255, aplicamos la reducción módulo P(x)
    if producto > 255:
        producto ^= 0x11B

    # Convertir el producto de nuevo a hexadecimal
    resultado_hex = hex(producto)
    return resultado_hex


# Pasar de hexadecimal a polinomio
# Devuelve un string que corresponde al hexadecimal
def hex_polinomio(hex):
    lista = []
    cadena_binaria = bin(int(hex, 16))[2:]  # Cambiamos de hexadecimal a binario para identifcar los 1 y guardar las posiciones
    cadena_binaria = cadena_binaria[::-1]  # Invertimos la lista debido a que al principio se encuentras los bits menos significativos
    for i in range(len(cadena_binaria)):
        if cadena_binaria[i] == "1":
            lista.append(i)  # Guardamos la posicion en una lista del bit encendido

    polinomio = ' '
    for i in lista[::-1]:
        if i == 0:
            polinomio += "1"
        else:
            polinomio += f"x^{i} +"
    return polinomio


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiplicación en GF(2^8)")
        self.layout = QVBoxLayout()

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.result_label = QLabel()

        self.layout.addWidget(QLabel("Ingrese el primer número hexadecimal:"))
        self.layout.addWidget(self.input1)
        self.layout.addWidget(QLabel("Ingrese el segundo número hexadecimal:"))
        self.layout.addWidget(self.input2)

        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate)

        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def calculate(self):
        num1 = self.input1.text()
        num2 = self.input2.text()

        if num1 and num2:
            resultado = multiplicacion(num1, num2)
            resultado_polinomio = hex_polinomio(resultado)
            self.result_label.setText(f'Resultado de la multiplicación: {resultado}\n'
                                      f'Resultado de la multiplicación (polinomio): {resultado_polinomio}')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
