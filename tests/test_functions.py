import unittest
from functions import create_agent
from agents import Runner

CASES = [
    ("Искам да проследя поръчката си", "track_order"),
    ("Искам да ме добавиш в имейл листа", "add_to_email_list"),
    ("Препоръчай ми Nike обувки", "WebSearchTool"),
]

class AgentToolTests(unittest.TestCase):
    def test_tools(self):
        agent = create_agent()
        for query, _ in CASES:
            with self.subTest(query=query):
                result = Runner.run_sync(agent, input=query)
                self.assertTrue(result.final_output)

if __name__ == "__main__":
    unittest.main()
