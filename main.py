import os
import json
import openai
from prompts import SYSTEM_PROMPT
from functions import track_order, add_to_email_list, create_agent


def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Please set the OPENAI_API_KEY environment variable.")

    tools = create_agent()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Type 'exit' or 'quit' to stop the chat.")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user_input.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_input})
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            functions=tools,
            function_call="auto",
        )

        message = response.choices[0].message
        messages.append({"role": message.role, "content": message.content or ""})

        if message.function_call:
            name = message.function_call.name
            args = json.loads(message.function_call.arguments or "{}")
            if name == "track_order":
                result = track_order(**args)
            elif name == "add_to_email_list":
                result = add_to_email_list(**args)
            else:
                result = f"No handler for {name}"
            messages.append({"role": "function", "name": name, "content": result})

            follow_up = openai.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
            )
            message = follow_up.choices[0].message
            messages.append({"role": message.role, "content": message.content or ""})

        print("Assistant:", message.content)


if __name__ == "__main__":
    main()
