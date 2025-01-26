from framework.MinecraftAgentFramework import MinecraftFramework
from mcpi.minecraft import Minecraft
from agents.InsultAgent import InsultAgent
from agents.OracleAgent import OracleAgent
from agents.RandomTpAgent import RandomTpAgent
from agents.MathAgent import MathAgent
from agents.TntAgent import TntAgent
from agents.BlockDestroyAgent import BlockDestroyAgent

# Crear una instancia de Minecraft
mc = Minecraft.create()

# Crear una instancia del framework
framework = MinecraftFramework(mc)

# Crear algunos agentes
tnt_agent = TntAgent(name="TntAgent", active=True, mc=mc)
insult_agent = InsultAgent(name="InsultAgent", active=True, mc=mc)
oracle_agent = OracleAgent(name="OracleAgent", active=True, mc=mc)
random_tp_agent = RandomTpAgent(name="RandomTpAgent", active=True, mc=mc)
block_destroyer = BlockDestroyAgent(name="BlockDestroyAgent", active=True, mc=mc)
math_agent = MathAgent(name="MathAgent", active=True, mc=mc)

# Añadir los agentes al framework
framework.add_agent(tnt_agent)
framework.add_agent(insult_agent)
framework.add_agent(oracle_agent)
framework.add_agent(random_tp_agent)
framework.add_agent(block_destroyer)
framework.add_agent(math_agent)

# Ejecutar el framework
framework.run()
