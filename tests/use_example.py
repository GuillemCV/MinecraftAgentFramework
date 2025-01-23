from framework.MinecraftAgentFramework import MinecraftAgent, MinecraftFramework
import framework.mcpi.minecraft as minecraft
import framework.mcpi.block as block
from agents.TntAgent import TntAgent

# Crear una instancia de Minecraft
mc = minecraft.Minecraft.create()

# Crear una instancia del framework
framework = MinecraftFramework(mc)

# Crear algunos agentes
agent1 = MinecraftAgent(name="Agente1", active=False, info="", mc=mc)
agent2 = MinecraftAgent(name="Agente2", active=False, info="", mc=mc)
agent3 = MinecraftAgent(name="Agente1", active=True, info="", mc=mc)
agent4 = MinecraftAgent(name="Agente4", active=True, info="", mc=mc)
agent_tnt = TntAgent(name="TntAgent", active=True, mc=mc)

# Añadir los agentes al framework
framework.add_agent(agent1)
framework.add_agent(agent2)
framework.add_agent(agent3) # No se añadirá, ya existe un agente con el mismo nombre
framework.add_agent(agent4)
framework.add_agent(agent_tnt)

# Eliminar un agente
framework.remove_agent("Agente8") # No se eliminará, no existe un agente con ese nombre
framework.remove_agent("Agente2") # Se eliminará el agente con nombre "Agente2"
 
# Ejecutar el framework
framework.run()
