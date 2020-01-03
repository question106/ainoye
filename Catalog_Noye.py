from __future__ import print_function
import os, sys
from PIL import Image
import shutil
import time
import pdf2image
import time

operating = True
Image.MAX_IMAGE_PIXELS = None

while operating:
    print('''
작업 단계:
1) PDF 파일의 크기가 20MB 보다 크면 (https://www.ilovepdf.com/compress_pdf) 이 사이트로 가셔서 압축하시면 됩니다.
2) PDF -> JPG 변환 할 때 (https://www.ilovepdf.com/pdf_to_jpg) 이 사이트로 가셔서 변환하면 됩니다.
3) PDF 파일을 오메가에 업로드하고 ID를 작 기억해두기.
    ''')

    folder_ID = input("Omega file ID: ").strip()
    catalog_dir_URL = input(r"JPG Folder: ").strip()

    print("주인님 잠시 기다려주시업소서~")
    # catalog_dir_URL1 = catalog_dir_URL.replace(catalog_dir_URL[:3], "")
    # catalog_dir = catalog_dir_URL1.replace('\\', '/')
    start_time = time.time()
    print(f"{os.path.basename(catalog_dir_URL)}: 작업중...")


    try:
        os.chdir(catalog_dir_URL)
        os.mkdir(catalog_dir_URL + "/450")
    except FileExistsError:
        pass
    try:
        os.mkdir(catalog_dir_URL + "/3600")
    except FileExistsError:
        pass
    try:
        os.mkdir(catalog_dir_URL + f"/{folder_ID}")
    except FileExistsError:
        pass

    # RESIZE

    for f in os.listdir("."):
        if f.endswith(".jpg"):
            i = Image.open(f)
            fn, fext = os.path.splitext(f)

            size_3600 = (3600, 3600)
            i.thumbnail(size_3600)
            i.save("3600/{}{}".format(fn, fext))

            width, height = i.size

            if width < height or width == height:

                size_450 = (200, 100000)
                i.thumbnail(size_450)

                left = 0
                top = 0
                right = 200
                bottom = 150

                im = i.crop((left, top, right, bottom))
                im.save("450/{}{}".format(fn, fext))

            elif width > height:

                size_450 = (1000000, 150)
                i.thumbnail(size_450)
                w, h = i.size
                start_pixel = (w - 200) / 2
                end_pixel = start_pixel + 200
                im = i.crop((start_pixel, 0, end_pixel, 150))
                im.save("450/{}{}".format(fn, fext))



    # RENAME
    def rename(path_3600, new_name, numbering, extension):
        list = os.listdir(path_3600)
        os.chdir(path_3600)
        count = numbering
        for i in list:
            os.rename(i, new_name + str(count) + "." + extension)
            count += 1


    path_3600 = f"{catalog_dir_URL}/3600"

    rename(path_3600, "", 1, "jpg")


    def rename(path_450, new_name, numbering, extension):
        list = os.listdir(path_450)
        os.chdir(path_450)
        count = numbering
        for i in list:
            os.rename(i, new_name + str(count) + "." + extension)
            count += 1


    path_450 = f"{catalog_dir_URL}/450"

    rename(path_450, "-", 1, "jpg")

    # MOVE FILES
    source1 = f"{path_450}/"
    source2 = f"{path_3600}/"
    dest1 = f"{catalog_dir_URL}/{folder_ID}"

    files_450 = os.listdir(source1)

    for f in files_450:
        shutil.move(source1 + f, dest1)

    files_3600 = os.listdir(source2)

    for f in files_3600:
        shutil.move(source2 + f, dest1)
    print(f"{os.path.basename(catalog_dir_URL)}: 작업 완료!({round(time.time() - start_time, 2)}초 걸림)")
    time.sleep(1)

