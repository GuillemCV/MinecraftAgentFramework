from framework.MinecraftAgentFramework import MinecraftAgent, MinecraftFramework
import framework.mcpi.minecraft as minecraft
import framework.mcpi.block as block

# Conectar al servidor de Minecraft
#mc = minecraft.Minecraft.create()

# Crear una instancia del framework
mc = None
framework = MinecraftFramework(mc)

# Crear algunos agentes
agent1 = MinecraftAgent(name="Agente1", active=True, mc=mc)
agent2 = MinecraftAgent(name="Agente2", active=False, mc=mc)
agent3 = MinecraftAgent(name="Agente1", active=True, mc=mc)
agent4 = MinecraftAgent(name="Agente4", active=True, mc=mc)

# Añadir los agentes al framework
framework.add_agent(agent1)
framework.add_agent(agent2)
framework.add_agent(agent3)
framework.add_agent(agent4)

# Eliminar un agente
framework.remove_agent("Agente8")
framework.remove_agent("Agente2")

# Enviar un mensaje desde todos los agentes activos
#framework.broadcast_message("Hola desde el framework de agentes!")

#framework.show_agents()

agent1_method = agent1.get_methods_names()
[print(f"Agente1: {method}") for method in agent1_method]
