import os
import tempfile
from pdf2image import convert_from_path
from PIL import Image
def convert_pdf(file_path, output_path):
    # save temp image files in temp dir, delete them after we are finished
    with tempfile.TemporaryDirectory() as temp_dir:
        # convert pdf to multiple image
        images = convert_from_path(file_path, output_folder=temp_dir)
        # save images to temporary directory
        temp_images = []
        for i in range(len(images)):
            image_path = f'{temp_dir}/{i}.jpg'
            images[i].save(image_path, 'JPEG')
            temp_images.append(image_path)
        # read images into pillow.Image
        imgs = list(map(Image.open, temp_images))
    # find minimum width of images
    min_img_width = min(i.width for i in imgs)
    # find total height of all images
    total_height = 0
    for i, img in enumerate(imgs):
        total_height += imgs[i].height
    # create new image object with width and total height
    merged_image = Image.new(imgs[0].mode, (min_img_width, total_height))
    # paste images together one by one
    y = 0
    for img in imgs:
        merged_image.paste(img, (0, y))
        y += img.height
    # save merged image
    merged_image.save(output_path)
    return output_path

# file_path = r"C:\Users\ADMIN\Desktop\Sanjaa\Personal\Fundtice\fundtice_jakwon\fundtice_jakwon.pdf"
# output_path = r"C:\Users\ADMIN\Desktop\Sanjaa\Personal\Fundtice\fundtice_jakwon"
convert_pdf(r"C:\Users\ADMIN\Desktop\카탈로그\1.Benz\Catalogs\cla-catalog-20190917.pdf", r"C:\Users\ADMIN\Desktop\카탈로그\1.Benz\Catalogs")