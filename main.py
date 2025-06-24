import os
from agents import Agent, Runner


def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Please set the OPENAI_API_KEY environment variable.")

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
    )

    result = None
    print("Type 'exit' or 'quit' to stop the chat.")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user_input.lower() in {"exit", "quit"}:
            break

        context = result.context_wrapper.context if result else None
        previous_id = result.last_response_id if result else None

        result = Runner.run_sync(
            agent,
            input=user_input,
            context=context,
            previous_response_id=previous_id,
        )

        print("Assistant:", result.final_output)


if __name__ == "__main__":
    main()
