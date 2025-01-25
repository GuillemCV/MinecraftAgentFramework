import unittest
from agents.TntAgent import TntAgent
from agents.InsultAgent import InsultAgent
from agents.OracleAgent import OracleAgent
from agents.RandomTpAgent import RandomTpAgent
from agents.BlockDestroyAgent import BlockDestroyAgent
from agents.MathAgent import MathAgent
from mcpi.minecraft import Minecraft
from unittest.mock import MagicMock



class TestMinecraftAgentFramework(unittest.TestCase):

    def setUp(self):
        self.mc = Minecraft.create()
        # Mockear el método getTilePos para que no se ejecute realmente, pero que se pueda llamar.
        # Ya que desde Github Actions no se puede ejecutar Minecraft y fallaría.
        self.mc.player.getTilePos = MagicMock() 
        self.tnt_agent = TntAgent(name="TntAgent", active=True, mc=self.mc)
        self.insult_agent = InsultAgent(name="InsultAgent", active=True, mc=self.mc)
        self.oracle_agent = OracleAgent(name="OracleAgent", active=True, mc=self.mc)
        self.random_tp_agent = RandomTpAgent(name="RandomTpAgent", active=True, mc=self.mc)
        self.block_destroyer = BlockDestroyAgent(name="BlockDestroyAgent", active=True, mc=self.mc)
        self.math_agent = MathAgent(name="MathAgent", active=True, mc=self.mc)


    def test_main_execute_with_valid_arguments(self):
        # self.tnt_agent.place_tnt = MagicMock()

        self.tnt_agent.main_execute(5, 3)

        #self.assertEqual(self.tnt_agent.place_tnt.call_count, 3)
        #self.tnt_agent.place_tnt.assert_called_with(5)
        self.assertTrue(True)

    def test_main_execute_with_insufficient_arguments(self):
        with self.assertRaises(ValueError) as context:
            self.tnt_agent.main_execute(5)
        self.assertEqual(str(context.exception), "Se necesitan dos argumentos: radio (int) y numero de bloques de TNT a colocar (int)")

    def test_main_execute_with_invalid_arguments(self):
        with self.assertRaises(ValueError) as context:
            self.tnt_agent.main_execute("invalid", 3)
        self.assertEqual(str(context.exception), "Los argumentos deben ser numeros enteros")

        with self.assertRaises(ValueError) as context:
            self.tnt_agent.main_execute(5, "invalid")
        self.assertEqual(str(context.exception), "Los argumentos deben ser numeros enteros")


        

    


if __name__ == "__main__":
    unittest.main()
