# Requires Python 3.6 or higher due to f-strings

# Import libraries
import platform
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

if platform.system() == "Windows":

	pytesseract.pytesseract.tesseract_cmd = (
		r".\tesseract-ocr\tesseract.exe"
	)
	
	path_to_poppler_exe = Path(r".\poppler-0.68.0\bin")
	
	# Path of the Output txt
	out_directory = Path(r"~\OneDrive\Escritorio").expanduser()
else:
	out_directory = Path("~").expanduser()

# Path of the Input pdf
PDF_file = Path(r".\test\InvoiceSimple-PDF-Template.pdf")

# Store all the pages of the PDF in a variable
image_file_list = []

text_file = out_directory / Path("out_text.txt")

def main():
	''' Main execution point of the program'''
	with TemporaryDirectory() as tempdir:
		# Create a temporary directory to hold our temporary images.

		"""
		Part #1 : Converting PDF to images
		"""

		if platform.system() == "Windows":
			pdf_pages = convert_from_path(
				PDF_file, 350, poppler_path=path_to_poppler_exe
			)
		else:
			pdf_pages = convert_from_path(PDF_file, 350)
		# Read in the PDF file at 350 DPI

		# Iterate through all the pages stored above
		for page_enumeration, page in enumerate(pdf_pages, start=1):
			# enumerate() "counts" the pages for us.

			# Create a file name to store the image
			filename = f"{tempdir}\page_{page_enumeration:03}.jpg"

			# Save the image of the page in system
			page.save(filename, "JPEG")
			image_file_list.append(filename)

		"""
		Part #2 - Recognizing text from the images using OCR
		"""

		with open(text_file, "a") as output_file:
			# Open the file in append mode so that
			# All contents of all images are added to the same file

			# Iterate from 1 to total number of pages
			for image_file in image_file_list:

				# Recognize the text as string in image using pytesserct
				text = str(((pytesseract.image_to_string(Image.open(image_file)))))

				# The recognized text is stored in variable text
				# Any string processing may be applied on text
				text = text.replace("-\n", "")

				# Finally, write the processed text to the file.
				output_file.write(text)

	
if __name__ == "__main__":
	# We only want to run this if it's directly executed!
	main()
