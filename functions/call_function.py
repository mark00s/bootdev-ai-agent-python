from google.genai import types

from config import WORKING_DIR
from consts import FUNCTIONS


def call_function(function_call_part: types.FunctionCall, verbose=False):
    function_name = function_call_part.name

    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name in FUNCTIONS:
        args = dict(function_call_part.args)
        args["working_directory"] = WORKING_DIR
        exec_func = FUNCTIONS[function_name]
        function_result = exec_func(**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
