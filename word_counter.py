"""
Word Counter from Text File
"""


def count_file(file_path):
    """Return (lines, words, characters, word frequency dict) for a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split() 
    characters = len(content)

    cleaned_words = [word.strip(".,!?;:\"'()[]{}").lower() for word in words]
    cleaned_words = [word for word in cleaned_words if word]

    frequency = {}
    for word in cleaned_words:
        frequency[word] = frequency.get(word, 0) + 1

    return len(lines), len(words), characters


def main():
    file_path = input("Enter the path of the text file: ").strip()

    try:
        line_count, word_count, char_count = count_file(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except IsADirectoryError:
        print(f"Error: '{file_path}' is a directory, not a file.")
        return
    except UnicodeDecodeError:
        print("Error: The file could not be read as a text file (encoding issue).")
        return

    print("\n----- File Statistics -----")
    print(f"Lines      : {line_count}")
    print(f"Words      : {word_count}")
    print(f"Characters : {char_count}")

if __name__ == "__main__":
    main()
