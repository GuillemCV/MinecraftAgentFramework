import datetime
import time
import inspect
from .mcpi import block
from .mcpi.minecraft import Minecraft


def executable(method):
    """
    Decorador para marcar un método como ejecutable mediante comandos des del chat de Minecraft.

    :param method: Método a decorar.
    :return: Método decorado.
    """

    # Se añade un atributo al método para marcarlo como ejecutable.
    method.executable = True

    # Se devuelve el método original.
    return method

class MinecraftAgent:
    """
    Clase base de la que heredan todos los agentes de Minecraft.
    """

    def __init__(self, name: str, active: bool, mc: Minecraft):
        """
        Inicializa un agente con un nombre y un estado inicial.

        :param name: Nombre del agente.
        :param active: Si el agente está activo o no inicialmente (True o False).
        :param mc: Instancia de Minecraft para interactuar con el servidor.
        """
        self.name = name
        self.active = active
        self.mc = mc

        self.executable_methods = []
        """
        Lista de nombres de métodos que se pueden ejecutar mediante comandos desde el chat de Minecraft
        a través del framework.
        """

        # Se obtienen los métodos ejecutables
        for method_name in dir(self):
            # Si el nombre no empieza por __
            if not method_name.startswith("__"):
                method = getattr(self, method_name)
                # Si es un método y es ejecutable
                if callable(method) and hasattr(method, "executable"):
                    # Se añade a la lista de métodos ejecutables
                    self.executable_methods.append(method_name)

    # Métodos para interactuar con el servidor de Minecraft:

    def send_message(self, message: str):
        """
        Envía un mensaje al chat de Minecraft.

        :param message: Mensaje a enviar.
        """
        self.mc.postToChat(f"[{self.name}]: {message}")

    def receive_message(self) -> str:
        """
        Lee el último mensaje del chat de Minecraft. 
        Si no hay mensajes, devuelve una cadena vacía.

        :return: Último mensaje del chat o cadena vacía.
        """
        # Se obtienen los eventos del chat
        list = self.mc.events.pollChatPosts()
        # Si hay mensajes, se devuelve el último. Si no, una cadena vacía.
        return list[-1].message if len(list) > 0 else ""

    def tp_player(self, x, y, z):
        """
        Teletransporta al jugador a una posición específica.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        """
        self.mc.player.setTilePos(x, y, z)

    def get_player_pos(self) -> tuple:
        """
        Obtiene la posición actual del jugador.

        :return: Tupla con las coordenadas X, Y, Z.
        """
        return self.mc.player.getTilePos()

    def place_block(self, x, y, z, block_type, data=0):
        """
        Coloca un bloque en una posición específica.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        :param block_type: Tipo de bloque (por ejemplo, block.STONE).
        :param data: Datos adicionales del bloque (por ejemplo, 1 para un bloque de TNT
        que explotará al ser golpeado).
        """
        self.mc.setBlock(x, y, z, block_type.id, data)

    def destroy_block(self, x, y, z):
        """
        Destruye un bloque en una posición específica.

        :param x: Coordenada X.
        :param y: Coordenada Y.
        :param z: Coordenada Z.
        """
        self.mc.setBlock(x, y, z, block.AIR.id)

    # Métodos para obtener y mostrar los métodos de la clase que se pueden ejecutar
    # mediante comandos desde el chat de Minecraft:

    @executable
    def show_methods(self):
        """
        Muestra en el chat los métodos que se pueden ejecutar mediante comandos
        desde el chat de Minecraft y sus parámetros.
        """

        # Se obtienen los métodos de la clase
        methods = self.get_methods_names()

        # Se obtienen los parámetros de cada método usando inspect
        methods_params = []
        for method in methods:
            method_obj = getattr(self, method)
            params = inspect.signature(method_obj).parameters
            methods_params.append(", ".join(params.keys()))

        # Se muestra en el chat el nombre de los métodos y sus parámetros
        self.send_message("Metodos disponibles:")
        [self.send_message(f"- {method}({params})") for method, params in zip(methods, methods_params)]

    def get_methods_names(self) -> list:
        """
        Devuelve el atributo executable_methods.

        :return: Lista con los nombres de los métodos que se pueden ejecutar
        mediante comandos desde el chat de Minecraft.
        """
        return self.executable_methods

    # Métodos para ejecutar un agente:

    @executable
    def execute(self, *args):
        """
        Template method para ejecutar un agente.

        :param args: Argumentos que se pasan al método principal.
        """
        # Se ejecutan el metodo ini_execute
        self.ini_execute()

        # Se ejecuta el método principal
        self.main_execute(*args)

        # Se ejecuta el método end_execute
        self.end_execute()

    def ini_execute(self):
        """
        Método que se ejecuta al inicio de la ejecución del agente.
        """
        self.send_message("Ejecutando...")

    def main_execute(self, *args):
        """
        Método principal de la ejecución del agente.
        """
        pass

    def end_execute(self):
        """
        Método que se ejecuta al final de la ejecución del agente.
        """
        self.send_message("Fin de la ejecución")

def command(cmd : str):
    """
    Decorador para asociar un comando con un método del framework.

    :param cmd: Comando que se debe escribir en el chat para ejecutar el método.
    :return: Método decorado.
    """
    def decorator(method):
        # Se añade un atributo al método para asociar el comando.
        method.command = cmd

        # Se devuelve el método original.
        return method

    return decorator

class MinecraftFramework:
    """
    Framework principal que procesa los comandos escritos en el chat de Minecraft
    y ejecuta los métodos correspondientes de los agentes registrados.
    """

    def __init__(self, mc: Minecraft):
        """
        Inicializa el framework con una lista de agentes vacía, un diccionario de comandos vacío
        y una instancia de Minecraft.

        :param mc: Instancia de Minecraft para interactuar con el servidor.
        """
        self.agents = []  # Lista de agentes registrados en el framework.
        self.mc = mc
        self.commands = {} # Diccionario de comandos y sus métodos asociados.

        # Se inicializan los comandos y los métodos asociados.
        for method_name in dir(self):
            # Si el nombre no empieza por __
            if not method_name.startswith("__"):
                method = getattr(self, method_name)
                # Si es un método y tiene el atributo command
                if callable(method) and hasattr(method, "command"):
                    # Se añade al diccionario de comandos
                    self.commands[method.command] = method
                

    def __print_info(self, message):
        """
        Escribir un mensaje informativo en la consola con la fecha y hora actuales
        y el prefijo [Agent Framework].
        """
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{date} [Agent Framework]: {message}")

    def write_chat(self, message):
        """
        Escribe un mensaje en el chat de Minecraft.

        :param message: Mensaje a enviar.
        """
        self.mc.postToChat(f"[Agent Framework]: {message}")

    def read_chat(self) -> str:
        """
        Lee el último mensaje del chat de Minecraft. 
        Si no hay mensajes, devuelve una cadena vacía.

        :return: Último mensaje del chat o cadena vacía.
        """
        # Se obtienen los eventos del chat
        list = self.mc.events.pollChatPosts()
        # Si hay mensajes, se devuelve el último. Si no, una cadena vacía.
        return list[-1].message if len(list) > 0 else ""
    
    def search_agent(self, agent_name: str) -> MinecraftAgent:
        """
        Busca un agente por su nombre.

        :param agent_name: Nombre del agente a buscar.
        :return: Instancia del agente si se encuentra, None en caso contrario.
        """
        result = list(filter(lambda a: a.name == agent_name, self.agents))
        return result[0] if len(result) > 0 else None

    def add_agent(self, agent: MinecraftAgent):
        """
        Añade un agente al framework.

        :param agent: Instancia de MinecraftAgent o una clase hija.
        """
        # Si ya existe un agente con el mismo nombre, se muestra un mensaje de error. 
        if self.search_agent(agent.name):
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
        agent = self.search_agent(agent_name)

        # Si existe el agente, se elimina de la lista.
        if agent:
            self.agents.remove(agent)
            self.__print_info(f"Se ha eliminado el agente {agent_name}")
        else:
            self.__print_info(f"No se ha encontrado el agente {agent_name}")

    @command("sayhi")
    def say_hi(self):
        """
        Todos los agentes activos envían un mensaje al chat de Minecraft.
        Es útil para comprobar des del chat que agentes están activos.
        """
        # Se filtran los agentes activos.
        active_agents = list(filter(lambda a: a.active, self.agents))

        # Si no hay agentes activos, se muestra un mensaje en el chat.
        if len(active_agents) == 0:
            self.write_chat("No hay agentes activos disponibles")
        else:
            # Si hay agentes activos, se envía un mensaje desde cada uno.
            [agent.send_message("Hola !!!") for agent in active_agents]

    @command("shagents")
    def show_agents(self):
        """
        Muestra en el chat los nombres de todos los agentes
        y su estado actual.
        """
        self.write_chat("Agentes disponibles:")
        if len(self.agents) == 0:
            self.write_chat("No hay agentes disponibles")
        else:
            name_active = map(lambda a: (a.name, "Activo") if a.active else (a.name, "Inactivo"), self.agents,)
            [self.write_chat(f"- {name} ({status})") for name, status in name_active]

    @command("help")
    def help(self):
        """
        Muestra en el chat los comandos disponibles y los argumentos que aceptan.
        """
        self.write_chat("Comandos disponibles:")
        [self.write_chat(f"- {cmd}") for cmd in self.commands.keys()]

        # FALTA MOSTRAR LOS ARGUMENTOS DE CADA COMANDO
    
    @command("chstate")
    def change_agent_state(self, agent_name: str):
        """
        Cambia el estado de un agente de activo a inactivo o viceversa.

        :param agent_name: Nombre del agente a cambiar el estado.
        """
        agent = self.search_agent(agent_name)
        if agent:
            agent.active = not agent.active
            status = "Activo" if agent.active else "Inactivo"
            msg = f"El agente {agent_name} ahora está {status}"
            self.write_chat(msg) # Se muestra un mensaje en el chat.
            self.__print_info(msg) # Se muestra un mensaje en la consola.
        else:
            self.write_chat(f"No se ha encontrado el agente {agent_name}")

    # faltan els metodes show_methods i execute_agent i execute_method

    def run(self):
        """
        Método principal para ejecutar el framework. Consiste en un bucle infinito
        que lee los mensajes del chat y ejecuta los comandos correspondientes.
        """

        msg = "Framework de agentes iniciado. Usa el prefijo 'af: ' para ejecutar comandos."
        self.__print_info(msg)
        self.write_chat(msg)

        while True:
            # Se lee el último mensaje del chat.
            message = self.read_chat()

            # Si empieza por "af: ", se considera un comando del framework.
            if message.startswith("af: "):
                # Se obtiene el comando y los argumentos.
                command = message.split(" ")[1]
                args = message.split(" ")[2:]

                # Si el comando es "show_agents", se muestran los agentes.
                if command == "show_agents":
                    self.show_agents()

                # Si el comando es "say_hi", se envía un mensaje desde todos los agentes activos.
                elif command == "say_hi":
                    self.say_hi()

                # Si el comando es "show_methods", se muestran los métodos de un agente.
                elif command == "show_methods":
                    agent_name = args[0]
                    agent = self.search_agent(agent_name)
                    if agent:
                        agent.show_methods()
                    else:
                        self.write_chat(f"No se ha encontrado el agente {agent_name}")

                # Si el comando es "execute", se ejecuta un agente.
            else:
                # No se hace nada si el mensaje no empieza por "af: ". 
                # Ya que no es un comando del framework.
                pass

            # Esperar un segundo para no saturar el servidor.
            time.sleep(1)

