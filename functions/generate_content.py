from google.genai import types, Client
from available_functions import available_functions
from config import SYSTEM_PROMPT
from functions.call_function import call_function


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

    if not res.function_calls:
        return res.text

    function_responses = []
    for function_call in res.function_calls:
        call_result = call_function(function_call, verbose)
        try:
            resp = call_result.parts[0].function_response.response
            function_responses.append(call_result.parts[0])
            if verbose:
                print(f"-> {resp}")
        except AttributeError as e:
            raise Exception("empty function call result") from e
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
