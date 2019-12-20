import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, sys
from selenium.webdriver import ActionChains


# Required PATHs
catalog_url = 'https://www.mercedes-benz.co.kr/passengercars/mercedes-benz-cars/catalog/disclaimer-pricelist.module.html'
compressor_url = 'https://www.ilovepdf.com/compress_pdf'
pdf2img_url = 'https://pdftoimage.com/'
chromedriver_dir = r'C:\Users\ADMIN\PycharmProjects\chromedriver.exe'
downloadFile_dir = r"C:\Users\ADMIN\Desktop\Sandbox\downloads\compressed"
upload_file_dir = r"C:\Users\ADMIN\Desktop\Catalog_noye\Resources\downloads\download_1563427360.attachment.EQC_Catalogue_20191114.pdf"

# Open up a Chrome browser and navigate to web page(PDF viewer disabled)
chromeOptions = Options()
prefs = {"plugins.always_open_pdf_externally": True,
         "download.default_directory": downloadFile_dir,
         "download.prompt_for_download": False,
         "download.directory_upgrade": True,
         "profile.managed_default_content_settings.images": 2
         }

chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver_dir, options=chromeOptions)
driver.get(compressor_url)


# Extract the catalog by X_PATH & Download

step1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div[3]/input').send_keys(upload_file_dir)
step2 = driver.find_element_by_id('processTask').click()

