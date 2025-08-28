# PDF Page Extractor

A simple Python script to extract a specific range of pages (inclusive) from a PDF file and save them as a new document. This project uses the `pypdf` library.

## Prerequisites

- Python 3.7+

## Setup and Installation

Follow these steps to set up your local environment.

1.  **Clone the repository or download the files.**

2.  **Navigate into the project directory:**

    ```bash
    cd /path/to/your/project
    ```

3.  **Create a virtual environment:**
    This will create an isolated environment in a folder named `venv`.

    ```bash
    python -m venv venv
    ```

    *(On macOS or Linux, you may need to use `python3`)*

4.  **Activate the virtual environment:**

    - **On Windows (CMD):**
      ```cmd
      venv\Scripts\activate
      ```
    - **On Windows (PowerShell):**
      ```powershell
      .\venv\Scripts\Activate.ps1
      ```
    - **On macOS & Linux:**
      ```bash
      source venv/bin/activate
      ```

    Your terminal prompt should now be prefixed with `(venv)`.

5.  **Install the required packages:**
    This command reads the `requirements.txt` file and installs the necessary libraries inside your virtual environment.

    ```bash
    pip install -r requirements.txt
    ```

6.  **(Recommended) Select the Interpreter in your Editor:**
    To ensure your code editor (like VS Code or PyCharm) uses the packages you just installed, you should select the interpreter from your virtual environment.

    - **In Visual Studio Code:** Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`), search for `Python: Select Interpreter`, and choose the Python interpreter located inside your `venv` folder. It should be automatically recommended and marked with a star.

---

## Usage

1.  Place the PDF file you want to process into the same directory as `main.py`.

2.  Open the `main.py` file and modify the configuration variables at the bottom of the file to set your input file and the page range. **The name of the output file is now automatically generated** based on the input file and the selected page numbers.

    ```python
    if __name__ == "__main__":
        # --- Configuration ---
        # Define the input file and the desired page range.
        INPUT_PDF_PATH = Path("mon_document.pdf") # <-- Your input PDF
        START_PAGE_NUM = 3                       # <-- The start page of the section
        END_PAGE_NUM = 60                        # <-- The end page of the section

        # The output file will be named automatically, for example: "mon_document_3-60.pdf"
    ```

3.  Run the script from your activated terminal:

    ```bash
    python main.py
    ```

If successful, a confirmation message will be printed, and the new PDF file will be created in your project directory. Any errors (e.g., file not found, invalid page range) will also be clearly displayed.