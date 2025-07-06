import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
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

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    res = client.models.generate_content(
        model=model,
        contents=messages,
    )

    print(res.text)
    if flag_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
