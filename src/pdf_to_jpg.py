import os
from pdf2image import convert_from_path


def pdf_to_jpg(filePath: str):

    pages = convert_from_path(filePath, 350)

    i = 1

    os.mkdir(filePath)

    for page in pages:
        image_name = "Page_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i+1
