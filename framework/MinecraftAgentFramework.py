import mcpi.minecraft as minecraft
import mcpi.block as block


class MinecraftAgent:
    """
    Clase base de la que heredan todos los agentes de Minecraft.
    """

    def __init__(self, name, state, mc):
        """
        Inicializa un agente con un nombre y un estado inicial.

        :param name: Nombre del agente.
        :param state: Estado inicial del agente.
        :param mc: Instancia de Minecraft para interactuar con el servidor.
        """
        self.name = name
        self.state = state
        self.mc = mc

    def send_message(self, message: str):
        """
        Envía un mensaje al chat de Minecraft.

        :param message: Mensaje a enviar.
        """
        self.mc.postToChat(f"{self.name}: {message}")

    def receive_message(self) -> str:
        """
        Lee el último mensaje del chat de Minecraft.

        :return: Último mensaje del chat.
        """
        return self.mc.events.pollChatPosts()[-1].message

    def move_player(self, x, y, z):
        """
        Mueve el jugador a una posición específica.

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
