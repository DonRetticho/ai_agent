import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_absol = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_absol, directory))

        valid_target_dir = os.path.commonpath([working_dir_absol, target_dir]) == working_dir_absol

        if not valid_target_dir:
            return f"Error: Cannot list {directory} as it is outside the permitted working directory"
    
        if not os.path.isdir(target_dir):
            return f"Error: {directory} is not a directory"
    
        convert = []
        filenames = os.listdir(target_dir)

        #print(f"working abs: {working_dir_absol}")
        #print(f"target dir: {target_dir}")
        for items in filenames:
            full_path = os.path.join(target_dir, items)
            #print(f"full path: {full_path}")
            #print(f"items: {items}")
            if os.path.isdir(full_path):
                item_string = f"- {items}: file_size={os.path.getsize(full_path)}, is_dir=True"
                convert.append(item_string)
            else:
                item_string = f"- {items}: file_size={os.path.getsize(full_path)}, is_dir=False"
                convert.append(item_string)

        return "\n".join(convert)

    except Exception as e:
        return f"Error: {e}"

        