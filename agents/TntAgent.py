from framework.MinecraftAgentFramework import MinecraftAgent, executable

import framework.mcpi.minecraft as minecraft
import framework.mcpi.block as block


class TntAgent(MinecraftAgent):
    def __init__(self, name, active, mc):
        super().__init__(name, active, mc)

    def place_tnt(self, x, y, z):
        print(f"TNT placed by {self.name} at ({x}, {y}, {z})")

    # sobreescribir el método main_execute


    def main_execute(self, *args):
        self.send_message("Ejecutando...")
        self.send_message("Fin de la ejecución")
