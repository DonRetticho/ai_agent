from google.genai import types

from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def call_function(function_call, verbose=False):

    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    FUNCTIONS = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    function_name = function_call.name
    func = FUNCTIONS.get(function_name)

    if function_name not in FUNCTIONS:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    args = dict(function_call.args)
    args["working_directory"] = "./calculator"

    result = func(**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": result},
            )
        ],
    )