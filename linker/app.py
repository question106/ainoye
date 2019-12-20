import os
import tempfile
from pdf2image import convert_from_path
from PIL import Image


def convert_pdf(file_path, output_path):
    # save temp image files in temp dir, delete them after we are finished
    # with tempfile.TemporaryDirectory() as temp_dir:
    temp_dir = output_path
    # convert pdf to multiple image
    images = convert_from_path(file_path, output_folder=temp_dir)
    # save images to temporary directory
    temp_images = []
    for i in range(len(images)):
        image_path = f'{temp_dir}/{i}.jpg'
        images[i].save(image_path, 'JPEG')
        temp_images.append(image_path)

# file_path = r"C:\Users\ADMIN\Desktop\Sanjaa\Personal\Fundtice\fundtice_jakwon\fundtice_jakwon.pdf"
# output_path = r"C:\Users\ADMIN\Desktop\Sanjaa\Personal\Fundtice\fundtice_jakwon"
convert_pdf(r"C:\Users\ADMIN\Desktop\카탈로그\1.Benz\Catalogs\cla-catalog-20190917.pdf", r"C:\Users\ADMIN\Desktop\카탈로그\1.Benz\Catalogs")
