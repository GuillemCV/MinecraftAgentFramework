import time
from framework.MinecraftAgentFramework import MinecraftAgent, executable


class MathAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que te da el resultado de la operacion matematica que escojas. "
                "Argumentos: Ninguno")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        self.show_ops() # Mostramos las operaciones disponibles
        op_num = self.choose_op() # El jugador escoge una operación
        self.send_message("Introduce dos numeros enteros separados por un espacio:")
        a, b = self.write_numbers() # El jugador introduce dos números enteros
        self.do_operation(a, b, op_num) # Realizamos la operación escogida

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
    
    def choose_op(self) -> int:
        """
        Pide al jugador que escoja una operación matemática.

        """
        # Bucle hasta que el jugador escoja una operación
        while True:
            # Se obtiene la respuesta del jugador
            op_num = self.receive_message()

            if not op_num == "":
                try:
                    op_num = int(op_num)
                    if 1 <= op_num <= 4:
                        return op_num
                    else:
                        self.send_message("Por favor, escoge un numero entre 1 y 4")
                except ValueError:
                    self.send_message("Por favor, escribe un numero entero")

            # Esperamos medio segundo
            time.sleep(0.5)
    
    def write_numbers(self) -> tuple:
        """
        Pide al jugador que introduzca dos números enteros.

        """
        # Bucle hasta que el jugador introduzca dos números enteros
        while True:
            # Se obtiene el primer número
            nums = self.receive_message()

            if not nums == "":
                try:
                    a, b = nums.split(" ")
                    a = int(a)
                    b = int(b)
                    return a, b
                except ValueError:
                    self.send_message("Por favor, escribe dos numeros enteros separados por un espacio")

            # Esperamos medio segundo
            time.sleep(0.5)
    
    def do_operation(self, a, b, op):
        """
        Realiza la operación matemática escogida por el jugador.

        :param a: Primer número
        :param b: Segundo número
        :param op: Operación a realizar

        """
        if op == 1:
            return self.sum(a, b)
        elif op == 2:
            return self.subs(a, b)
        elif op == 3:
            return self.mult(a, b)
        elif op == 4:
            return self.div(a, b)

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
