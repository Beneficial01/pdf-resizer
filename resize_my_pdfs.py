import os
from reportlab.lib.pagesizes import *
from pdf_resizer import resize_pdf

# Directory containing the PDFs
input_dir = '/home/beneficial01/Nextcloud/KUL/Bachelor/ACSP/slides/'
output_dir = '/home/beneficial01/Nextcloud/KUL/Bachelor/ACSP/slides/resized/'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all PDF files in the input directory
pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]

# Resize each PDF and save the result in the output directory
for pdf_file in pdf_files:
    input_pdf_path = os.path.join(input_dir, pdf_file)
    output_pdf_path = os.path.join(output_dir, pdf_file)
    # Change 'A4' to 'A5' for example or 'portrait' to 'landscape'
    resize_pdf(input_pdf_path, output_pdf_path, A5, 'landscape')

print("All PDFs have been resized and saved in the 'resized' folder.")
