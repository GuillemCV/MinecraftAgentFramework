import inspect
import unittest
from agents import InsultAgent, OracleAgent, RandomTpAgent, MathAgent, TntAgent, BlockDestroyAgent
from framework.MinecraftAgentFramework import MinecraftAgent, MinecraftFramework, executable, command, method_execution
from mcpi.minecraft import Minecraft
import mcpi.block as block



class TestMinecraftAgentFramework(unittest.TestCase):

    def setUp(self):
        self.mc = Minecraft.create()
        self.tnt_agent = TntAgent(name="TntAgent", active=True, mc=self.mc)
        self.insult_agent = InsultAgent(name="InsultAgent", active=True, mc=self.mc)
        self.oracle_agent = OracleAgent(name="OracleAgent", active=True, mc=self.mc)
        self.random_tp_agent = RandomTpAgent(name="RandomTpAgent", active=True, mc=self.mc)
        self.block_destroyer = BlockDestroyAgent(name="BlockDestroyAgent", active=True, mc=self.mc)
        self.math_agent = MathAgent(name="MathAgent", active=True, mc=self.mc)
        

    


if __name__ == "__main__":
    unittest.main()
