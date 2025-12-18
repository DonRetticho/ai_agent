import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Excecutes the specified file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
            "arguments": types.Schema(
                type=types.Type.STRING,
                description="Additional arguments that can be given to the run command"
            )
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_absol = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_absol, file_path))
        #print(target_dir)

        valid_target_dir = os.path.commonpath([working_dir_absol, target_dir]) == working_dir_absol

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]

        if args:
            command.extend(args)

        running_command = subprocess.run(
            command,
            cwd=working_dir_absol, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            timeout=30, 
            text=True,
            )
        
        if running_command.returncode != 0:
            output = (
                f'Process exited with code {running_command.returncode}\n'
                f'STDOUT: {running_command.stdout}\n'
                f'STDERR: {running_command.stderr}'
            )
        
        elif not running_command.stdout and not running_command.stderr:
            output = f'No output produced'

        else:
            output = (
                f'STDOUT: {running_command.stdout}\n'
                f'STDERR: {running_command.stderr}'
            )
        

        return output
    
    except Exception as e:
        return f"Error: executing Python file {e}"