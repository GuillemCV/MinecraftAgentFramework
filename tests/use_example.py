from framework.MinecraftAgentFramework import MinecraftAgent, MinecraftFramework
import framework.mcpi.minecraft as minecraft
import framework.mcpi.block as block
from agents.TntAgent import TntAgent

"""
# Crear una instancia del framework
mc = None
framework = MinecraftFramework(mc)

# Crear algunos agentes
agent1 = MinecraftAgent(name="Agente1", active=False, mc=mc)
agent2 = MinecraftAgent(name="Agente2", active=False, mc=mc)
agent3 = MinecraftAgent(name="Agente1", active=True, mc=mc)
agent4 = MinecraftAgent(name="Agente4", active=True, mc=mc)
agent_tnt = TntAgent(name="TntAgent", active=True, mc=mc)

# Añadir los agentes al framework
framework.add_agent(agent1)
framework.add_agent(agent2)
framework.add_agent(agent3)
framework.add_agent(agent4)
framework.add_agent(agent_tnt)

# Eliminar un agente
framework.remove_agent("Agente8")
framework.remove_agent("Agente2")
"""
# ejemplos de uso de *args
def test_args(x, *args):
    print("x:", x)
    sum = sumar(*args)
    print("sum:", sum)

def sumar(*args):
    return sum(args)

tuple = (2, 3, 4, 5)
test_args(1, *tuple)

#framework.say_hi()
#framework.show_agents()
#agent_tnt.show_methods()

#framework.run()
