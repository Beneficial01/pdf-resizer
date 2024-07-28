from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4, A5, landscape, portrait

def resize_pdf(input_pdf, output_pdf, page_size, orientation='portrait'):
    """
    Resize the pages of a PDF to a specified size and orientation.

    Parameters:
    - input_pdf: Path to the input PDF file
    - output_pdf: Path to the output resized PDF file
    - page_size: Target page size (e.g., A4, A5) from reportlab.lib.pagesizes
    - orientation: 'portrait' or 'landscape'
    """
    # Read the input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Define new page size and orientation
    if orientation == 'landscape':
        new_height, new_width = landscape(page_size)
    else:
        new_height, new_width = portrait(page_size)

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        
        # Scale the page
        page.scale_to(new_width, new_height)
        
        # Add the scaled page to the writer
        writer.add_page(page)
    
    # Write the resized PDF to the output file
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
