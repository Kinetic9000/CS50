import sys
import re

def count_lines_of_code(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    code_lines = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            code_lines += 1
    
    return code_lines

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <python_file.py>")
    
    file_path = sys.argv[1]
    if not file_path.endswith('.py'):
        sys.exit("File must be a Python file ending with .py")
    
    try:
        loc = count_lines_of_code(file_path)
        print(loc)
    except FileNotFoundError:
        sys.exit(f"File {file_path} does not exist")

if __name__ == "__main__":
    main()