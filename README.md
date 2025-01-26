[![codecov](https://codecov.io/github/GuillemCV/MinecraftAgentFramework/graph/badge.svg?token=SPH9M0FDKY)](https://codecov.io/github/GuillemCV/MinecraftAgentFramework)
# Minecraft Agent Framework

Minecraft Agent Framework es un framework para crear, gestionar y ejecutar agentes en un servidor de Minecraft. Los agentes pueden interactuar con el mundo de Minecraft y realizar diversas acciones, como escribir en el chat, leer el chat, teletransportar al jugador, leer la posición del jugador, colocar bloques y romper bloques.

## Requisitos

- Python
- Minecraft Java Edition versión 1.12
- Servidor de AdventuresInMinecraft

## Instalación

1. Clonar el repositorio del servidor de AdventuresInMinecraft según el sistema operativo que estés utilizando:
    - [Windows]:
    ```sh 
    git clone https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-PC.git minecraft_server
    ```

    - [Linux]: 
    ```sh 
    git clone https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-Linux.git minecraft_server
    ```

    - [MacOS]:
    ```sh
    git clone https://github.com/AdventuresInMinecraft/AdventuresInMinecraft-Mac.git minecraft_server
    ```
2. Clonar el repositorio MinecraftAgentFramework:
    ```sh
    git clone https://github.com/GuillemCV/MinecraftAgentFramework.git
    ```
3. Instalar las dependencias:
    ```sh
    pip install -e .
    ```
4. Iniciar el servidor de AdventuresInMinecraft:
   
    Ejecutar el script StartServer, que se encuentra en el repositorio clonado en el 1r paso, y esperar a que el servidor termine de iniciarse.
6. Iniciar Minecraft Java Edition versión 1.12 y conectarse al servidor:
   
    Para ello, hay que crear un nuevo servidor en el apartado de "Multijugador", cuya dirección sea localhost, y conectarse a él.
8. Ejecutar el programa use_example.py de la carpeta tests para comprovar que todo funcione correctamente.

## Uso

### Crear un agente
Para crear un agente, hereda de la clase MinecraftAgent y sobrescribe el método main_execute. También puedes definir métodos adicionales y decorarlos con @executable para que puedan ser ejecutados desde el chat de Minecraft. Para interactuar con el mundo de Minecraft hay que usar los métodos definidos en la clase MinecraftAgent. Hay que tener en cuenta que los métodos pensados para ser ejecutados mediante comandos a través del chat de Minecraft, como el método main_execute o cualquier método anotado con @executable, reciben sus argumentos como objetos de tipo str (string). Por lo que el programador deberá convertir los argumentos al tipo adecuado, lanzando una excepción en caso de error. Por último, mencionar que en estos métodos no se admite el parámetro **kwargs, para que acepten un número variable de argumentos hay que usar *args, como en el caso de main_execute. En este caso habrá que comprobar que el número de elementos en args sea igual al número de argumentos necesarios y lanzar una excepción en caso contrario.
Ejemplo:
   
<p align="center">
  <img src="https://github.com/user-attachments/assets/69123fd6-ef78-4b0d-8fa3-895b3a187fb6" alt="create_agent" width="600">
</p>

### Añadir agentes al framework y ejecutarlo
Usa la libreria mcpi para crear una instancia de la clase Minecraft, que es la que permite la comunicación con el servidor. Luego crea una instancia de MinecraftFramework, crea instancias de tus agentes, añadelos al framework y ejecutalo.
Ejemplo:

<p align="center">
  <img src="https://github.com/user-attachments/assets/bc82c664-5b62-4c47-98a1-54f34fb62c75" alt="add_and_execute" width="600">
</p>

### Ejecutar comandos desde el chat de Minecraft
Los comandos empiezan por el prefijo "af:", seguido del comando y de los argumentos necesarios, todo esto separado por espacios:
        
    af: comando [arg1] [arg2] ... [argN]

Usa el comando "af: help" para ver todos los comandos disponibles y los argumentos que reciben.

        




   
    
