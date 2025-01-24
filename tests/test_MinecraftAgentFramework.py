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
        
        def method_no_return():
            print("I have no return")
        
        result = method_execution(method_no_return, {}, [])
        # de que tipo es return
        print(result)
   


if __name__ == "__main__":
    unittest.main()
