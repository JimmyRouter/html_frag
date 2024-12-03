# HTML Message Splitter

**HTML Message Splitter** is a Python tool designed to split large HTML messages into smaller fragments for systems with message size constraints. It ensures that the HTML structure remains valid and formatted correctly.

---

## Features

- Splits large HTML messages into fragments without breaking HTML tags.
- Maintains the correct nesting of block-level tags like `<p>`, `<div>`, `<ul>`, and others.
- Configurable maximum fragment size (`max_len`).
- Supports command-line execution with customizable inputs.
- Includes unit tests for reliability.

---

## Installation
1. Clone the repository and navigate to the project directory:

git clone https://github.com/JimmyRouter/html_frag.git
cd html_frag

2.Install dependencies:
pip install requirements.txt

Usage
Command-line Interface
The script can be executed from the command line to split an HTML file into smaller fragments.

bash
Copy code
python split_msg.py --max-len=<desired_length> <path_to_html_file>
Example:

bash
Copy code
python split_msg.py --max-len=3072 ./source.html

Output
The script outputs fragments to the console in the following format:
fragment #1: <number_of_characters> chars
<content>
---
fragment #2: <number_of_characters> chars
<content>

Project Structure

html_frag/
├── README.md          # Project documentation
├── requirements.txt   # Project dependencies
├── constants.py       # Contains constants like `MAX_LEN` and `BLOCK_TAGS`
├── file_manager.py    # Handles file reading and preprocessing
├── msg_split.py       # Core logic for splitting HTML messages
├── split_msg.py       # CLI script for running the program
├── tests_html_frag.py # Unit tests
├── source.html        # Example input HTML file
└── for_tests.html     # Example input HTML file

Dependencies:

Beautiful Soup: For parsing and manipulating HTML.
Click: For creating the command-line interface.
pytest: For unit testing.