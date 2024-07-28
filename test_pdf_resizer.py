import unittest
import os
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import A4, A5, landscape
from reportlab.pdfgen import canvas

# Import the resize_pdf function from the script
from pdf_resizer import resize_pdf

class TestPDFResizer(unittest.TestCase):
    
    def setUp(self):
        # Create a sample PDF for testing
        self.input_pdf_path = 'sample_input.pdf'
        self.output_pdf_path = 'sample_output.pdf'
        self.create_sample_pdf(self.input_pdf_path)
    
    def tearDown(self):
        # Remove the sample PDF files after tests
        if os.path.exists(self.input_pdf_path):
            os.remove(self.input_pdf_path)
        if os.path.exists(self.output_pdf_path):
            os.remove(self.output_pdf_path)
    
    def create_sample_pdf(self, path):
        # Create a simple A4-sized PDF file for testing
        c = canvas.Canvas(path, pagesize=A4)
        c.drawString(100, 750, "This is a sample PDF for testing.")
        c.showPage()
        c.save()
    
    def test_resize_to_a5(self):
        # Resize the sample PDF from A4 to A5
        resize_pdf(self.input_pdf_path, self.output_pdf_path, landscape(A5))
        
        # Check if the output PDF exists
        self.assertTrue(os.path.exists(self.output_pdf_path))
        
        # Check the dimensions of the resized PDF
        reader = PdfReader(self.output_pdf_path)
        page = reader.pages[0]
        width, height = page.mediabox.upper_right
        
        expected_width, expected_height = landscape(A5)
        self.assertAlmostEqual(width, expected_width, delta=1)
        self.assertAlmostEqual(height, expected_height, delta=1)

if __name__ == '__main__':
    unittest.main()
