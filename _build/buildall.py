import os

def invoke_command(filename):
    os.system(f"python3 ./_build/MAIN.py {filename}")

if __name__ == "__main__":
    files = os.listdir()
    md_files = [file for file in files if file.endswith('.md')]
    for md_file in md_files:
        invoke_command(md_file)

    os.system("python3 ./_build/MAIN.py")
