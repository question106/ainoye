from __future__ import print_function
import os, sys
import shutil
from tkinter import filedialog
from tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("*"*10+"카탈로그 노예 일시작하겠습니다~"+"*"*10)
print("압축기: https://www.ilovepdf.com/compress_pdf")
print("이미지 변환기: https://pdftoimage.com/")



# -------------Catalog dir input
folder_ID = input("Catalog Folder ID? ").strip()
catalog_dir_URL = input("캍탈로그 포르더 주소: ")

# root = Tk()
# root.filename =filedialog.askopenfilename(initialdir = "/",title = "파일 선택",filetypes = (("PDF files","*.pdf",),("All files","*.*")))


# catalog_dir_name_split = root.filename.split("/")
# catalog_dir2 = catalog_dir_name_split[:-1]
# separator = "/"
catalog_dir_folder = separator.join(catalog_dir_URL)
catalog_name1 = catalog_dir_name_split[-1:]
catalog_name2 = separator.join(catalog_name1)
catalog_name = os.path.splitext(catalog_name2)[0]
print(catalog_dir_folder)
print("주인님 잠시 기다려주시업소서~")

catalog_dir_URL1 = catalog_dir_URL.replace(catalog_dir_URL[:3],"")
catalog_dir_folder = catalog_dir_URL1.replace('\\', '/')
#

os.chdir(catalog_dir_folder)
os.mkdir(catalog_dir_folder)
os.mkdir(catalog_dir_folder + "/450")
os.mkdir(catalog_dir_folder + "/3600")
os.mkdir(catalog_dir_folder + f"/{folder_ID}")


# # #--------------Compress PDF
#
# # Required PATHs
# compressor_url = 'https://www.ilovepdf.com/compress_pdf'
# chromedriver_dir = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
# downloadFile_dir = f"{catalog_dir_folder}/{catalog_name}"
# upload_file_dir = root.filename
#
# # Open up a Chrome browser and navigate to web page(PDF viewer disabled)
# chromeOptions = Options()
# prefs = {"plugins.always_open_pdf_externally": True,
#          "download.default_directory": downloadFile_dir,
#          "download.prompt_for_download": False,
#          "download.directory_upgrade": True,
#          "profile.managed_default_content_settings.images": 2
#          }
#
# chromeOptions.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(executable_path=chromedriver_dir, options=chromeOptions)
# driver.get(compressor_url)
#
#
# # Extract the catalog by X_PATH & Download
#
# step1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div[3]/input').send_keys(upload_file_dir)
# step2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[1]').click()
# step2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
#
#
#
#

# # #--------------PDF to Image
#
# pdf2img_url = 'https://pdftoimage.com/'
# upload_file_dir = root.filename
# # os.chdir(upload_file_dir)
# downloadFile_dir = f"{catalog_dir_folder}/{catalog_name}"
# chromedriver_dir = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
#
# print(upload_file_dir)
# print(downloadFile_dir)
# # Open up a Chrome browser and navigate to web page(PDF viewer disabled)
# chromeOptions = Options()
# prefs = {"plugins.always_open_pdf_externally": True,
#          "download.default_directory": downloadFile_dir,
#          "download.prompt_for_download": False,
#          "download.directory_upgrade": True,
#          "profile.managed_default_content_settings.images": 2
#          }
#
# chromeOptions.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(executable_path=chromedriver_dir, options=chromeOptions)
# driver.get(pdf2img_url)
#
#
# # Extract the catalog by X_PATH & Download
# # step2 = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/input').click()
# step1 = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[3]/input').send_keys(upload_file_dir)
#
# RESIZE
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

path_3600= f"{catalog_dir_folder}/3600"

rename(path_3600,"",1,"jpg")


def rename(path_450, new_name, numbering, extension):
    list = os.listdir(path_450)
    os.chdir(path_450)
    count = numbering
    for i in list:
        os.rename(i, new_name + str(count) +"."+ extension)
        count +=1

path_450= f"{catalog_dir_folder}/450"

rename(path_450,"-",1,"jpg")
#
# # MOVE FILES
#
src = f"{path_450}", f"{path_3600}"
dst = f"catalog_dir_folder/{catalog_name}/{folder_ID}"
shutil.move(src, dst)

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