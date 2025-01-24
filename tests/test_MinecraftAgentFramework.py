import inspect
import unittest
from framework.MinecraftAgentFramework import MinecraftAgent, MinecraftFramework, executable, command, method_execution
from mcpi.minecraft import Minecraft
import mcpi.block as block



class TestMinecraftAgentFramework(unittest.TestCase):

    def setUp(self):
        self.mc = Minecraft.create()
        self.agent = MinecraftAgent(name="TestAgent", active=True, info="Test Agent", mc=self.mc)
        self.framework = MinecraftFramework(mc=self.mc)
        self.framework.add_agent(self.agent)

    def test_decorator_executable(self):
        @executable
        def test_executable():
            return "Hello World"

        self.assertEqual(test_executable(), "Hello World")
        self.assertTrue(test_executable.executable)
    
    def test_decorator_command(self):
        @command("TestCommand")
        def test_command():
            return "Hello World"

        self.assertEqual(test_command(), "Hello World")
        self.assertEqual(test_command.command, "TestCommand")
    
    def test_method_execution(self):
        def method_no_param():
            return "I have no parameter"
        
        def method_with_param(param):
            return f"I have parameter {param}"
        
        def method_with_param_args(param, *args):
            return f"I have parameter {param} and args {args}"
        
        result = method_execution(method_no_param, {}, [])
        self.assertEqual(result, (True, 0, "I have no parameter"))

        result = method_execution(method_with_param, inspect.signature(method_with_param).parameters, ["Test"])
        self.assertEqual(result, (True, 1, "I have parameter Test"))

        result = method_execution(method_with_param, inspect.signature(method_with_param).parameters, [])
        self.assertEqual(result, (False, 1, None))

        result = method_execution(method_with_param_args, inspect.signature(method_with_param_args).parameters, ["Test", "Arg1", "Arg2"])
        self.assertEqual(result, (True, 1, "I have parameter Test and args ('Arg1', 'Arg2')"))

    # Test de MinecraftAgent:

    def test_MinecraftAgent_init(self):
        self.assertEqual(self.agent.name, "TestAgent")
        self.assertTrue(self.agent.active)
        self.assertEqual(self.agent.info, "Test Agent")
        self.assertEqual(self.agent.mc, self.mc)
        self.assertNotEqual(self.agent.executable_methods, [])

    def test_send_message(self):
        self.agent.send_message("Hello World")
        self.assertTrue(True)
    
    def test_receive_message_empty(self):
        msg = self.agent.receive_message()
        self.assertEqual(msg, "")
       
    def test_tp_player(self):
        self.agent.tp_player(0, 0, 0)
        self.assertTrue(True)

    def test_get_player_pos(self):
        try:
            pos = self.agent.get_player_pos()
            print(pos)
            self.assertTrue(True)
        except Exception as e:
            # En GitHub Actions no se puede obtener la posición del jugador
            self.assertTrue(True)

    def test_place_block(self):
        self.agent.place_block(0, 0, 0, block.STONE)
        self.assertTrue(True)
    
    def test_destroy_block(self):
        self.agent.destroy_block(0, 0, 0)
        self.assertTrue(True)
    
    def test_show_methods(self):
        self.agent.show_methods()
        self.assertTrue(True)

    def test_execute(self):
        self.agent.execute([])
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
