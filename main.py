import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    if not openai.api_key:
        raise RuntimeError("Please set the OPENAI_API_KEY environment variable.")
    messages = []
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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        reply = response["choices"][0]["message"]["content"].strip()
        messages.append({"role": "assistant", "content": reply})
        print("Assistant:", reply)


if __name__ == "__main__":
    main()
