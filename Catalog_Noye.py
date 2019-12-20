from __future__ import print_function
import os, sys
from PIL import Image
import shutil
import time
import pdf2image
import time

print('''
**********카탈로그 노예 일시작하겠습니다~**********
시작: S
도움말: 도움말
닫기: Q
''')
command = ""
while command != "q":
    command = input("> ").lower()
    try:
        if command == "s":
            print("압축 필요시: https://www.ilovepdf.com/compress_pdf")

            folder_ID = input("Omega 카탈로그 ID? ").strip()
            catalog_dir_URL =input("사진들이 있는 폴더 주소를 입력하세요? ").strip()

            print("주인님 잠시 기다려주시업소서~")
            catalog_dir_URL1 = catalog_dir_URL.replace(catalog_dir_URL[:3],"")
            catalog_dir = catalog_dir_URL1.replace('\\', '/')


            os.chdir(catalog_dir_URL)
            os.mkdir(catalog_dir_URL + "/450")

            # PDF to JPG
            # DECLARE CONSTANTS
            PDF_PATH = r"C:\Users\ADMIN\Desktop\Sanjaa\국산차가격표\1.현대\1.작은차\그랜저\grandeur-catalog-201903.pdf"
            DPI = 120
            OUTPUT_FOLDER = r"C:\Users\ADMIN\Desktop\Sanjaa\catalog"
            FIRST_PAGE = None
            LAST_PAGE = None
            FORMAT = 'jpg'
            THREAD_COUNT = 1
            USERPWD = None
            USE_CROPBOX = False
            STRICT = False


            def pdftopil():
                # This method reads a pdf and converts it into a sequence of images
                # PDF_PATH sets the path to the PDF file
                # dpi parameter assists in adjusting the resolution of the image
                # output_folder parameter sets the path to the folder to which the PIL images can be stored (optional)
                # first_page parameter allows you to set a first page to be processed by pdftoppm
                # last_page parameter allows you to set a last page to be processed by pdftoppm
                # fmt parameter allows to set the format of pdftoppm conversion (PpmImageFile, TIFF)
                # thread_count parameter allows you to set how many thread will be used for conversion.
                # userpw parameter allows you to set a password to unlock the converted PDF
                # use_cropbox parameter allows you to use the crop box instead of the media box when converting
                # strict parameter allows you to catch pdftoppm syntax error with a custom type PDFSyntaxError

                start_time = time.time()
                pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER,
                                                         first_page=FIRST_PAGE,
                                                         last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT,
                                                         userpw=USERPWD,
                                                         use_cropbox=USE_CROPBOX, strict=STRICT)
                print("Time taken : " + str(time.time() - start_time))
                return pil_images


            # def save_images(pil_images):
            #     # This method helps in converting the images in PIL Image file format to the required image format
            #     index = 1
            #     for image in pil_images:
            #         image.save("page_" + str(index) + ".jpg")
            #         index += 1

            if __name__ == "__main__":
                pil_images = pdftopil()
                # save_images(pil_images)


            Image.MAX_IMAGE_PIXELS = None

            # RESIZE
            folder_ID = input("Omega 카탈로그 ID? ").strip()
            catalog_dir_URL =input("사진들이 있는 폴더 주소를 입력하세요? ").strip()

            print("주인님 잠시 기다려주시업소서~")
            catalog_dir_URL1 = catalog_dir_URL.replace(catalog_dir_URL[:3],"")
            catalog_dir = catalog_dir_URL1.replace('\\', '/')


            os.chdir(catalog_dir_URL)
            os.mkdir(catalog_dir_URL + "/450")
            os.mkdir(catalog_dir_URL + "/3600")
            os.mkdir(catalog_dir_URL + f"/{folder_ID}")


            size_450 = (10000,150)
            size_3600 = (3600, 3600)

            for f in os.listdir("."):
                if f.endswith(".jpg"):
                    i = Image.open(f)
                    fn, fext = os.path.splitext(f)

                    i.thumbnail(size_3600)
                    i.save("3600/{}{}".format(fn, fext))

                    i.thumbnail(size_450)
                    i.save("450/{}{}".format(fn, fext))


            # RENAME
            def rename(path_3600, new_name, numbering, extension):
                list = os.listdir(path_3600)
                os.chdir(path_3600)
                count = numbering
                for i in list:
                    os.rename(i, new_name + str(count)+"."+extension)
                    count +=1

            path_3600= f"{catalog_dir_URL}/3600"

            rename(path_3600,"",1,"jpg")


            def rename(path_450, new_name, numbering, extension):
                list = os.listdir(path_450)
                os.chdir(path_450)
                count = numbering
                for i in list:
                    os.rename(i, new_name + str(count) +"."+ extension)
                    count +=1

            path_450= f"{catalog_dir_URL}/450"

            rename(path_450,"-",1,"jpg")

            # # MOVE FILES
            #
            # folder_ID = "1234"
            # catalog_dir_URL = r"C:\Users\ADMIN\Downloads\download_1563427360.attachment.EQC_Catalogue_20191114_compressed"
            # path_450_1 = r"C:\Users\ADMIN\Downloads\download_1563427360.attachment.EQC_Catalogue_20191114_compressed\450"
            # path_3600_1 = r"C:\Users\ADMIN\Downloads\download_1563427360.attachment.EQC_Catalogue_20191114_compressed\3600"

            # catalog_dir_URL1 = catalog_dir_URL.replace(catalog_dir_URL[:3],"")
            # catalog_dir = catalog_dir_URL1.replace('\\', '/')
            #
            # path_450_2 = path_450_1.replace(path_450_1[:3],"")
            # path_450 = path_450_2.replace('\\', '/')
            #
            # path_3600_2 = path_3600_1.replace(path_3600_1[:3],"")
            # path_3600 = path_3600_2.replace('\\', '/')



            source1 = f"{path_450}/"
            source2 = f"{path_3600}/"
            dest1 = f"{catalog_dir_URL}/{folder_ID}"


            files_450 = os.listdir(source1)

            for f in files_450:
                    shutil.move(source1+f, dest1)

            files_3600 = os.listdir(source2)

            for f in files_3600:
                shutil.move(source2+f, dest1)

            # time.sleep(0.5)
            # shutil.rmtree(f"{path_450}")
            # time.sleep(0.5)
            # shutil.rmtree(f"{path_3600}")
        elif command == "help":
            print("도움이 필요하세요? 기도하세요~ㅋㅋㅋ")
        elif command == "quit":
            break
        else:
            print("IQq가 딸려서 이해 못함 ㅠㅠ")
    except FileExistsError:
        print("같은 이름의 파일이 이미 존재합니다")

