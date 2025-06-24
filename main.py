import os
from agents import Runner
from functions import create_agent


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Please set the OPENAI_API_KEY environment variable.")
    
    agent = create_agent()
    
    print("Type 'exit' or 'quit' to stop the chat.")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user_input.lower() in {"exit", "quit"}:
            break
        
        result = Runner.run_sync(agent, input=user_input)
        print("Assistant:", result.final_output)


if __name__ == "__main__":
    main()