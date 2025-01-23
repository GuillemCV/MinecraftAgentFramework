import random
import time
from framework.MinecraftAgentFramework import MinecraftAgent, executable
import framework.mcpi.block as block


class MathAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que te da el resultado de la operacion matematica que escojas. "
                "Argumentos: Ninguno")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        # Mostramos las operaciones disponibles
        self.show_ops()

        # Bucle hasta que el jugador escoja una operación
        while True:
            # Se obtiene la respuesta del jugador
            op_num = self.receive_message()

            if not op_num == "":
                try:
                    op_num = int(op_num)
                    if 1 <= op_num <= 4:
                        break
                    else:
                        self.send_message("Por favor, escoge un numero entre 1 y 4")
                except ValueError:
                    self.send_message("Por favor, escribe un numero entero")

            # Esperamos medio segundo
            time.sleep(0.5)

        # Le pedimos al jugador que introduzca dos números enteros
        self.send_message("Introduce dos numeros enteros separados por un espacio:")

        # Bucle hasta que el jugador introduzca dos números enteros
        while True:
            # Se obtiene el primer número
            nums = self.receive_message()

            if not nums == "":
                try:
                    a, b = nums.split(" ")
                    a = int(a)
                    b = int(b)
                    break
                except ValueError:
                    self.send_message("Por favor, escribe dos numeros enteros separados por un espacio")

            # Esperamos medio segundo
            time.sleep(0.5)

        # Realizamos la operación escogida
        if op_num == 1:
            self.sum(a, b)
        elif op_num == 2:
            self.subs(a, b)
        elif op_num == 3:
            self.mult(a, b)
        elif op_num == 4:
            self.div(a, b)

    # Definir otros métodos si es necesario, para ser llamados desde main_execute i/o
    # ser ejecutados mediante comandos des del chat del juego (decorator @executable):

    def show_ops(self):
        """
        Muestra las operaciones matemáticas disponibles.

        """
        ops = ["1. suma", "2. resta", "3. multiplicacion", "4. division"]
        self.send_message("Escoge la operacion que quieras realizar:")
        for op in ops:
            self.send_message(op)

    @executable
    def sum(self, a, b):
        """
        Suma dos números y devuelve el resultado.

        :param a: Primer número
        :param b: Segundo número

        """
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise ValueError("Los argumentos deben ser numeros enteros")

        return self.send_message(f"{a} + {b} = {a + b}")

    @executable
    def subs(self, a, b):
        """
        Resta dos números y devuelve el resultado.

        :param a: Primer número
        :param b: Segundo número

        """
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise ValueError("Los argumentos deben ser numeros enteros")

        return self.send_message(f"{a} - {b} = {a - b}")

    @executable
    def mult(self, a, b):
        """
        Multiplica dos números y devuelve el resultado.

        :param a: Primer número
        :param b: Segundo número

        """
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise ValueError("Los argumentos deben ser numeros enteros")

        return self.send_message(f"{a} * {b} = {a * b}")

    @executable
    def div(self, a, b):
        """
        Divide dos números y devuelve el resultado.

        :param a: Primer número
        :param b: Segundo número

        """
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise ValueError("Los argumentos deben ser numeros enteros")

        return self.send_message(f"{a} / {b} = {a / b}")
