# PDF Page Extractor

A simple Python script to extract a specific range of pages (inclusive) from a PDF file and save them as a new document. This project uses the `pypdf` library.

## Prerequisites

- Python 3.10+

## Setup and Installation

Follow these steps to set up your local environment.

1.  **Clone the repository or download the files.**

2.  **Navigate into the project directory:**

    ```bash
    cd /path/to/your/project
    ```

3.  **Create a virtual environment:**
    This will create an isolated environment in a folder named `.venv`.

    ```bash
    python -m venv .venv
    ```

    *(On macOS or Linux, you may need to use `python3`)*

4.  **Activate the virtual environment:**

    - **On Windows (CMD):**
      ```cmd
      .venv\Scripts\activate
      ```
    - **On Windows (PowerShell):**
      ```powershell
      .\.venv\Scripts\Activate.ps1
      ```
    - **On macOS & Linux:**
      ```bash
      source .venv/bin/activate
      ```

    Your terminal prompt should now be prefixed with `(.venv)`.

5.  **Install the required packages:**
    This command reads the `requirements.txt` file and installs the necessary libraries inside your virtual environment.

    ```bash
    pip install -r requirements.txt
    ```

6.  **(Recommended) Select the Interpreter in your Editor:**
    To ensure your code editor (like VS Code or PyCharm) uses the packages you just installed, you should select the interpreter from your virtual environment.

    - **In Visual Studio Code:** Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`), search for `Python: Select Interpreter`, and choose the Python interpreter located inside your `.venv` folder. It should be automatically recommended and marked with a star.

---

## Usage

1.  Run the script from your activated terminal:

    ```bash
    python main.py
    ```

2.  Enter the path of the PDF file when prompted (quotes around the path are ignored). Both values can also be given as arguments, which skips the prompts: `python main.py my_document.pdf 1-10,15-20`.

3.  Enter the pages to extract (1-based, inclusive). Separate several extractions with commas; a single number extracts one page:

    ```
    1-50          one extraction
    1-10,15-20    two extractions in one go
    3,7-9         page 3, then pages 7 to 9
    ```

Each extraction is saved next to the source file and named automatically from the input name and the range, for example `my_document_3-60.pdf`. If a file with that name already exists, you are asked before it is overwritten.

Errors (file not found, invalid or out-of-bounds page range) are printed, and the script exits with a non-zero status if anything failed.
