import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def write_page_range(pdf_reader: PdfReader, output_path: Path, start_page: int, end_page: int) -> None:
    """
    Writes a range of pages from an already opened PDF into a new file.

    Args:
        pdf_reader: The opened source PDF.
        output_path: The path where the new PDF file will be saved.
        start_page: The first page number to include (1-based index).
        end_page: The last page number to include (inclusive).

    Raises:
        ValueError: If the specified page range is invalid.
    """
    total_pages = len(pdf_reader.pages)

    if not (1 <= start_page <= end_page <= total_pages):
        raise ValueError(f"Invalid page range: {start_page}-{end_page}. The document has {total_pages} pages.")

    pdf_writer = PdfWriter()
    # Page indices are 0-based, so we subtract 1 from the start page.
    for page_num in range(start_page - 1, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)


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

    write_page_range(PdfReader(input_path), output_path, start_page, end_page)


def parse_page_ranges(ranges_str: str) -> list[tuple[int, int]]:
    """
    Parses a string representing page ranges and returns a list of (start, end) tuples.

    A single page number such as "5" is read as the range 5-5.

    Args:
        ranges_str: A string containing page ranges separated by commas, e.g. "1-5,8-10,12".

    Returns:
        A list of tuples, each representing a start and end page number.

    Raises:
        ValueError: If the string is empty or a part is not a valid page or range.
    """
    ranges = []
    for part in ranges_str.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            if "-" in part:
                start, end = (int(value) for value in part.split("-"))
            else:
                start = end = int(part)
        except ValueError:
            raise ValueError(f"Invalid range: '{part}' (expected e.g. 5 or 1-10).") from None
        if start > end:
            raise ValueError(f"Invalid range: '{part}' (start is after end).")
        ranges.append((start, end))

    if not ranges:
        raise ValueError("No page range provided.")
    return ranges


def main(argv: list[str]) -> int:
    """Takes the PDF path and page ranges from the command line, and asks for whatever is missing."""
    if len(argv) > 2:
        print("Usage: main.py [PDF_PATH [PAGE_RANGES]]")
        return 2
    pdf_path_str = argv[0] if argv else input("Enter PDF file path: ")
    pdf_path_str = pdf_path_str.strip().strip("'\"")
    if len(argv) > 1:
        page_ranges_str = argv[1].strip()
    else:
        page_ranges_str = input("Enter page ranges (e.g. 1-50 or 1-10,15-20 for 2 extractions in one go): ").strip()
    input_pdf_path = Path(pdf_path_str).expanduser()

    try:
        page_ranges = parse_page_ranges(page_ranges_str)
        if not input_pdf_path.is_file():
            raise FileNotFoundError(f"Source file not found at: {input_pdf_path}")
        pdf_reader = PdfReader(input_pdf_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

    exit_code = 0
    for start_page, end_page in page_ranges:
        # Output is saved next to the source file.
        output_pdf_path = input_pdf_path.with_name(f"{input_pdf_path.stem}_{start_page}-{end_page}.pdf")
        if output_pdf_path.exists():
            answer = input(f"'{output_pdf_path}' exists. Overwrite? [y/N] ").strip().lower()
            if answer != "y":
                print(f"Skipped '{output_pdf_path}'")
                continue
        try:
            write_page_range(pdf_reader, output_pdf_path, start_page, end_page)
            print(f"Created '{output_pdf_path}'")
        except ValueError as e:
            print(f"Error: {e}")
            exit_code = 1
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
