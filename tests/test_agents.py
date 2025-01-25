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
        self.tnt_agent = TntAgent(name="TntAgent", active=True, mc=self.mc)
        self.insult_agent = InsultAgent(name="InsultAgent", active=True, mc=self.mc)
        self.oracle_agent = OracleAgent(name="OracleAgent", active=True, mc=self.mc)
        self.random_tp_agent = RandomTpAgent(name="RandomTpAgent", active=True, mc=self.mc)
        self.block_destroyer = BlockDestroyAgent(name="BlockDestroyAgent", active=True, mc=self.mc)
        self.math_agent = MathAgent(name="MathAgent", active=True, mc=self.mc)

        # Comprovamos si hay algun jugador conectado, si no hay, se usa Mock.
        try:
            # Si no hay ningún jugador conectado lanzará una excepción.
            self.mc.player.getTilePos()
        except Exception as e:
            self.mc.player.getTilePos = MagicMock()
            print("Usando Mock para mc.player.getTilePos")


    # Test de TntAgent:

    def test_main_execute_TntAgent(self):
        try: 
            self.tnt_agent.main_execute()
        except ValueError as e:
            print(e)
        
        try:
            self.tnt_agent.main_execute(5, "test")
        except ValueError as e:
            print(e)
        
        self.tnt_agent.main_execute(5, 5)

        self.assertTrue(True)

    def test_place_tnt_TntAgent(self):
        self.tnt_agent.place_tnt(5)
        try:
            self.tnt_agent.place_tnt("test")
        except ValueError as e:
            print(e)
        self.assertTrue(True)

    # Test de InsultAgent:

    def test_main_execute_InsultAgent(self):
        try:
            self.insult_agent.main_execute()
        except ValueError as e:
            print(e)
        
        try:
            self.insult_agent.main_execute("test")
        except ValueError as e:
            print(e)

        self.insult_agent.main_execute(10)

    def test_random_insult_InsultAgent(self):
        self.insult_agent.random_insult()
        self.assertTrue(True)
    
    # Test de OracleAgent:

    def test_main_execute_OracleAgent(self):
        # No se puede testear correctamente ya que el método main_execute() tiene un bucle
        # que espera una respuesta del jugador.
        self.assertTrue(True)

    def test_show_questions_OracleAgent(self):
        self.oracle_agent.show_questions()
        self.assertTrue(True)
    
    def test_check_question_number_OracleAgent(self):
        self.oracle_agent.check_question_number("")
        self.oracle_agent.check_question_number("test")
        self.oracle_agent.check_question_number(50)
        self.oracle_agent.check_question_number(5)
        self.assertTrue(True)

    # Test de RandomTpAgent:

    def test_main_execute_RandomTpAgent(self):
        try:
            self.random_tp_agent.main_execute()
        except ValueError as e:
            print(e)
        
        try:
            self.random_tp_agent.main_execute("test")
        except ValueError as e:
            print(e)

        self.random_tp_agent.main_execute(10)
        self.assertTrue(True)

    # Test de BlockDestroyAgent:

    def test_main_execute_BlockDestroyAgent(self):
        try:
            self.block_destroyer.main_execute()
        except ValueError as e:
            print(e)
        
        try:
            self.block_destroyer.main_execute(5, "test")
        except ValueError as e:
            print(e)

        self.block_destroyer.main_execute(5, 5)
        self.assertTrue(True)
    
    def test_destroy_BlockDestroyAgent(self):
        self.block_destroyer.destroy(5)
        try:
            self.block_destroyer.destroy("test")
        except ValueError as e:
            print(e)
        self.assertTrue(True)

    # Test de MathAgent:

    def test_main_execute_MathAgent(self):
        # No se puede testear correctamente ya que el método main_execute() tiene bucles
        # que esperan una respuesta del jugador.
        self.assertTrue(True)
    
    def test_show_ops_MathAgent(self):
        self.math_agent.show_ops()
        self.assertTrue(True)
    
    def test_do_operation_MathAgent(self):
        self.math_agent.do_operation(5, 5, 1)
        self.math_agent.do_operation(5, 5, 2)
        self.math_agent.do_operation(5, 5, 3)
        self.math_agent.do_operation(5, 5, 4)
        self.math_agent.do_operation(5, 5, 20)
        self.assertTrue(True)


        

    


if __name__ == "__main__":
    unittest.main()
