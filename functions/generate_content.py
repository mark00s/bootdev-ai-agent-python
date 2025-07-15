from google.genai import types, Client
from available_functions import available_functions
from config import SYSTEM_PROMPT


def generate_content(client: Client, messages, verbose, model="gemini-2.0-flash-001"):
    res = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
        ),
    )

    if verbose:
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
        print("##############################################################")
    if res.function_calls:
        for function_call in res.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(res.text)
