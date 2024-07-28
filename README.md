# PDF Resizer

This Python script allows you to resize PDF files to a specified page size and orientation. It can be used to resize all PDF files in a directory and save the resized versions in a specified output directory.

## Features

- Resize PDF pages to a specified size (e.g., A4, A5) and orientation (portrait or landscape).
- Batch process all PDFs in a directory.
- Easy to use with minimal setup.

## Installation

Make sure you have Python and the required libraries installed:

```bash
pip install PyPDF2 reportlab
```

## Usage

### Example Script

Create a `resize_pdfs.py` file with the following content to batch process all PDFs in a directory:

```python
import os
from pdf_resizer import resize_pdf
from reportlab.lib.pagesizes import A4, A5, landscape, portrait

# Define the input and output directories
input_dir = '/path/to/input/directory'
output_dir = '/path/to/output/directory'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all PDF files in the input directory
pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]

# Resize each PDF and save the result in the output directory
for pdf_file in pdf_files:
    input_pdf_path = os.path.join(input_dir, pdf_file)
    output_pdf_path = os.path.join(output_dir, pdf_file)
    resize_pdf(input_pdf_path, output_pdf_path, A5, landscape)

print("All PDFs have been resized and saved in the output directory.")
```

### Running the Script

To resize all PDFs in the specified input directory to A5 landscape, simply run:

```bash
python resize_pdfs.py
```

### Customizing the Resizing

You can customize the target size and orientation by modifying the parameters passed to the `resize_pdf` function in `resize_pdfs.py`. For example, to resize to A4 portrait:

```python
resize_pdf(input_pdf_path, output_pdf_path, A4, portrait)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
