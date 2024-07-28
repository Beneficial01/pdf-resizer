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

### Cloning the Repository

First, clone the repository and change to the repository directory:

```bash
git clone https://github.com/Beneficial01/pdf-resizer.git
cd pdf-resizer
```

### Running the Script

You can use the provided script `resize_pdfs.py` to resize all PDFs in a directory. The script will take care of resizing and saving the PDFs in a specified output directory. 

1. Open the `resize_pdfs.py` file.
2. Modify the `input_dir` and `output_dir` variables to specify the directories containing your PDFs and where you want to save the resized PDFs.

For example:
```python
# Directory containing the PDFs
input_dir = '/path/to/input/directory'
output_dir = '/path/to/output/directory'
```

3. Run the script:
```bash
python resize_pdfs.py
```

### Customizing the Resizing

You can customize the target size and orientation by modifying the parameters passed to the `resize_pdf` function in `resize_pdfs.py`. For example, to resize to A4 portrait, update the `resize_pdf` function call as follows:

```python
resize_pdf(input_pdf_path, output_pdf_path, A4, portrait)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
