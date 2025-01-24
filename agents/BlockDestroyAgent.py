import random
from framework.MinecraftAgentFramework import MinecraftAgent, executable


class BlockDestroyAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que destruye bloques en un radio alrededor del jugador, tantos como se le indique. " 
                "Argumentos: radio (int) y numero de bloques a destruir (int)")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        # Se comprueba que se hayan pasado como mínimo dos argumentos, el resto se ignoran.
        if len(args) < 2:
            raise ValueError("Se necesitan dos argumentos: radio (int) y numero de bloques a destruir (int)")

        # Se obtienen los argumentos
        try:
            radius = int(args[0])
            num_blocks = int(args[1])
        except ValueError:
            raise ValueError("Los argumentos deben ser numeros enteros")

        for _ in range(num_blocks):
            self.destroy(radius)

    # Definir otros métodos si es necesario, para ser llamados desde main_execute i/o
    # ser ejecutados mediante comandos des del chat del juego (decorator @executable):

    @executable
    def destroy(self, radius):
        """
        Destruye un bloque en una posición aleatoria alrededor del jugador.

        :param radius: Radio de destrucción alrededor del jugador.

        """

        # Se comprueba que el radio sea un número entero
        try:
            radius = int(radius)
        except ValueError:
            raise ValueError("El radio debe ser un numero entero")

        # Se obtiene la posición del jugador
        pos = self.get_player_pos()

        # Se calcula una posición aleatoria alrededor del jugador
        x = pos.x + random.randint(-radius, radius)
        y = pos.y + random.randint(-radius, radius)
        z = pos.z + random.randint(-radius, radius)

        # Se destruye el bloque en la posición calculada
        self.destroy_block(x, y, z)
