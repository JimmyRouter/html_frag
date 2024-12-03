import re


def open_file(file_path: str) -> str:
    """
    Reads the content of an HTML file, cleans up extra line breaks,
    and optionally adjusts spacing around HTML tags.
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    try:
        with open(file_path, 'r', encoding='utf-8') as html_file:
            content = html_file.read()
        content = re.sub(r'\n{2,}', '\n', content)
        return content

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")

    except UnicodeDecodeError:
        raise ValueError("File encoding is not valid UTF-8.")

if __name__ == '__main__':
    try:
        print(open_file('for_tests.html'))
    except Exception as e:
        print(f"Error: {e}")
