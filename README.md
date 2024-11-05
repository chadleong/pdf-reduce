# PDF Compression Script

This script compresses a PDF file using Ghostscript. It supports various compression levels and can be run on both Windows and Linux.

## Usage

To compress a PDF file, run the following command:

```bash
python compress_pdf.py input_file output_file [compression_level]
```

Replace `input_file` with the path to the input PDF file, `output_file` with the path where the compressed PDF will be saved, and `compression_level` with the desired compression level (optional, default is 0).

## Compression Levels

The compression level determines the quality of the compressed PDF. The higher the level, the higher the resolution and the longer the compression time. The following table shows the compression levels and their corresponding Ghostscript settings:

| Compression Level | Ghostscript Settings |
| ----------------- | -------------------- |
| 0                 | /default             |
| 1                 | /screen              |
| 2                 | /ebook               |
| 3                 | /printer             |
| 4                 | /prepress            |

## Example

To compress a PDF file with the default compression level (0), run the following command:

```bash
python compress_pdf.py input_file output_file
```

This will compress the PDF file and save it as `output_file`.
