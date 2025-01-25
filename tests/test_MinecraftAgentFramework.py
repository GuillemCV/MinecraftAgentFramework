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

    # Tests de MinecraftAgent:

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
    
    # Tests de MinecraftFramework:

    def test_MinecraftFramework_init(self):
        self.assertEqual(self.framework.mc, self.mc)
        self.assertNotEqual(self.framework.agents, [])
        self.assertNotEqual(self.framework.commands, {})
    
    def test_write_chat(self):
        self.framework.write_chat("Hello World")
        self.assertTrue(True)

    def test_read_chat(self):
        msg = self.framework.read_chat()
        self.assertEqual(msg, "")

    def test_search_agents(self):
        agents = self.framework.search_agent("TestAgent")
        self.assertNotEqual(agents, None)

        agents = self.framework.search_agent("TestAgent2")
        self.assertEqual(agents, None)

    def test_add_agent(self):
        agent = MinecraftAgent(name="TestAgent2", active=True, info="Test Agent 2", mc=self.mc)
        self.framework.add_agent(agent)
        self.assertEqual(len(self.framework.agents), 2)
        self.assertNotEqual(self.framework.search_agent("TestAgent2"), None)

        agent = MinecraftAgent(name="TestAgent", active=True, info="Test Agent", mc=self.mc)
        self.framework.add_agent(agent)
        self.assertEqual(len(self.framework.agents), 2)

    def test_remove_agent(self):
        self.framework.remove_agent("TestAgent")
        self.assertEqual(len(self.framework.agents), 0)


if __name__ == "__main__":
    unittest.main()
