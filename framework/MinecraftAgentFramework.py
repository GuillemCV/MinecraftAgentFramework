import datetime
from .mcpi import block

class MinecraftAgent:
    """
    Clase base de la que heredan todos los agentes de Minecraft.
    """

    def __init__(self, name: str, active: bool, mc):
        """
        Inicializa un agente con un nombre y un estado inicial.

        :param name: Nombre del agente.
        :param active: Si el agente está activo o no inicialmente (True o False).
        :param mc: Instancia de Minecraft para interactuar con el servidor.
        """
        self.name = name
        self.active = active
        self.mc = mc

    def send_message(self, message: str):
        """
        Envía un mensaje al chat de Minecraft.

        :param message: Mensaje a enviar.
        """
        self.mc.postToChat(f"[{self.name}]: {message}")

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

    def __init__(self, mc):
        """
        Inicializa el framework con una lista de agentes vacía, un diccionario de comandos vacío
        y una instancia de Minecraft.

        :param mc: Instancia de Minecraft para interactuar con el servidor.
        """
        self.agents = []
        self.commands = {}
        self.mc = mc

    def __print_info(self, message):
        """
        Escribir un mensaje informativo en la consola con la fecha y hora actuales
        y el prefijo [Agent Framework].
        """
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{date} [Agent Framework]: {message}")

    def __write_chat(self, message):
        """
        Escribe un mensaje en el chat de Minecraft.

        :param message: Mensaje a enviar.
        """
        self.mc.postToChat(f"[Agent Framework]: {message}")

    def __read_chat(self) -> str:
        """
        Lee el último mensaje del chat de Minecraft.

        :return: Último mensaje del chat.
        """
        return self.mc.events.pollChatPosts()[-1].message

    def add_agent(self, agent: MinecraftAgent):
        """
        Añade un agente al framework.

        :param agent: Instancia de MinecraftAgent o una clase hija.
        """
        # Si ya existe un agente con el mismo nombre, se muestra un mensaje de error.
        if len(list(filter(lambda a: a.name == agent.name, self.agents))) > 0:
            self.__print_info(
                f"No se puede añadir el agente {agent.name} porque ya existe otro con el mismo nombre"
            )
        else:
            # Si no existe, se añade a la lista de agentes.
            self.agents.append(agent)
            self.__print_info(f"Se ha añadido el agente {agent.name}")

    def remove_agent(self, agent_name: str):
        """
        Elimina un agente del framework.

        :param agent_name: Nombre del agente a eliminar.
        """
        # Se busca el agente por su nombre.
        result = list(filter(lambda a: a.name == agent_name, self.agents))
        agent = result[0] if len(result) > 0 else None

        # Si existe el agente, se elimina de la lista.
        if agent:
            self.agents.remove(agent)
            self.__print_info(f"Se ha eliminado el agente {agent_name}")
        else:
            self.__print_info(f"No se ha encontrado el agente {agent_name}")

    def broadcast_message(self, message):
        """
        Envía un mensaje al chat desde todos los agentes activos.

        :param message: Mensaje a enviar.
        """
        # Se filtran los agentes activos.
        active_agents = list(filter(lambda a: a.active, self.agents))

        # Si no hay agentes activos, se muestra un mensaje en el chat.
        if len(active_agents) == 0:
            self.__write_chat(
                "No hay agentes activos disponibles para enviar el mensaje"
            )
        else:
            # Si hay agentes activos, se envía el mensaje desde cada uno.
            [agent.send_message(message) for agent in active_agents]

    def show_agents(self):
        """
        Muestra en el chat los nombres de todos los agentes
        y su estado actual.
        """
        msg = "Agentes disponibles:"
        if len(self.agents) == 0:
            self.__write_chat(msg + "No hay agentes disponibles")
        else:
            name_active = map(
                lambda a: (a.name, "Activo") if a.active else (a.name, "Inactivo"),
                self.agents,
            )
            
            self.__write_chat(msg)
            for name, status in name_active:
                self.__write_chat(f"{name} - {status}")
            
