import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes the specified content to a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is intended to be written to the specified file"
            )
        },
    ),
)

def write_file(working_directory, file_path, content):
    try:
        working_dir_absol = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_absol, file_path))

        valid_target_dir = os.path.commonpath([working_dir_absol, target_dir]) == working_dir_absol

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        parent = os.path.dirname(target_dir)
        if parent:  # only if non-empty
            os.makedirs(parent, exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"