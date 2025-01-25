import inspect
import unittest
from framework.MinecraftAgentFramework import (
    MinecraftAgent,
    MinecraftFramework,
    executable,
    command,
    method_execution,
)
from mcpi.minecraft import Minecraft
import mcpi.block as block
from unittest.mock import MagicMock


class AgentTest(MinecraftAgent):
    def __init__(self, name, active, mc):
        info = "Test Agent"
        super().__init__(name, active, info, mc)

    def main_execute(self, *args):
        if len(args) < 1:
            raise ValueError("Se necesita al menos un argumento")

        self.send_message("Ejecutado con argumentos: ")
        for arg in args:
            self.send_message(arg)

    @executable
    def test_executable(self, msg):
        # Si no es un string, se lanza una excepción
        if not isinstance(msg, str):
            raise ValueError("El argumento debe ser un string")

        self.send_message(msg)


class TestMinecraftAgentFramework(unittest.TestCase):

    def setUp(self):
        self.mc = Minecraft.create()
        self.agent = AgentTest(name="TestAgent", active=True, mc=self.mc)
        self.framework = MinecraftFramework(mc=self.mc)
        self.framework.add_agent(self.agent)

        # Comprovamos si hay algun jugador conectado, si no hay, se usa Mock.
        try:
            # Si no hay ningún jugador conectado lanzará una excepción.
            self.mc.player.getTilePos()
        except Exception as e:
            self.mc.player.getTilePos = MagicMock()
            print("Usando Mock para mc.player.getTilePos")

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

        result = method_execution(
            method_with_param, inspect.signature(method_with_param).parameters, ["Test"]
        )
        self.assertEqual(result, (True, 1, "I have parameter Test"))

        result = method_execution(
            method_with_param, inspect.signature(method_with_param).parameters, []
        )
        self.assertEqual(result, (False, 1, None))

        result = method_execution(
            method_with_param_args,
            inspect.signature(method_with_param_args).parameters,
            ["Test", "Arg1", "Arg2"],
        )
        self.assertEqual(
            result, (True, 1, "I have parameter Test and args ('Arg1', 'Arg2')")
        )

    # Tests de MinecraftAgent:

    def test_instanciate_MinecraftAgent(self):
        try:
            agent = MinecraftAgent("TestAgent", True, "Test Agent", self.mc)
            self.assertTrue(False)
        except Exception as e:
            print(e)
            self.assertTrue(True)

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
        pos = self.agent.get_player_pos()
        print(pos)
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
        self.agent.main_execute = MinecraftAgent.main_execute
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
        agent = AgentTest(name="TestAgent2", active=True, mc=self.mc)
        self.framework.add_agent(agent)
        self.assertEqual(len(self.framework.agents), 2)
        self.assertNotEqual(self.framework.search_agent("TestAgent2"), None)

        agent = AgentTest(name="TestAgent", active=True, mc=self.mc)
        self.framework.add_agent(agent)
        self.assertEqual(len(self.framework.agents), 2)

    def test_remove_agent(self):
        self.framework.add_agent(AgentTest(name="TestAgent2", active=True, mc=self.mc))
        self.assertEqual(len(self.framework.agents), 2)
        self.framework.remove_agent("TestAgent232")
        self.assertEqual(len(self.framework.agents), 2)
        self.framework.remove_agent("TestAgent2")
        self.assertEqual(len(self.framework.agents), 1)

    def test_say_hi(self):
        self.framework.say_hi()
        self.framework.remove_agent("TestAgent")
        self.framework.say_hi()
        self.assertTrue(True)

    def test_show_agents(self):
        self.framework.show_agents()
        self.framework.remove_agent("TestAgent")
        self.framework.show_agents()
        self.assertTrue(True)

    def test_help(self):
        self.framework.help()
        self.assertTrue(True)

    def test_change_agent_state(self):
        self.framework.change_agent_state("TestAgent")
        self.assertFalse(self.framework.search_agent("TestAgent").active)
        self.framework.change_agent_state("TestAgent")
        self.assertTrue(self.framework.search_agent("TestAgent").active)

        self.framework.change_agent_state("TestAgent2")

    def test_show_methods(self):
        self.framework.show_methods("TestAgent")
        self.framework.show_methods("TestAgent2")
        self.assertTrue(True)

    def test_show_info(self):
        self.framework.show_info("TestAgent")
        self.framework.show_info("TestAgent2")
        self.assertTrue(True)

    def test_execute_agent(self):
        self.framework.execute_agent("TestAgent")
        self.framework.execute_agent("TestAgent", "Test")
        self.framework.execute_agent("TestAgentNotExists")

        self.framework.change_agent_state("TestAgent")
        self.framework.execute_agent("TestAgent")

        self.assertTrue(True)

    def test_execute_method(self):
        self.framework.execute_method("TestAgent2", "test", "Hello World")
        self.framework.change_agent_state("TestAgent")
        self.framework.execute_method("TestAgent", "test", "Hello World")
        self.framework.change_agent_state("TestAgent")
        self.framework.execute_method("TestAgent", "test", 1)
        self.framework.execute_method("TestAgent", "show_methods")
        self.framework.execute_method("TestAgent", "execute")
        self.framework.execute_method("TestAgent", "test_executable", "Hello World")
        self.framework.execute_method("TestAgent", "test_executable", 1)
        self.framework.execute_method("TestAgent", "test_executable")

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
