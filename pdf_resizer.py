from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A5, landscape

def resize_pdf(input_pdf, output_pdf, target_size):
    """
    Resize the pages of a PDF to a specified size.

    Parameters:
    - input_pdf: Path to the input PDF file
    - output_pdf: Path to the output resized PDF file
    - target_size: Target page size (width, height) in points
    """
    # Read the input PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Define new page size
    new_width, new_height = target_size

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        
        # Scale the page
        page.scale_to(new_width, new_height)
        
        # Add the scaled page to the writer
        writer.add_page(page)
    
    # Write the resized PDF to the output file
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# Example usage
if __name__ == '__main__':
    input_pdf_path = './2.02_Amplifiers_Conversion-to-dB.pdf'
    output_pdf_path = './2.02_Amplifiers_Conversion-to-dB_resized.pdf'
    resize_pdf(input_pdf_path, output_pdf_path, landscape(A5))
