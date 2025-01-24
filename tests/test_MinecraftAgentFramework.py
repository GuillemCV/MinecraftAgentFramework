import unittest
from framework.MinecraftAgentFramework import *
from framework.mcpi.minecraft import Minecraft
import framework.mcpi.block as block


class TestMinecraftAgentFramework(unittest.TestCase):

    def setUp(self):
        self.mc = Minecraft.create()
        self.agent = MinecraftAgent(name="TestAgent", active=True, info="Test Agent", mc=self.mc)
        self.framework = MinecraftFramework(mc=self.mc)
        self.framework.add_agent(self.agent)

    def test_executable_decorator(self):
        @executable
        def test_method():
            pass

        self.assertTrue(hasattr(test_method, "executable"))
        self.assertTrue(test_method.executable)

    def test_command_decorator(self):
        @command("testcmd")
        def test_method():
            pass

        self.assertTrue(hasattr(test_method, "command"))
        self.assertEqual(test_method.command, "testcmd")

    def test_add_agent(self):
        self.assertIn(self.agent, self.framework.agents)

    def test_remove_agent(self):
        self.framework.remove_agent("TestAgent")
        self.assertNotIn(self.agent, self.framework.agents)

    def test_send_message(self):
        self.agent.send_message("Hello")

    def test_receive_message(self):
        message = self.agent.receive_message()
        self.assertEqual(message, "")

    def test_tp_player(self):
        self.agent.tp_player(10, 20, 30)

    def test_get_player_pos(self):
        pos = self.agent.get_player_pos()
        self.assertEqual(pos.x, 10)
        self.assertEqual(pos.y, 20)
        self.assertEqual(pos.z, 30)

    def test_place_block(self):
        self.agent.place_block(10, 20, 30, block.STONE)

    def test_destroy_block(self):
        self.agent.destroy_block(10, 20, 30)

    def test_show_methods(self):
        self.agent.show_methods()

    def test_execute_agent(self):
        self.framework.execute_agent("TestAgent")

    def test_change_agent_state(self):
        self.framework.change_agent_state("TestAgent")
        self.assertFalse(self.agent.active)
        self.framework.change_agent_state("TestAgent")
        self.assertTrue(self.agent.active)

    def test_show_agents(self):
        self.framework.show_agents()

    def test_help(self):
        self.framework.help()

    def test_execute_method(self):
        self.framework.execute_method("TestAgent", "show_methods")


if __name__ == "__main__":
    unittest.main()
