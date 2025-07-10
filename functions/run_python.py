import os
from subprocess import run


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed = run(
            ["python3", abs_file_path],
            timeout=30,
            check=True,
            capture_output=True,
            cwd=abs_working_dir,
        )
        output = ""
        if completed.stdout:
            output += f"STDOUT: {completed.stdout}"
        if completed.stderr:
            output += f"STDERR: {completed.stderr}"
        if completed.returncode:
            output += f"Process exited with code {completed.returncode}"
        if not output:
            output += "No output produced."
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
