import subprocess
import sys
import os


def compress_pdf(input_file, output_file, compression_level=0):
    """
    Compress a PDF file using Ghostscript.

    Parameters:
    - input_file (str): Path to the input PDF file.
    - output_file (str): Path where the output PDF will be saved.
    - compression_level (int): Compression quality from 0 to 4.
      0: Default
      1: Screen quality (lowest)
      2: eBook quality (low)
      3: Printer quality (high)
      4: Prepress quality (highest)
    """
    # Define the Ghostscript PDF settings based on compression level
    quality_settings = {
        0: "/default",
        1: "/screen",
        2: "/ebook",
        3: "/printer",
        4: "/prepress",
    }

    # Validate compression level
    if compression_level not in quality_settings:
        print("Invalid compression level. Using default setting.")
        compression_level = 0

    # Construct the Ghostscript command
    gs_command = [
        "gs",  # Command for Ghostscript; use 'gswin64c' or 'gswin32c' on Windows
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={quality_settings[compression_level]}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_file}",
        input_file,
    ]

    # Adjust Ghostscript command for Windows if necessary
    if os.name == "nt":
        gs_command[0] = r"C:\Program Files\gs\gs10.04.0\bin\gswin64c.exe"

    try:
        # Run the Ghostscript command
        subprocess.check_call(gs_command)
        print(f"Compressed PDF saved as '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print("Ghostscript error:", e)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python compress_pdf.py input_file output_file [compression_level]"
        )
        print("\nCompression levels:")
        print("0: Default compression")
        print("1: Screen quality (lowest resolution)")
        print("2: eBook quality (medium resolution)")
        print("3: Printer quality (high resolution)")
        print("4: Prepress quality (maximum quality)")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    # Set compression level if provided, else default to 0
    compression = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    compress_pdf(input_pdf, output_pdf, compression)
