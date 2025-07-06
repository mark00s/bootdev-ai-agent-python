import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.generate_content import generate_content


def main():
    load_dotenv()
    # flags
    flag_verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print("\nUsage: python main.py <prompt> <flags>")
        print('Example: python main.py "How do I build a calculator app?"')
        print("\n   --verbose: Make app more informative")
        print(
            '\n           example: python main.py "How do I build a calculator app?" --verbose'
        )
        sys.exit(1)

    user_prompt = " ".join(args)
    if flag_verbose:
        print(f"User prompt: {user_prompt}")

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, flag_verbose)


if __name__ == "__main__":
    main()
