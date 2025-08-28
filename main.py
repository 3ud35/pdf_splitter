from pathlib import Path
from pypdf import PdfReader, PdfWriter


def extract_pages_from_pdf(input_path: Path, output_path: Path, start_page: int, end_page: int) -> None:
    """
    Extracts a range of pages from a source PDF and saves them into a new file.

    Args:
        input_path: The path to the source PDF file.
        output_path: The path where the new PDF file will be saved.
        start_page: The first page number to include (1-based index).
        end_page: The last page number to include (inclusive).

    Raises:
        FileNotFoundError: If the input PDF file does not exist.
        ValueError: If the specified page range is invalid.
    """
    if not input_path.is_file():
        raise FileNotFoundError(f"Source file not found at: {input_path}")

    pdf_reader = PdfReader(input_path)
    total_pages = len(pdf_reader.pages)

    if not (1 <= start_page <= end_page <= total_pages):
        raise ValueError(f"Invalid page range: {start_page}-{end_page}. " f"The document has {total_pages} pages.")

    pdf_writer = PdfWriter()
    # Page indices are 0-based, so we subtract 1 from the start page.
    for page_num in range(start_page - 1, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)


if __name__ == "__main__":
    # --- Configuration ---
    # Define the input file, output file, and the desired page range.
    INPUT_PDF_PATH = Path("mon_document.pdf")
    START_PAGE_NUM = 3
    END_PAGE_NUM = 60
    OUTPUT_PDF_PATH = Path(f"{INPUT_PDF_PATH.stem}_{START_PAGE_NUM}-{END_PAGE_NUM}.pdf")

    # --- Execution ---
    try:
        extract_pages_from_pdf(
            input_path=INPUT_PDF_PATH,
            output_path=OUTPUT_PDF_PATH,
            start_page=START_PAGE_NUM,
            end_page=END_PAGE_NUM,
        )
        print(f"Successfully created '{OUTPUT_PDF_PATH}' with pages " f"{START_PAGE_NUM} through {END_PAGE_NUM}.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
