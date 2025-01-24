import random
from framework.MinecraftAgentFramework import MinecraftAgent


class RandomTpAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = ("Agente que transporta al jugador a una posición aleatoria dentro de un radio. "
                "Argumentos: radio (int)")
        super().__init__(name, active, info, mc)

    # Sobreescribir el método main_execute:
    def main_execute(self, *args):
        # Se comprueba que se haya pasado como mínimo un argumento
        if len(args) < 1:
            raise ValueError("Se necesita un argumento: radio (int)")

        # Se obtiene el argumento
        try:
            radius = int(args[0])
        except ValueError:
            raise ValueError("El argumento debe ser un numero entero")

        # Se obtiene la posición del jugador
        player_pos = self.get_player_pos()

        # Se calcula una posición aleatoria alrededor del jugador
        x = player_pos.x + random.randint(-radius, radius)
        y = player_pos.y + random.randint(-radius, radius)
        z = player_pos.z + random.randint(-radius, radius)

        # Se transporta al jugador a la posición calculada
        self.tp_player(x, y, z)

