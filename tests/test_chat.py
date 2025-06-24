from functions import create_agent
from agents import Runner

EXAMPLES = [
    "Искам да проследя поръчката си",
    "Искам да ме добавиш в имейл листа",
    "Препоръчай ми Nike обувки",
]

if __name__ == "__main__":
    agent = create_agent()
    for query in EXAMPLES:
        print("Query:", query)
        result = Runner.run_sync(agent, input=query)
        print("Response:", result.final_output)
        print()
