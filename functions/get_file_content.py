import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        working_dir_absol = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_absol, file_path))
        print(target_dir)

        valid_target_dir = os.path.commonpath([working_dir_absol, target_dir]) == working_dir_absol

        if not valid_target_dir:
            return f"Error: Cannot list {file_path} as it is outside the permitted working directory"
    
        if not os.path.isfile(target_dir):
            return f"Error: {file_path} is not a file"
    
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(MAX_CHARS+1):
                file_content_string += f'[...File "{file_path}" trunctated at {MAX_CHARS} characters]'

        return file_content_string
    
    except Exception as e:
        return f"Error {e}"