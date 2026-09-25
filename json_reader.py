"""
JSON File Reader
"""

import json

def load_json(file_path):
    """Read and parse a JSON file. Returns the Python object."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def main():
    file_path = input("Enter the path of the JSON file: ").strip()

    try:
        data = load_json(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except json.JSONDecodeError as error:
        print(f"Error: Invalid JSON in '{file_path}'.")
        print(f"Details: {error}")
        return
    except PermissionError:
        print(f"Error: Permission denied while reading '{file_path}'.")
        return

    print("\n----- Formatted Output -----")
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
