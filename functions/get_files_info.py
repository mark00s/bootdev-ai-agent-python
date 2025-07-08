import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        files_metadata = []
        for filename in os.listdir(target_dir):
            filepath = f"{target_dir}/{filename}"
            file_size = 0
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isfile(filepath)
            files_metadata.append(
                f" - {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_metadata)
    except Exception as e:
        return f"Error listing files: {e}"
