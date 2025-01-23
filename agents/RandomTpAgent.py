import random
from framework.MinecraftAgentFramework import MinecraftAgent, executable
import framework.mcpi.block as block


class RandomTpAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que coloca aleatoriamente bloques de TNT dentro de un radio alrededor del jugador, tantos como se le indique. " 
                "Argumentos: radio (int) y numero de bloques de TNT a colocar (int)")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        # Se comprueba que se hayan pasado como mínimo dos argumentos, el resto se ignoran.
        if len(args) < 2:
            raise ValueError("Se necesitan dos argumentos: radio y numero de bloques de TNT a colocar")

        # Se obtienen los argumentos
        try:
            radius = int(args[0])
            num_tnt = int(args[1])
        except ValueError:
            raise ValueError("Los argumentos deben ser numeros enteros")

        for _ in range(num_tnt):
            self.place_tnt(radius)

    # Definir otros métodos si es necesario, para ser llamados desde main_execute i/o
    # ser ejecutados mediante comandos des del chat del juego (decorator @executable):

    @executable
    def place_tnt(self, radius):
        """
        Coloca un bloque de TNT en una posición aleatoria alrededor del jugador, este
        explota cuando el jugador intenta destruirlo.

        :param radius: Distancia máxima a la que se colocará el TNT alrededor del jugador

        """

        # Se comprueba que el radio sea un número entero
        try:
            radius = int(radius)
        except ValueError:
            raise ValueError("El radio debe ser un numero entero")

        # Se obtiene la posición del jugador
        pos = self.mc.player.getTilePos()

        # Se calcula una posición aleatoria alrededor del jugador
        x = pos.x + random.randint(-radius, radius)
        y = pos.y + random.randint(-radius, radius)
        z = pos.z + random.randint(-radius, radius)

        # Se coloca un bloque de TNT en la posición calculada
        self.place_block(x, y, z, block.TNT, 1)
