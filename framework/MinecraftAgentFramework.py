import mcpi.minecraft as minecraft
import mcpi.block as block

class MinecraftAgent:
    """
    Clase base para agentes de Minecraft que proporciona funcionalidades básicas
    para interactuar con el servidor de Minecraft.
    """

    def __init__(self, name="Agent"):
        """
        Inicializa un nuevo agente de Minecraft.

        :param name: Nombre del agente (opcional).
        """
        self.name = name
        self.mc = minecraft.Minecraft.create()

    def send_message(self, message):
        """
        Envía un mensaje al chat de Minecraft.

        :param message: Mensaje a enviar.
        """
        self.mc.postToChat(f"{self.name}: {message}")

    def move_to(self, x, y, z):
        """
        Mueve al agente a una posición específica.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        """
        self.mc.player.setTilePos(x, y, z)

    def place_block(self, block_type, x, y, z):
        """
        Coloca un bloque en una posición específica.

        :param block_type: Tipo de bloque (por ejemplo, block.STONE).
        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        """
        self.mc.setBlock(x, y, z, block_type)

    def destroy_block(self, x, y, z):
        """
        Destruye un bloque en una posición específica.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        """
        self.mc.setBlock(x, y, z, block.AIR.id)

class MinecraftFramework:
    """
    Framework principal para gestionar y coordinar agentes en un servidor de Minecraft.
    """

    def __init__(self):
        """
        Inicializa el framework con una lista de agentes vacía.
        """
        self.agents = []

    def add_agent(self, agent):
        """
        Añade un agente al framework.

        :param agent: Instancia de MinecraftAgent o una clase derivada.
        """
        self.agents.append(agent)

    def broadcast_message(self, message):
        """
        Envía un mensaje al chat desde todos los agentes.

        :param message: Mensaje a enviar.
        """
        for agent in self.agents:
            agent.send_message(message)

    def run_all(self):
        """
        Método para ejecutar las tareas principales de todos los agentes.

        Nota: Este método debe ser sobrescrito por subclases o por el usuario.
        """
        for agent in self.agents:
            agent.send_message("Listo para interactuar con el mundo de Minecraft!")
