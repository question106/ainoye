from __future__ import print_function
import os, sys
from PIL import Image
import shutil
print("*"*10+"카탈로그 노예 일시작하겠습니다~"+"*"*10)
print("Compress: https://www.ilovepdf.com/compress_pdf")
print("PDF to Image: https://pdftoimage.com/")
# RESIZE
catalog_dir_URL =input(r"Folder URL? ").strip()
folder_ID = input("Catalog Folder ID? ").strip()
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
# path_original = path_3600.replace('/','\\')
# path_thumbnail = path_450.replace('/','\\')
#
# source1 = os.listdir(path_original)
# source2 = os.listdir(path_thumbnail)
# dest = catalog_dir_URL + f"\{folder_ID}"
#
# source1 = "/Users/ADMIN/Desktop/카탈로그/3.Audi/A5-catalog-2019/3600"
# source2 = "/Users/ADMIN/Desktop/카탈로그/3.Audi/A5-catalog-2019/450"
# dest = "/Users/ADMIN/Desktop/카탈로그/3.Audi/A5-catalog-2019/test"
#
# # shutil.move(f"{source1}/1.jpg","/Users/ADMIN/Desktop/카탈로그/3.Audi/A5-catalog-2019/test/1.jpg")
# for f_3600 in source1:
#     shutil.move(f_3600, dest)
# #
# #
# # for f_450 in source2:
# #     shutil.move(f_450, dest)
#
# print(source1)
# print(source2)
# print(dest)
# #