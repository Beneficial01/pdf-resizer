# PDF Resizer

This Python script resizes PDF pages to a specified format. It uses PyPDF2 and ReportLab libraries.

## Features

- Resize PDF pages to any format (e.g., A5, A4) with ease.

## Installation

1. Clone the repository:
```
git clone https://github.com/YourUsername/pdf-resizer.git
```

2. Install the required libraries:
```
pip install PyPDF2 reportlab
```

## Usage

To resize a PDF to A5 horizontal format, use the following code:

```python
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A5, landscape

def resize_pdf(input_pdf, output_pdf, target_size):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    new_width, new_height = target_size

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        
        page.scale_to(new_width, new_height)
        
        writer.add_page(page)
    
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

if __name__ == '__main__':
    input_pdf_path = 'input.pdf'
    output_pdf_path = 'output.pdf'
    resize_pdf(input_pdf_path, output_pdf_path, landscape(A5))
```

To resize to a different format, simply change `landscape(A5)` to the desired format (e.g., `landscape(A4)` or `A4`).

## Running Tests

Run the test script using:

```
python test_pdf_resizer.py
```

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.
